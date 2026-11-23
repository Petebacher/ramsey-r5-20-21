"""Check that a graph F is exactly the construction of Theorem 3 of Xu, Shao and Radziszowski (SIAM J. Discrete
Math. 25 (2011) 394-400) and that the theorem's hypotheses hold. Standard library only; written separately from
build.py (it recovers the construction from F itself and only then compares with the input files).

Checks:
 1. F is a symmetric 0/1 matrix with zero diagonal on n(G) + n(H) + m vertices.
 2. F's first n(G) rows are G and the next n(H) rows are H (the given files).
 3. From F alone: the G-H edges are a matching of size m; every one of the last m vertices w is joined to exactly
    the G-neighbours of one matched G vertex y and the H-neighbours of its partner u, and to neither of them.
 4. The recovered pairs equal the common_part file, in order.
 5. M is common and induced: G[y_a, y_b] = H[u_a, u_b] for all pairs.
 6. The w's induce exactly M[W1] u M[W2] for a split W1, W2 (recovered from F, compared with the file), both
    nonempty, no edge between W1 and W2.
 7. The theorem's condition, word for word: for i = 1, 2 and every v in V(M) - W_i, M[W_i u {v}] has no K_(k-1).
    (Also reported: K_(k-1) count of M and how each splits, triangles inside each part.)
 8. G has no K_k; H has no K_k and no independent set of size t (exact, by bitset search).
    That G has no independent set of size s is checked by the two C checkers in reproduce.sh (too slow in Python).
Usage: python3 verify_hypotheses.py F.txt G.txt H.txt common_part.txt k s t"""
import itertools
import sys


def read01(fn):
    rows = [r.strip() for r in open(fn) if r.strip()]
    n = len(rows)
    assert all(len(r) == n and set(r) <= {'0', '1'} for r in rows), fn + ': not an n x n 0/1 matrix'
    A = [[int(c) for c in r] for r in rows]
    assert all(A[i][j] == A[j][i] for i in range(n) for j in range(n)), fn + ': not symmetric'
    assert all(A[i][i] == 0 for i in range(n)), fn + ': nonzero diagonal'
    return A


def bits(A):
    return [sum(1 << j for j, x in enumerate(r) if x) for r in A]


def has_clique(nb, cand, r):
    """Is there a clique of size r inside the vertex set cand (bitmask)? nb = neighbour bitmasks."""
    if r == 0:
        return True
    if bin(cand).count('1') < r:
        return False
    while cand:
        v = cand.bit_length() - 1
        cand &= ~(1 << v)
        if has_clique(nb, cand & nb[v], r - 1):
            return True
        if bin(cand).count('1') < r:
            return False
    return False


def comp_bits(A):
    n = len(A)
    full = (1 << n) - 1
    return [full & ~nb & ~(1 << i) for i, nb in enumerate(bits(A))]


def main():
    Ff, Gf, Hf, Pf = sys.argv[1:5]
    k, s, t = map(int, sys.argv[5:8])
    F, G, H = read01(Ff), read01(Gf), read01(Hf)
    nG, nH, N = len(G), len(H), len(F)
    m = N - nG - nH
    print('F: %d vertices, %d edges; n(G) = %d, n(H) = %d, m = %d' % (N, sum(map(sum, F)) // 2, nG, nH, m))
    # 2. blocks
    assert all(F[i][:nG] == G[i] for i in range(nG)), 'G block differs from ' + Gf
    assert all(F[nG + i][nG:nG + nH] == H[i] for i in range(nH)), 'H block differs from ' + Hf
    print('[ok] rows 0..%d are G and rows %d..%d are H' % (nG - 1, nG, nG + nH - 1))
    # 3. recover the construction from F alone
    Gr, Hr, Zr = range(nG), range(nG, nG + nH), range(nG + nH, N)
    cross = [(y, u) for y in Gr for u in Hr if F[y][u]]
    assert len(cross) == m and len({y for y, _ in cross}) == m and len({u for _, u in cross}) == m, \
        'G-H edges are not a matching of size m (%d edges)' % len(cross)
    rec = []
    for w in Zr:
        NG = {j for j in Gr if F[w][j]}
        NH = {j for j in Hr if F[w][j]}
        c = [(y, u) for y, u in cross
             if NG == {j for j in Gr if F[y][j]} and NH == {j for j in Hr if F[u][j]}]
        assert len(c) == 1, 'w = %d does not copy exactly one matched pair' % w
        y, u = c[0]
        assert not F[w][y] and not F[w][u]
        rec.append((y, u))
    assert len(set(rec)) == m
    print('[ok] G-H edges: a matching of size %d; each of the last %d vertices is the twin of one matched pair' % (m, m))
    # 4. compare with the file
    pairs = []
    for line in open(Pf):
        line = line.strip()
        if line and not line.startswith('#'):
            pairs.append(tuple(map(int, line.split(':'))))
    assert [(y, nG + u) for u, y, _ in pairs] == rec, 'recovered pairs differ from ' + Pf
    print('[ok] recovered pairs equal', Pf)
    Y = [y for y, _ in rec]
    Uh = [u - nG for _, u in rec]
    # 5. common and induced
    M = [[G[Y[a]][Y[b]] for b in range(m)] for a in range(m)]
    assert all(M[a][b] == H[Uh[a]][Uh[b]] for a in range(m) for b in range(m)), 'M is not common and induced'
    print('[ok] M is an induced subgraph of both G and H (%d vertices, %d edges)' % (m, sum(map(sum, M)) // 2))
    # 6. split recovered from the w's: an M edge present among the w's = same side, missing = different sides
    Z = [[F[nG + nH + a][nG + nH + b] for b in range(m)] for a in range(m)]
    assert all(not Z[a][b] or M[a][b] for a in range(m) for b in range(m)), 'the w part has an edge M lacks'
    side, comps = {}, []
    for r in range(m):
        if r in side:
            continue
        side[r] = 0
        comp, st = [r], [r]
        while st:
            x = st.pop()
            for y in range(m):
                if M[x][y]:
                    want = side[x] if Z[x][y] else 1 - side[x]
                    if y in side:
                        assert side[y] == want, 'the w part is not M[W1] u M[W2] for any split'
                    else:
                        side[y] = want
                        comp.append(y)
                        st.append(y)
        comps.append(comp)
    # each component of M may be flipped; try all choices (one component here)
    good = None
    for flips in itertools.product((0, 1), repeat=len(comps) - 1):
        sd = dict(side)
        for c, f in zip(comps[1:], flips):
            for x in c:
                sd[x] ^= f
        W = [{a for a in range(m) if sd[a] == q} for q in (0, 1)]
        if not W[0] or not W[1]:
            continue
        ok = True
        for i in (0, 1):
            Wi = W[i]
            for v in W[1 - i]:
                S = Wi | {v}
                nb = [sum(1 << b for b in S if M[a][b]) if a in S else 0 for a in range(m)]
                if has_clique(nb, sum(1 << a for a in S), k - 1):
                    ok = False
        if ok:
            good = W
            break
    assert good, 'no split satisfies the condition of Theorem 3'
    W1, W2 = good
    fileW = [{a for a, p in enumerate(pairs) if p[2] == q} for q in (1, 2)]
    assert {frozenset(W1), frozenset(W2)} == {frozenset(fileW[0]), frozenset(fileW[1])}, 'split differs from file'
    print('[ok] the w part induces exactly M[W1] u M[W2], no edge between; |W1| = %d, |W2| = %d (from the file: %d, %d)'
          % (len(W1), len(W2), len(fileW[0]), len(fileW[1])), '; M has %d component(s)' % len(comps))
    print('[ok] Theorem 3 condition: for i = 1, 2 and every v in V(M) - W_i, M[W_i u {v}] has no K%d' % (k - 1))
    K = [c for c in itertools.combinations(range(m), k - 1) if all(M[a][b] for a, b in itertools.combinations(c, 2))]
    spl = sorted({(len(set(c) & fileW[0]), len(set(c) & fileW[1])) for c in K})
    tri = [sum(1 for c in itertools.combinations(sorted(W), 3) if all(M[a][b] for a, b in itertools.combinations(c, 2)))
           for W in fileW]
    print('     info: M has %d copies of K%d, splits (W1, W2) = %s; triangles inside W1, W2: %d, %d'
          % (len(K), k - 1, spl, tri[0], tri[1]))
    # 8. clique and independence bounds
    full = lambda n: (1 << n) - 1
    assert not has_clique(bits(G), full(nG), k), 'G contains K%d' % k
    print('[ok] G has no K%d (independent sets of size %d in G: checked by the C checkers)' % (k, s))
    assert not has_clique(bits(H), full(nH), k), 'H contains K%d' % k
    assert not has_clique(comp_bits(H), full(nH), t), 'H has an independent %d-set' % t
    assert has_clique(comp_bits(H), full(nH), t - 1)
    print('[ok] H has no K%d and no independent set of size %d (one of size %d exists): H is a (%d,%d)-graph'
          % (k, t, t - 1, k, t))
    print('[ok] arithmetic: s + t - 1 = %d; n(G) + n(H) + n(M) = %d + %d + %d = %d, so R(%d,%d) >= %d'
          % (s + t - 1, nG, nH, m, N, k, s + t - 1, N + 1))
    print('HYPOTHESES OK (given that G has no independent %d-set)' % s)


if __name__ == '__main__':
    main()
