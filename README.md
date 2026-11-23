# R(5,20) ≥ 426 and R(5,21) ≥ 447

This repository gives two graphs:

- `R5_20_425.txt`: a graph on **425 vertices** with no clique of 5 vertices and no independent set of 20 vertices. It shows that **R(5,20) ≥ 426**.
- `R5_21_446.txt`: a graph on **446 vertices** with no clique of 5 vertices and no independent set of 21 vertices. It shows that **R(5,21) ≥ 447**.

The file names give the number of vertices; the bound is one more.

Both graphs are built with Theorem 3 of Xu, Shao and Radziszowski (2011), from published ingredients: a 384-vertex graph of Mathon's cyclotomic type and a graph from B. D. McKay's lists. What is new is the common induced subgraph that glues them together, which is larger than those used before for these two numbers (17 vertices against 12 for R(5,20), 20 against 18 for R(5,21)). The absence of a 5-clique was checked directly on both finished graphs by two independently written exact programs. The absence of the large independent set rests on Theorem 3, whose hypotheses were all checked by machine. In addition, for the 425-vertex graph one exact program searched directly and found no independent set of size 20; for the 446-vertex graph no direct search of that side has been completed (details below).

## Previous bounds

| | survey (DS1 rev. 18, Table IIa) | best public bound we found before this work | this work |
|---|---|---|---|
| R(5,20) | ≥ 424, reference [XSR2] (Xu, Shao and Radziszowski 2011, a 423-vertex Theorem 3 graph built from a 387-vertex G, a 24-vertex H and a 12-vertex common part) | ≥ 424 (the survey value) | ≥ 426 |
| R(5,21) | ≥ 441, by survey item 2.3.i | ≥ 445: Byungkun Jang, 11 November 2026, github.com/8rulerstar/ramsey-lower-bounds, folder `r5-21` (Zenodo concept DOI 10.5281/zenodo.24128875), a 444-vertex Theorem 3 graph with G = the same 384-vertex graph used here, H = graph number 2 of McKay's `r55_42some.g6`, common part 18 | ≥ 447 |

Survey: S. P. Radziszowski, *Small Ramsey Numbers*, Electronic Journal of Combinatorics, Dynamic Survey DS1, revision 18 (24 April 2026), https://doi.org/10.37236/21.

What we searched, all on 23 November 2026 (UTC): the survey (local copy of revision 18); Jang's repository (re-read at 20:39: newest commit 23 November 01:02, about R(8,12); the `r5-21` folder unchanged since 11 November; his README still lists R(5,21) ≥ 445 and has no R(5,20) entry); GitHub repositories about Ramsey numbers (pushed since 1 October, read at about 19:25; those pushed since 19:00, re-read at 20:39); the Leaps in Bounds tracker (no row for R(5,20) or R(5,21)); Google Research's `ramsey_number_bounds/improved_bounds` folder (no R(5,·) file); the Quantavane records (none for these cells); the 60 newest arXiv papers on Ramsey lower bounds (to 18 November); the 25 newest Zenodo records about Ramsey numbers (about 19:00); and general web searches. An independent re-check between 20:47 and 20:50 UTC found Jang's repository unchanged, searched Zenodo with five queries ("Ramsey number", "Ramsey numbers", "R(5,20)", "R(5,21)", and Jang as creator; his newest record is version 1.7 of 20 November, on other work), and repeated the GitHub and web searches. We found no bound above 424 for R(5,20) or above 445 for R(5,21). We cannot see private communications, mailing lists or social media.

Published formulas do not reach these values. Survey item 2.3.i gives R(5,l) ≥ 4 R(3,l−1) − 3, which is 4 × 106 − 3 = 421 for l = 20 and 4 × 111 − 3 = 441 for l = 21 with today's R(3,19) ≥ 106 and R(3,20) ≥ 111. (If someone shows R(3,20) ≥ 113, that formula would give R(5,21) ≥ 449.) Corollary 3 of [XSR2], R(k, s+t−1) ≥ R(k,s) + R(k,t) + k − 2, gives at most 419 and 434.

Earlier on the same day we had found common parts of 16 and 19 vertices (graphs on 424 and 445 vertices). Those were intermediate steps of the same search and are not separate results.

## The theorem

X. Xu, Z. Shao and S. P. Radziszowski, "More constructive lower bounds on classical Ramsey numbers", SIAM Journal on Discrete Mathematics 25 (2011) 394-400, Theorem 3. Quoted from the authors' preprint of that paper (dated 14 September 2010). The paper writes the vertex set of M as "VM" (and V G, E F for G and F); we write V_M, and index subscripts such as W_1 and K_{k−1} with underscores:

> **Theorem 3** Let k ≥ 4 and s, t ≥ 2. Given a (k, s)-graph G and a (k, t)-graph H, let M be a graph isomorphic to induced subgraphs of G and H. If the vertex set V_M can be partitioned into two nonempty sets, V_M = W_1 ∪ W_2, so that for every v ∈ V_M − W_i and i ∈ {1, 2} there is no K_{k−1} in M[W_i ∪ {v}], then
>
> R(k, s + t − 1) ≥ n(G) + n(H) + n(M) + 1.

A (k, s)-graph is a graph with no clique of size k and no independent set of size s.

**This is the full condition, not the triangle-free shorthand.** For k = 5 the condition says: every K4 of M has exactly two vertices in W_1 and two in W_2 (a K4 with three or four vertices on one side is excluded, and so is a K4 inside one side, because the other side is nonempty). A simpler sufficient form, used by Jang and stated after the theorem in the paper, asks that neither part contain a K_{k−2}, which for k = 5 means both parts are triangle-free. **Our parts contain triangles,** so that simpler form does not apply, and a checker that asserts it (such as the one in Jang's `build.py`) will reject our common parts. The full condition holds:

| | R(5,20) graph | R(5,21) graph |
|---|---|---|
| k, s, t | 5, 17, 4 | 5, 17, 5 |
| n(G) + n(H) + n(M) | 384 + 24 + 17 = 425 | 384 + 42 + 20 = 446 |
| \|W_1\|, \|W_2\| | 6, 11 | 9, 11 |
| copies of K4 in M | 0 | 18, every one split 2 and 2 |
| triangles inside W_1, W_2 | 0, 17 | 1, 10 |
| edges of M | 68 | 79 |

**R(5,20): the common part is the Paley graph on 17 vertices.** It has no K4 and, as an induced subgraph of H, no independent set of size 4; the only such graph on 17 vertices is Paley(17), and `verify_hypotheses.py` confirms the K4 count (we also checked the isomorphism directly). So for R(5,20) the plain survey item 2.3.h ("a common induced subgraph on m vertices without K_{k−1}", Radziszowski DS1 rev. 18, page 12) already applies, with p = 4 and q = 17. Since R(4,4) = 18, 17 is also the largest common part without K4 that is possible; a larger one would have to contain K4s, all split 2 and 2.

## The construction

Write G = G384 (vertices u_1, ..., u_p), H (vertices v_1, ..., v_q), and let the common part M be given by pairs (u_i, v_i), i = 1, ..., m, such that u_i ↦ v_i is an isomorphism between G[{u_i}] and H[{v_i}], with each i on side W_1 or W_2. The graph F has vertex set V(G) ∪ V(H) ∪ {w_1, ..., w_m} and these edges:

- all edges of G and all edges of H;
- the matching u_i v_i for i = 1, ..., m;
- w_i u_j whenever u_i u_j is an edge of G (j ≠ i), and w_i v_j whenever v_i v_j is an edge of H;
- w_i w_j whenever i and j are on the same side and adjacent in M; no edges between W_1 and W_2.

So w_i is a "twin" of the matched pair (u_i, v_i): it has the neighbours of u_i in G and of v_i in H, and is joined to neither u_i nor v_i. In the files the vertex order is G (rows 0 to 383), then H, then w_1, ..., w_m in the order of the `common_part` file. Note that the `common_part` files use the letters differently from this text: in a line `u:y:side`, u is a vertex of H and y a vertex of G (here u_i is in G and v_i in H).

## Proof that the construction works

We give a complete proof because the paper's proof is short ("directly from the construction it can be concluded"), and its Case 2 writes w_j ∈ W_1 where it means w_j ∈ S_3. The argument below follows an independent review of this release and was checked again by us. Identify the index i with the vertex of M it labels.

**No K_k.** Suppose S is a clique of F with k vertices. There are no edges between W_1 and W_2, so S meets at most one of them, say (by symmetry) S ∩ W ⊆ W_1.

- *S meets both V(G) and V(H).* The only edges between V(G) and V(H) are the matching edges, so S contains exactly one u_j and exactly one v_j, with the same j, and the other k − 2 vertices of S are w's in W_1. None of them is w_j, because w_j is joined to neither u_j nor v_j. Each such w_i is joined to u_j, so u_i u_j is an edge of G, so i and j are adjacent in M; and the w's are pairwise adjacent, so their indices are pairwise adjacent in M. Hence the indices of the w's together with j form a K_{k−1} in M[W_1 ∪ {j}]. If j ∈ W_2 this contradicts the hypothesis directly. If j ∈ W_1, the K_{k−1} lies in M[W_1], hence in M[W_1 ∪ {v}] for any v ∈ W_2 (which is nonempty), again a contradiction.
- *S misses V(H) (the case "S misses V(G)" is the same with H in place of G).* Replace each w_i ∈ S by u_i. This is one to one: u_i ∉ S, because w_i and u_i are not adjacent. Adjacency is kept: w_i w_l adjacent means i l is an edge of M, so u_i u_l is an edge of G; w_i u_l adjacent (l ≠ i) means u_i u_l is an edge of G. So G would contain a clique of k vertices, a contradiction.

**No independent set of size s + t − 1.** Let I be an independent set of F. Since u_j and v_j are adjacent, at most one of them is in I. Split I into two groups.

- The *G group*: every w_i ∈ I with i ∈ W_1; every u ∈ I ∩ V(G), except those u_j whose twin w_j is in I; and, for every w_j ∈ I with j ∈ W_2, whichever of u_j, v_j lies in I (if either does).
- The *H group*: the mirror image: every w_i ∈ I with i ∈ W_2; every v ∈ I ∩ V(H), except those v_j whose twin w_j is in I; and, for every w_j ∈ I with j ∈ W_1, whichever of u_j, v_j lies in I.

Every vertex of I is in exactly one group. Map the G group into V(G): w_i ↦ u_i; a vertex u_j or v_j of the third kind ↦ u_j; a vertex u of the second kind ↦ u. The images of the three kinds are disjoint (indices in W_1 with w_i ∈ I; indices in W_2 with w_j ∈ I; vertices whose twin is not in I), so the map is one to one. The image is independent in G; we check every kind of pair. Write x(i) for the third-kind vertex attached to w_i.

1. w_i, w_l (both in W_1): they are not adjacent, and F contains all edges of M[W_1], so i l is not an edge of M; hence u_i u_l is not an edge of G.
2. w_i (i ∈ W_1) and a second-kind u: w_i and u are not adjacent, and u ≠ u_i, so u_i u is not an edge of G.
3. w_i (i ∈ W_1) and x(j) (j ∈ W_2): if x(j) = u_j, then w_i u_j not adjacent gives u_i u_j not an edge. If x(j) = v_j, then w_i v_j not adjacent gives v_i v_j not an edge of H, hence u_i u_j not an edge of G, because M is the same induced graph in G and in H.
4. Two second-kind vertices u, u': both are in I, so they are not adjacent.
5. A second-kind u and x(j): if x(j) = u_j, both are in I. If x(j) = v_j, then w_j ∈ I and u ∈ I are not adjacent, and u ≠ u_j, so u_j u is not an edge of G.
6. x(j) and x(l) (j, l ∈ W_2): w_j and w_l are both in I and not adjacent, and F contains all edges of M[W_2], so j l is not an edge of M, hence u_j u_l is not an edge of G.

So the G group has at most s − 1 vertices. By the mirror argument the H group has at most t − 1 vertices. Hence |I| ≤ s + t − 2. ∎

The independence part of the proof never uses the K_{k−1} condition; it uses only the facts that `verify_hypotheses.py` checks on the finished graph (the matching, the twins, M common and induced, all of M[W_1] and M[W_2] present among the w's) and the bounds on G and H.

## Inputs and credits

- **G384** (`G384.txt`): one colour class of R. Mathon's cubic-residue colouring for p = 127 (R. Mathon, "Lower bounds for Ramsey numbers and association schemes", J. Combin. Theory Ser. B 42 (1987) 122-127), in the form of X. Xu and S. P. Radziszowski, "An improvement to Mathon's cyclotomic Ramsey colorings", Electron. J. Combin. 16 (2009) #N1, without that paper's three extra vertices. It is a (5,17)-graph on 384 vertices with 24,766 edges. `build_g384.py` builds it from the published rule (stated in the script) and reproduces `G384.txt` byte for byte. The file is also identical to rows 0 to 383 of Jang's `r5-21/R5_21_444.txt`, which is where we first took it from; Byungkun Jang used the same G for his R(5,21) ≥ 445. The 2011 paper used a 387-vertex extension of this graph (three more vertices, from Xu and Radziszowski 2009). We could not reproduce that extension from the published description, and neither could Jang (see his README), so we use the 384-vertex graph, as he did. If a (5,17)-graph on 387 vertices containing G384 as an induced subgraph is available, the common parts given here would give R(5,20) ≥ 429 and R(5,21) ≥ 450 by the same theorem.
- **H24** (`H24.txt`, for R(5,20)): the complement of the graph on line 3521 (number 3520 counting from 0) of B. D. McKay's `r45_24.g6`, the complete list of the 352,366 Ramsey(4,5)-graphs on 24 vertices. The line itself is in `mckay_r45_24_line3521.g6`. A (5,4)-graph on 24 vertices with 154 edges.
- **H42** (`H42.txt`, for R(5,21)): the complement of the graph on line 94 (number 93 counting from 0) of McKay's `r55_42some.g6`, 328 of the 656 known Ramsey(5,5)-graphs on 42 vertices (the other 328 are their complements). The line itself is in `mckay_r55_42some_line94.g6`. A (5,5)-graph on 42 vertices with 433 edges.
- McKay's lists are at https://users.cecs.anu.edu.au/~bdm/data/ramsey.html (files fetched 23 November 2026; sha256 of `r45_24.g6` 83ca4028f206b2fa4315ef219b8c2c57c7835209673dd8183d8fb4353bd4fdd0, of `r55_42some.g6` 067902e853d87b49bcef0d1d4c0e3bbadd238ee18bc65341b079a3ca4780eccb). That page credits the (4,5,24) list to McKay and Radziszowski (1995) and McKay and Angeltveit (2016), and the (5,5,42) graphs to Exoo (1989) and McKay and Radziszowski.
- **The common parts** (`common_part_r5_20_m17.txt`, `common_part_r5_21_m20.txt`): new. One line per vertex of M in the form `u:y:side` (u a vertex of H, y a vertex of G, side 1 or 2). They were found by a local search for large common induced subgraphs that checks the full Theorem 3 condition during the search. For R(5,20) we tried 201 of McKay's 352,366 graphs (complemented); 128 reached m = 17 and none reached 18 (32 longer runs). For R(5,21) we tried all 656 (5,5,42)-graphs (the 328 of the file and their complements): m = 18 for 596, 19 for 58, 20 for 2, and none reached 21 (longer runs on the two m = 20 inputs).
- **The theorem**: Xu Xiaodong, Shao Zehui and S. P. Radziszowski (2011), as above.
- **Byungkun Jang** published R(5,21) ≥ 445 with the same G and the same theorem, using the triangle-free form with a common part of 18 vertices; his README notes that larger common parts may exist. This release improves his bound by two. Our use of the full Theorem 3 condition is what allows the larger common parts.

## Verification

`reproduce.sh` runs everything below and stops at the first failure. It needs python3, gcc and the standard tools sha256sum and cmp. Results of our run on 23 November 2026 are in `logs/`.

1. Checksums (`SHA256SUMS`).
2. `build_g384.py` rebuilds G384 from the rule: identical to `G384.txt`.
3. `build.py` decodes McKay's two g6 lines, complements them (identical to `H24.txt` and `H42.txt`), and rebuilds both graphs from G384, H and the common part: both identical byte for byte to the shipped files.
4. `verify_hypotheses.py` reads each finished graph and recovers the construction from it alone (the matching, the twins, the split), then compares with the input files. It checks: rows 0 to 383 are G384 and the next rows are H; the G-H edges form a matching of size m; each of the last m vertices is the twin of exactly one matched pair; the recovered pairs equal the common_part file; M is common and induced; the w's induce exactly M[W_1] ∪ M[W_2] with both parts nonempty; the condition of Theorem 3 word for word (for i = 1, 2 and every v ∉ W_i, M[W_i ∪ {v}] has no K4); G has no K5; H has no K5 and no independent set of size t. Both graphs pass.
5. Two independently written exact checkers, different algorithms: `check_russian_doll.c` (Östergård's Russian-doll method; usage `file T i|c`) and `check_branch_bound.c` (Tomita-style branch and bound with a colouring bound; usage `file K T`, −1 skips a side):
   - H24: no K5, no independent 4-set (both checkers). H42: no K5, no independent 5-set (both checkers).
   - `R5_20_425.txt` and `R5_21_446.txt`: no K5 (both checkers; the clique number of each is 4).
   - Controls, so that the searches are not vacuous: both graphs contain K4, the 425-vertex graph has an independent set of size 19 and the 446-vertex graph one of size 20 (found in under a second).
6. G384 has no K5 and no independent set of size 17 (both checkers: branch and bound 33 s with 5.1 × 10^7 nodes, Russian doll 2 min 47 s with 3.8 × 10^9 nodes; the Russian doll shows the independence number of G384 is exactly 16).

An independent adversarial review by a separate AI agent, with its own code (not in this repository) reached the same results on the construction, the hypotheses of Theorem 3, the clique side of both graphs and the bounds on G384, H24 and H42, and confirmed their provenance (G384 rebuilt from the published rule; H24 and H42 matched to McKay's lines).

**The independent-set side.** For both graphs this side rests on Theorem 3, with every hypothesis checked by machine as above (the same is true of Jang's R(5,21) graph). Direct exact searches add the following:

- `R5_20_425.txt`, no independent set of size 20: **passed by one exact checker**, `check_parts_bb.c` (Tomita-style branch and bound with a colouring bound, split into 8 parts over the top-level branches; the parts together cover the whole search). All 8 parts answered "no"; 1.16 × 10^10 search nodes and about 10,250 CPU seconds in total, finished 23 November 2026 20:37 UTC. The outputs are in `logs/R5_20_425_direct_independence/` (the files carry the program's working name, chkA2). Note that this program uses the same family of algorithm as `check_branch_bound.c`. A Russian-doll run on this side (output file `ramsey/verify_main/thm3/out_F425_i.txt` in our working tree) was started on 23 November 2026 at 20:44 UTC and had not finished when this was published.
- `R5_21_446.txt`, no independent set of size 21: **no direct search completed.** This side rests on the theorem alone. A Russian-doll run on this side (output file `ramsey/verify_main/thm3/out_F446_i.txt`) was started on 23 November 2026 at 20:44 UTC and had not finished when this was published.
- As a further test of the theorem at full size, the same direct search also finished on our earlier 424-vertex Theorem 3 graph for R(5,20) (same G, a different H24 from the same list, a 16-vertex common part) and found no independent set of size 20.
- Independent sets of size 19 (in the 425-vertex graph) and 20 (in the 446-vertex graph) do exist, so the searches are not vacuous, and together with the bounds above the independence numbers are exactly 19 and 20.

## Files

- `R5_20_425.txt`, `R5_21_446.txt`: the two graphs, as rows of 0/1 with no separators; row i, column j is 1 when vertices i and j are adjacent.
- `G384.txt`, `build_g384.py`: the 384-vertex (5,17)-graph and the script that builds it from the published rule.
- `H24.txt`, `H42.txt`: the two H graphs as 0/1 matrices; `mckay_r45_24_line3521.g6`, `mckay_r55_42some_line94.g6`: the McKay lines they come from (before complementing).
- `common_part_r5_20_m17.txt`, `common_part_r5_21_m20.txt`: the common parts.
- `build.py`: rebuilds H24, H42 and both graphs (standard library only).
- `verify_hypotheses.py`: checks the construction and the hypotheses of Theorem 3 (standard library only).
- `check_russian_doll.c`, `check_branch_bound.c`: the two exact checkers used by `reproduce.sh`. `check_parts_bb.c`: the exact checker used for the long direct independence search on the 425-vertex graph (usage `file r s part nparts side`, for example `./check_parts_bb R5_20_425.txt 5 20 0 8 1` for part 0 of 8 of the independence side; about 15 to 30 minutes per part).
- `reproduce.sh`, `SHA256SUMS`, `logs/` (outputs of our runs: `reproduce_quick.txt`, the G384 checks and `check_G384.sh` that produced them, and the direct independence search).

## Method

This work was directed by Peter J. Chrisbacher. The search, construction, proofs and checks were carried out with AI coding agents (Anthropic's Claude Code), under fixed rules: every claimed graph is checked by two independently written exact checkers wherever a direct exact check is feasible (here: all inputs and the clique side of both graphs; the status of the independent-set side is given under Verification), an independent adversarial review is done before any announcement, and published results are checked before anything is claimed as new.

## License

- Code (`build.py`, `build_g384.py`, `verify_hypotheses.py`, the three checkers, `reproduce.sh`, `logs/check_G384.sh`): MIT (see `LICENSE`).
- The two new graphs, the common parts, this text and the run outputs in `logs/`: CC BY 4.0 (text in `LICENSES/CC-BY-4.0.txt`); please credit Peter J. Chrisbacher and cite this repository.
- Third-party data. The two graphs contain, as induced subgraphs, G384 (Mathon's construction) and the complement of one of McKay's graphs. `mckay_*.g6` are single lines copied unchanged from B. D. McKay's public Ramsey graph lists, and `H24.txt`, `H42.txt` are their complements. **McKay's page states no licence or terms of use that we could find**, so these files are not covered by our licence; they are included as mathematical data with their source and attribution, and anyone reusing them should credit B. D. McKay (and the authors named on his page). `G384.txt` is a construction from the literature (Mathon; Xu and Radziszowski), built here by `build_g384.py`; it is not claimed as our work. Jang's repository is MIT for code and CC BY 4.0 for documentation and the graphs constructed there (his `LICENSE`); we redistribute none of his files, but `G384.txt` equals part of his graph file, which we credit above.

## How to cite

See `CITATION.cff`, or cite the Zenodo record for this repository once it is published.

## Glossary

- (k, s)-graph: a graph with no clique of size k and no independent set of size s. One on n vertices proves R(k, s) ≥ n + 1.
- Clique, K4, K5: a set of 4 or 5 vertices all joined to each other. Independent set: a set of vertices with no edges among them.
- Common part M, m: a graph that sits as an induced subgraph in both G and H, and its number of vertices.
- W_1, W_2: the two sides into which M is split.
- Twin: a new vertex w_i joined to the neighbours of the matched pair (u_i, v_i) but not to u_i or v_i.
- g6: B. D. McKay's graph6 text format, one graph per line.
- Survey items 2.3.h and 2.3.i: general lower-bound constructions in Radziszowski's survey; 2.3.h is the special case of Theorem 3 in which M has no K_{k−1}.
