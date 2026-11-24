"""Rebuild the graphs of this release: R5_20_426.txt (R(5,20) >= 427), R5_20_425.txt (R(5,20) >= 426, kept as
history) and R5_21_446.txt (R(5,21) >= 447).

Construction: Theorem 3 of X. Xu, Z. Shao and S. P. Radziszowski, "More constructive lower bounds on classical
Ramsey numbers", SIAM J. Discrete Math. 25 (2011) 394-400, with k = 5:
  G = G384.txt, a (5,17)-graph on 384 vertices (Mathon's cubic-residue colouring, p = 127; see build_g384.py);
  H = the complement of one of B. D. McKay's graphs (the g6 line in this folder), a (5,4)- or (5,5)-graph;
  M = the common induced subgraph given in the common_part file (pairs u:y:side, u in H, y in G, side 1 or 2).
The graph F has vertices G (0..383), then H, then w_0..w_{m-1} in the order of the common_part file. Edges:
  all of G; all of H; the matching y_i -- u_i; w_i joined to the G-neighbours of y_i and the H-neighbours of u_i;
  among the w's only the edges of M[W1] and of M[W2] (none between W1 and W2).
H is decoded here from McKay's g6 line and complemented, so the H files are also checked.
Usage: python3 build.py OUTDIR   (standard library only). Writes OUTDIR/H24.txt, OUTDIR/H24_line119677.txt,
OUTDIR/H42.txt, OUTDIR/R5_20_425.txt, OUTDIR/R5_20_426.txt and OUTDIR/R5_21_446.txt; reproduce.sh compares them byte for byte with the shipped files."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def read01(fn):
    rows = [r.strip() for r in open(fn) if r.strip()]
    n = len(rows)
    assert all(len(r) == n and set(r) <= {'0', '1'} for r in rows), fn + ': not an n x n 0/1 matrix'
    return [[int(c) for c in r] for r in rows]


def g6_decode(s):
    s = s.strip()
    n = ord(s[0]) - 63
    assert 0 < n < 63
    bits = []
    for ch in s[1:]:
        v = ord(ch) - 63
        bits += [(v >> k) & 1 for k in range(5, -1, -1)]
    A = [[0] * n for _ in range(n)]
    k = 0
    for j in range(1, n):
        for i in range(j):
            A[i][j] = A[j][i] = bits[k]
            k += 1
    return A


def complement(A):
    n = len(A)
    return [[0 if i == j else 1 - A[i][j] for j in range(n)] for i in range(n)]


def read_pairs(fn):
    pairs = []
    for line in open(fn):
        line = line.strip()
        if line and not line.startswith('#'):
            u, y, s = map(int, line.split(':'))
            pairs.append((u, y, s))
    return pairs


def build(G, H, pairs):
    n1, n2, m = len(G), len(H), len(pairs)
    U = [u for u, y, s in pairs]
    Y = [y for u, y, s in pairs]
    S = [s for u, y, s in pairs]
    assert len(set(U)) == m and len(set(Y)) == m and set(S) == {1, 2}
    for a in range(m):
        for b in range(m):
            assert G[Y[a]][Y[b]] == H[U[a]][U[b]], 'M is not a common induced subgraph'
    N = n1 + n2 + m
    F = [[0] * N for _ in range(N)]
    for i in range(n1):
        for j in range(n1):
            F[i][j] = G[i][j]
    for i in range(n2):
        for j in range(n2):
            F[n1 + i][n1 + j] = H[i][j]
    for a in range(m):
        w = n1 + n2 + a
        F[Y[a]][n1 + U[a]] = F[n1 + U[a]][Y[a]] = 1
        for j in range(n1):
            if G[Y[a]][j]:
                F[w][j] = F[j][w] = 1
        for j in range(n2):
            if H[U[a]][j]:
                F[w][n1 + j] = F[n1 + j][w] = 1
        for b in range(m):
            if S[a] == S[b] and H[U[a]][U[b]]:
                F[w][n1 + n2 + b] = 1
    assert all(F[i][j] == F[j][i] for i in range(N) for j in range(N)) and all(F[i][i] == 0 for i in range(N))
    return F


def write01(A, fn):
    open(fn, 'w').write('\n'.join(''.join(map(str, r)) for r in A) + '\n')


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    G = read01(os.path.join(HERE, 'G384.txt'))
    assert len(G) == 384
    jobs = (('mckay_r45_24_line3521.g6', 'H24.txt', 'common_part_r5_20_m17.txt', 'R5_20_425.txt', 24),
            ('mckay_r45_24_line119677.g6', 'H24_line119677.txt', 'common_part_r5_20_m18.txt', 'R5_20_426.txt', 24),
            ('mckay_r55_42some_line94.g6', 'H42.txt', 'common_part_r5_21_m20.txt', 'R5_21_446.txt', 42))
    for g6f, hname, pf, fname, nh in jobs:
        H = complement(g6_decode(open(os.path.join(HERE, g6f)).read()))
        assert len(H) == nh
        write01(H, os.path.join(out, hname))
        pairs = read_pairs(os.path.join(HERE, pf))
        F = build(G, H, pairs)
        write01(F, os.path.join(out, fname))
        print('built %s: %d vertices = 384 + %d + %d (|W1| = %d, |W2| = %d)' % (
            fname, len(F), nh, len(pairs), sum(s == 1 for _, _, s in pairs), sum(s == 2 for _, _, s in pairs)))


if __name__ == '__main__':
    main()
