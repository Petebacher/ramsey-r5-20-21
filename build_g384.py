"""Build G384, a (5,17)-graph on 384 vertices: one colour class of Mathon's cubic-residue 3-colouring M_p for
p = 127, in the form of X. Xu and S. P. Radziszowski, "An improvement to Mathon's cyclotomic Ramsey colorings",
Electron. J. Combin. 16 (2009) #N1 (Figure 1 of that paper, without the three extra vertices w0, w1, w2).

Rule (from the paper):
  vertices U = {(0,1), (0,b), (0,b^2)} and V_i = {(b^i, a) : a in Z_p} for i = 0, 1, 2 (b = 3, a primitive root
  mod 127), in the order U, V_0, V_1, V_2 with a = 0..126 inside each V_i;
  the edge {(x,y),(s,t)} gets colour i in {0,1,2} when x*t - y*s = b^(3r+i) mod p for some r;
  when x*t - y*s = 0 the edge has the special colour c. Those edges form p + 1 disjoint triangles: U, and one
  triangle inside V for each of the other p lines through the origin.
Recolouring of the special colour, as used here:
  the p triangles inside V get colour 0; the three edges inside U get the colours of the U rows of Figure 1
  (u0u1 = 0, u0u2 = 1, u1u2 = 2 in the figure's labels), translated to our colour labels by the unique
  permutation of colours that makes the figure's U-to-V block agree with the computed colouring.
G384 = the graph of colour 0 (in our labels).
Usage: python3 build_g384.py out.txt   (standard library only)"""
import itertools, sys
p, b = 127, 3
assert len({pow(b, e, p) for e in range(p - 1)}) == p - 1, 'b is not a primitive root'
log = {pow(b, e, p): e for e in range(p - 1)}
U = [(0, 1), (0, b), (0, b * b % p)]
V = [(pow(b, i, p), a) for i in range(3) for a in range(p)]
X = U + V
n = len(X)
C = [[None] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            (x, y), (s, t) = X[i], X[j]
            d = (x * t - y * s) % p
            C[i][j] = 'c' if d == 0 else log[d] % 3
assert all(C[i][j] == C[j][i] for i in range(n) for j in range(n))
# special colour: U is one triangle, the rest are triangles inside V
assert all(C[i][j] == 'c' for i in range(3) for j in range(3) if i != j)
assert all(C[i][j] != 'c' for i in range(3) for j in range(3, n))
assert sum(C[i][j] == 'c' for i in range(3, n) for j in range(i + 1, n)) == 3 * p
# Figure 1, U rows: colour of u_i to all of V_j, and inside U
figUV = [(1, 2, 0), (2, 0, 1), (0, 1, 2)]
figUU = {(0, 1): 0, (0, 2): 1, (1, 2): 2}
act = [tuple(C[i][3 + j * p] for j in range(3)) for i in range(3)]
for i in range(3):   # each u_i has one colour to each whole V_j
    assert all(C[i][3 + j * p + a] == act[i][j] for j in range(3) for a in range(p))
match = [pi for pi in itertools.permutations(range(3)) if [tuple(pi[c] for c in r) for r in figUV] == act]
assert len(match) == 1, 'figure labels do not match the computed colouring'
pi = match[0]
for (i, j), c in figUU.items():
    C[i][j] = C[j][i] = pi[c]
for i in range(3, n):
    for j in range(3, n):
        if C[i][j] == 'c':
            C[i][j] = 0
A = [[1 if i != j and C[i][j] == 0 else 0 for j in range(n)] for i in range(n)]
open(sys.argv[1], 'w').write('\n'.join(''.join(map(str, r)) for r in A) + '\n')
print('G384 built:', n, 'vertices,', sum(map(sum, A)) // 2, 'edges; figure-to-computed colour map', pi)
