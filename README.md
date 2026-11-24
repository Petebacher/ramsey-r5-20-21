# R(5,20) ≥ 427 and R(5,21) ≥ 447

This repository gives three graphs:

- `R5_20_426.txt` (new in version 1.1): a graph on **426 vertices** with no clique of 5 vertices and no independent set of 20 vertices. It shows that **R(5,20) ≥ 427**.
- `R5_20_425.txt` (version 1.0, kept as history): a graph on **425 vertices** with the same two properties. It showed that R(5,20) ≥ 426 and is superseded by the 426-vertex graph.
- `R5_21_446.txt`: a graph on **446 vertices** with no clique of 5 vertices and no independent set of 21 vertices. It shows that **R(5,21) ≥ 447**.

The file names give the number of vertices; the bound is one more.

All three graphs are built with Theorem 3 of Xu, Shao and Radziszowski (2011), from published ingredients: a 384-vertex graph of Mathon's cyclotomic type and a graph from B. D. McKay's lists. What is new is the common induced subgraph that glues them together, which is larger than those used before for these two numbers (18 vertices against 12 for R(5,20), 20 against 18 for R(5,21)). The absence of a 5-clique was checked directly on all three finished graphs by two independently written exact programs. The absence of the large independent set rests on Theorem 3, whose hypotheses were all checked by machine. In addition, direct exact searches on that side have finished for all three graphs and found no forbidden independent set: two different programs for each R(5,20) graph, one program for the 446-vertex graph (details below).

**The 426-vertex graph depends on the full condition of Theorem 3.** Its common part has 18 vertices and contains 18 copies of K4, every one with exactly two vertices in each of the two parts. Neither survey item 2.3.h nor the simpler triangle-free form of the theorem applies to it (see "The theorem").

## Previous bounds

| | survey (DS1 rev. 18, Table IIa) | best public bound we could find as of 24 November 2026 before this work | this work |
|---|---|---|---|
| R(5,20) | ≥ 424, reference [XSR2] (Xu, Shao and Radziszowski 2011, a 423-vertex Theorem 3 graph built from a 387-vertex G, a 24-vertex H and a 12-vertex common part) | ≥ 426: our own version 1.0 of this repository (23 November 2026, 425-vertex graph); before that, the survey value 424 | ≥ 427 |
| R(5,21) | ≥ 441, by survey item 2.3.i | ≥ 445: Byungkun Jang, 11 November 2026, github.com/8rulerstar/ramsey-lower-bounds, folder `r5-21` (Zenodo concept DOI 10.5281/zenodo.24128875), a 444-vertex Theorem 3 graph with G = the same 384-vertex graph used here, H = graph number 2 of McKay's `r55_42some.g6`, common part 18 | ≥ 447 |

Survey: S. P. Radziszowski, *Small Ramsey Numbers*, Electronic Journal of Combinatorics, Dynamic Survey DS1, revision 18 (24 April 2026), https://doi.org/10.37236/21.

What we searched on 23 November 2026 (UTC): the survey (local copy of revision 18); Jang's repository (re-read at 20:39: newest commit 23 November 01:02, about R(8,12); the `r5-21` folder unchanged since 11 November; his README still lists R(5,21) ≥ 445 and has no R(5,20) entry); GitHub repositories about Ramsey numbers (pushed since 1 October, read at about 19:25; those pushed since 19:00, re-read at 20:39); the Leaps in Bounds tracker (no row for R(5,20) or R(5,21)); Google Research's `ramsey_number_bounds/improved_bounds` folder (no R(5,·) file); the Quantavane records (none for these cells); the 60 newest arXiv papers on Ramsey lower bounds (to 18 November); the 25 newest Zenodo records about Ramsey numbers (about 19:00); and general web searches. An independent re-check between 20:47 and 20:50 UTC found Jang's repository unchanged, searched Zenodo with five queries ("Ramsey number", "Ramsey numbers", "R(5,20)", "R(5,21)", and Jang as creator; his newest record is version 1.7 of 20 November, on other work), and repeated the GitHub and web searches. Apart from our own version 1.0, we found no bound above 424 for R(5,20) or above 445 for R(5,21). On 24 November 2026 at about 01:17 UTC an independent re-check of Jang's repository, the Leaps in Bounds tracker, the Quantavane records, Google's folder, GitHub repositories about Ramsey numbers pushed since 19:00 UTC on 23 November, and the eight newest arXiv papers on Ramsey lower bounds again found nothing at or above 427 for R(5,20) or above 447 for R(5,21) (that check did not repeat the web and Zenodo searches). We cannot see private communications, mailing lists or social media.

Published formulas do not reach these values. Survey item 2.3.i gives R(5,l) ≥ 4 R(3,l−1) − 3, which is 4 × 106 − 3 = 421 for l = 20 and 4 × 111 − 3 = 441 for l = 21 with today's R(3,19) ≥ 106 and R(3,20) ≥ 111. (If someone shows R(3,20) ≥ 113, that formula would give R(5,21) ≥ 449; for R(5,20) it would need R(3,19) ≥ 108 to pass 427.) Corollary 3 of [XSR2], R(k, s+t−1) ≥ R(k,s) + R(k,t) + k − 2, gives at most 419 and 435.

Earlier on 23 November we had found common parts of 16 and 19 vertices (graphs on 424 and 445 vertices). Those were intermediate steps of the same search and are not separate results. The 425-vertex graph of version 1.0 (common part of 17 vertices) stays in this release as history.

## The theorem

X. Xu, Z. Shao and S. P. Radziszowski, "More constructive lower bounds on classical Ramsey numbers", SIAM Journal on Discrete Mathematics 25 (2011) 394-400, Theorem 3. Quoted from the authors' preprint of that paper (dated 14 September 2010). The paper writes the vertex set of M as "VM" (and V G, E F for G and F); we write V_M, and index subscripts such as W_1 and K_{k−1} with underscores:

> **Theorem 3** Let k ≥ 4 and s, t ≥ 2. Given a (k, s)-graph G and a (k, t)-graph H, let M be a graph isomorphic to induced subgraphs of G and H. If the vertex set V_M can be partitioned into two nonempty sets, V_M = W_1 ∪ W_2, so that for every v ∈ V_M − W_i and i ∈ {1, 2} there is no K_{k−1} in M[W_i ∪ {v}], then
>
> R(k, s + t − 1) ≥ n(G) + n(H) + n(M) + 1.

A (k, s)-graph is a graph with no clique of size k and no independent set of size s.

**This is the full condition, not the triangle-free shorthand.** For k = 5 the condition says: every K4 of M has exactly two vertices in W_1 and two in W_2 (a K4 with three or four vertices on one side is excluded, and so is a K4 inside one side, because the other side is nonempty). A simpler sufficient form, used by Jang and stated after the theorem in the paper, asks that neither part contain a K_{k−2}, which for k = 5 means both parts are triangle-free. **Our parts contain triangles,** so that simpler form does not apply, and a checker that asserts it (such as the one in Jang's `build.py`) will reject our common parts. The full condition holds:

| | R(5,20), 426-vertex graph (v1.1) | R(5,20), 425-vertex graph (v1.0) | R(5,21), 446-vertex graph |
|---|---|---|---|
| k, s, t | 5, 17, 4 | 5, 17, 4 | 5, 17, 5 |
| n(G) + n(H) + n(M) | 384 + 24 + 18 = 426 | 384 + 24 + 17 = 425 | 384 + 42 + 20 = 446 |
| \|W_1\|, \|W_2\| | 10, 8 | 6, 11 | 9, 11 |
| copies of K4 in M | 18, every one split 2 and 2 | 0 | 18, every one split 2 and 2 |
| triangles inside W_1, W_2 | 6, 2 | 0, 17 | 1, 10 |
| edges of M | 79 | 68 | 79 |

In words, for the 426-vertex graph: M has 18 vertices, 79 edges, clique number 4 and independence number 3, and 18 copies of K4. Each of the 18 K4s has exactly 2 vertices in each part. The split is 10 + 8, and the parts contain 6 and 2 triangles. `verify_hypotheses.py` checks this both in the "2 and 2" form and in the theorem's literal wording (for each part and each vertex outside it, no K4 in the part plus that vertex).

**R(5,20), 426-vertex graph: survey item 2.3.h does not apply.** Item 2.3.h ("a common induced subgraph on m vertices without K_{k−1}", Radziszowski DS1 rev. 18, page 12) needs a K4-free common part. Here the common part would need 18 vertices, no K4 and no independent set of size 4, and that cannot exist because R(4,4) = 18. So this graph rests on the full condition of Theorem 3 and on nothing weaker.

**R(5,20), 425-vertex graph (history): the common part is the Paley graph on 17 vertices.** It has no K4 and, as an induced subgraph of H, no independent set of size 4; the only such graph on 17 vertices is Paley(17), and `verify_hypotheses.py` confirms the K4 count (we also checked the isomorphism directly). For that graph, and only for that graph, the plain survey item 2.3.h already applies, with p = 4 and q = 17. Since R(4,4) = 18, 17 is the largest common part without K4 that is possible; a larger one has to contain K4s, all split 2 and 2, and the 426-vertex graph is exactly that case.

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

**The 426-vertex graph (k = 5).** Here the hypothesis is used as follows. Take a part W_i and a vertex v of the other part. A K4 inside M[W_i ∪ {v}] would have at least 3 vertices in W_i, because only v lies outside W_i. But every K4 of M has exactly 2 vertices in each part, so none exists; and a K4 inside W_i alone is excluded for the same reason. This is the condition of the theorem, and the K_k part of the proof above then applies unchanged.

The independence part of the proof never uses the K_{k−1} condition; it uses only the facts that `verify_hypotheses.py` checks on the finished graph (the matching, the twins, M common and induced, all of M[W_1] and M[W_2] present among the w's) and the bounds on G and H.

## Inputs and credits

- **G384** (`G384.txt`): one colour class of R. Mathon's cubic-residue colouring for p = 127 (R. Mathon, "Lower bounds for Ramsey numbers and association schemes", J. Combin. Theory Ser. B 42 (1987) 122-127), in the form of X. Xu and S. P. Radziszowski, "An improvement to Mathon's cyclotomic Ramsey colorings", Electron. J. Combin. 16 (2009) #N1, without that paper's three extra vertices. It is a (5,17)-graph on 384 vertices with 24,766 edges. `build_g384.py` builds it from the published rule (stated in the script) and reproduces `G384.txt` byte for byte. The file is also identical to rows 0 to 383 of Jang's `r5-21/R5_21_444.txt`, which is where we first took it from; Byungkun Jang used the same G for his R(5,21) ≥ 445. The 2011 paper used a 387-vertex extension of this graph (three more vertices, from Xu and Radziszowski 2009). We could not reproduce that extension from the published description, and neither could Jang (see his README), so we use the 384-vertex graph, as he did. If a (5,17)-graph on 387 vertices containing G384 as an induced subgraph is available, the common parts given here would give R(5,20) ≥ 430 and R(5,21) ≥ 450 by the same theorem.
- **H24** (`H24.txt`, for R(5,20)): the complement of the graph on line 3521 (number 3520 counting from 0) of B. D. McKay's `r45_24.g6`, the complete list of the 352,366 Ramsey(4,5)-graphs on 24 vertices. The line itself is in `mckay_r45_24_line3521.g6`. A (5,4)-graph on 24 vertices with 154 edges.
- **H24 for the 426-vertex graph** (`H24_line119677.txt`): the complement of the graph on line 119677 (number 119676 counting from 0) of the same `r45_24.g6`. The line itself is in `mckay_r45_24_line119677.g6`. A (5,4)-graph on 24 vertices with 153 edges. It is a different graph from the H24 above (line 3521).
- **H42** (`H42.txt`, for R(5,21)): the complement of the graph on line 94 (number 93 counting from 0) of McKay's `r55_42some.g6`, 328 of the 656 known Ramsey(5,5)-graphs on 42 vertices (the other 328 are their complements). The line itself is in `mckay_r55_42some_line94.g6`. A (5,5)-graph on 42 vertices with 433 edges.
- McKay's lists are at https://users.cecs.anu.edu.au/~bdm/data/ramsey.html (files fetched 23 November 2026; sha256 of `r45_24.g6` 83ca4028f206b2fa4315ef219b8c2c57c7835209673dd8183d8fb4353bd4fdd0, of `r55_42some.g6` 067902e853d87b49bcef0d1d4c0e3bbadd238ee18bc65341b079a3ca4780eccb). That page credits the (4,5,24) list to McKay and Radziszowski (1995) and McKay and Angeltveit (2016), and the (5,5,42) graphs to Exoo (1989) and McKay and Radziszowski.
- **The common parts** (`common_part_r5_20_m17.txt`, `common_part_r5_20_m18.txt`, `common_part_r5_21_m20.txt`): new. One line per vertex of M in the form `u:y:side` (u a vertex of H, y a vertex of G, side 1 or 2). They were found by a local search for large common induced subgraphs that checks the full Theorem 3 condition during the search. For R(5,20) we tried 201 of McKay's 352,366 graphs (complemented); 128 reached m = 17 and none reached 18 (32 longer runs). For R(5,21) we tried all 656 (5,5,42)-graphs (the 328 of the file and their complements): m = 18 for 596, 19 for 58, 20 for 2, and none reached 21 (longer runs on the two m = 20 inputs).

  **The R(5,20) sweep that found m = 18.** On the night of 23 to 24 November 2026 we ran the same kind of search (20 seconds per input) on a random sample of 8,000 of McKay's 352,366 (4,5;24)-graphs (sampling seed 20261123), complemented, plus one control input that was known to reach 17. All 8,001 runs finished. The best common part found per input: 15 vertices for 688 inputs, 16 for 2,314, 17 for 4,988, 18 for 11, and 19 or more for none. So 18 is rare (11 of 8,001) and 19 was not reached. The first input to reach 18 is number 2785 of the sample counting from 0 (the name `t002785c`), which is line 119677 of `r45_24.g6` counting from 1; the 426-vertex graph comes from it. These counts come from our run records; the search program and the sample list are not part of this repository.
- **The theorem**: Xu Xiaodong, Shao Zehui and S. P. Radziszowski (2011), as above.
- **Byungkun Jang** published R(5,21) ≥ 445 with the same G and the same theorem, using the triangle-free form with a common part of 18 vertices; his README notes that larger common parts may exist. This release improves his bound by two. Our use of the full Theorem 3 condition is what allows the larger common parts.

## Verification

`reproduce.sh` runs everything below and stops at the first failure. It needs python3, gcc and the standard tools sha256sum and cmp. Results of our runs are in `logs/` (the quick run was repeated on 24 November 2026).

1. Checksums (`SHA256SUMS`).
2. `build_g384.py` rebuilds G384 from the rule: identical to `G384.txt`.
3. `build.py` decodes McKay's three g6 lines, complements them (identical to `H24.txt`, `H24_line119677.txt` and `H42.txt`), and rebuilds all three graphs from G384, H and the common part: all identical byte for byte to the shipped files (for `R5_20_426.txt`, sha256 0a6ee98fd69cbd5b5ad1339d57abc51abf782a5e611bb6a9f970e4cf50a48d72).
4. `verify_hypotheses.py` reads each finished graph and recovers the construction from it alone (the matching, the twins, the split), then compares with the input files. It checks: rows 0 to 383 are G384 and the next rows are H; the G-H edges form a matching of size m; each of the last m vertices is the twin of exactly one matched pair; the recovered pairs equal the common_part file; M is common and induced; the w's induce exactly M[W_1] ∪ M[W_2] with both parts nonempty; the condition of Theorem 3 word for word (for i = 1, 2 and every v ∉ W_i, M[W_i ∪ {v}] has no K4); G has no K5; H has no K5 and no independent set of size t. For k = 5 it also checks the "2 and 2" form: every K4 of M has exactly two vertices in each part. All three graphs pass.
5. Two independently written exact checkers, different algorithms: `check_russian_doll.c` (Östergård's Russian-doll method; usage `file T i|c`) and `check_branch_bound.c` (Tomita-style branch and bound with a colouring bound; usage `file K T`, −1 skips a side):
   - H24 and the H24 of line 119677: no K5, no independent 4-set (both checkers). H42: no K5, no independent 5-set (both checkers).
   - `R5_20_425.txt`, `R5_20_426.txt` and `R5_21_446.txt`: no K5 (both checkers; the clique number of each is 4). For the 426-vertex graph the Russian-doll run takes 0.1 s (1.18 × 10^6 nodes) and branch and bound 1.4 × 10^5 nodes; the output is also saved alone in `logs/R5_20_426_clique_side.txt`.
   - Controls, so that the searches are not vacuous: all three graphs contain K4, the 425- and 426-vertex graphs each have an independent set of size 19 and the 446-vertex graph one of size 20 (found in under a second).
6. G384 has no K5 and no independent set of size 17 (both checkers: branch and bound 33 s with 5.1 × 10^7 nodes, Russian doll 2 min 47 s with 3.8 × 10^9 nodes; the Russian doll shows the independence number of G384 is exactly 16).

An independent adversarial review by a separate AI agent, with its own code (not in this repository) reached the same results on the construction, the hypotheses of Theorem 3, the clique side of the graphs and the bounds on G384, H24 and H42, and confirmed their provenance (G384 rebuilt from the published rule; H24 and H42 matched to McKay's lines). The same reviewer repeated this for the 426-vertex graph (including its own exact search for a K5 and its own check of the Theorem 3 condition in both forms) with the same results, and found the H block to be exactly the complement of line 119677 of `r45_24.g6`.

**The independent-set side.** For all three graphs this side rests on Theorem 3, with every hypothesis checked by machine as above (the same is true of Jang's R(5,21) graph). Direct exact searches add the following. All of them found no forbidden independent set; the logs are in `logs/` and were produced in our working tree (the working names of the files are `out_F425_i.txt` and so on). The three Russian-doll logs were written by the working copy of the program, which differs from the shipped check_russian_doll.c only in its header comment, its usage text and one print statement: it printed "K4 count: 0" even though the K4 count is skipped for graphs with more than 300 vertices. Ignore that line; all three graphs contain K4s (see the controls above). The shipped program prints "K4 count: skipped (n > 300)".

- `R5_20_426.txt`, no independent set of size 20 (the new graph). Two searches finished:
  - Russian doll (`check_russian_doll.c`, mode `i`, target 20): independence number 19, no independent 20-set; 1.30 × 10^11 nodes (130,023,218,480), 4,434 CPU seconds; finished 24 November 2026 about 02:32 UTC. Log: `logs/out_F426_i.txt`.
  - `check_parts_bb.c` (branch and bound with a colouring bound, 8 parts that together cover the whole search, independence side): all 8 parts answered "no"; 1.18 × 10^10 nodes (11,823,446,531) and 10,252 CPU seconds in total; the last part finished 24 November 2026 about 01:52 UTC. Logs: `logs/R5_20_426_direct_independence/` (the files carry the program's working name, chkA2; "side1" is the independence side).
  Two different algorithms agree. Together with the control (a 19-set exists) the independence number is exactly 19.
- `R5_20_425.txt`, no independent set of size 20 (history). Two searches finished: `check_parts_bb.c` in 8 parts, all "no", 1.16 × 10^10 nodes and about 10,250 CPU seconds, finished 23 November 2026 20:37 UTC, logs in `logs/R5_20_425_direct_independence/`; and Russian doll, independence number 19, 1.14 × 10^11 nodes (113,518,779,089), 3,746 CPU seconds, log `logs/out_F425_i.txt` (written by 24 November 2026 about 00:12 UTC). In version 1.0 this Russian-doll run had not finished.
- `R5_21_446.txt`, no independent set of size 21: **one direct search finished**, Russian doll, independence number 20, no independent 21-set; 4.20 × 10^11 nodes (419,893,453,917), 10,775 CPU seconds; log `logs/out_F446_i.txt` (written by 24 November 2026 about 00:12 UTC). In version 1.0 this run had not finished. No second program has searched this side, so for this graph the direct check rests on one program.
- As a further test of the theorem at full size, the same direct search also finished on our earlier 424-vertex Theorem 3 graph for R(5,20) (same G, a different H24 from the same list, a 16-vertex common part) and found no independent set of size 20.
- Independent sets of size 19 (in the 425- and 426-vertex graphs) and 20 (in the 446-vertex graph) do exist, so the searches are not vacuous, and the independence numbers are exactly 19, 19 and 20.

## Files

- `R5_20_426.txt`, `R5_20_425.txt`, `R5_21_446.txt`: the three graphs (the 425-vertex graph is the one of version 1.0), as rows of 0/1 with no separators; row i, column j is 1 when vertices i and j are adjacent.
- `G384.txt`, `build_g384.py`: the 384-vertex (5,17)-graph and the script that builds it from the published rule.
- `H24.txt`, `H24_line119677.txt`, `H42.txt`: the three H graphs as 0/1 matrices; `mckay_r45_24_line3521.g6`, `mckay_r45_24_line119677.g6`, `mckay_r55_42some_line94.g6`: the McKay lines they come from (before complementing).
- `common_part_r5_20_m17.txt`, `common_part_r5_20_m18.txt`, `common_part_r5_21_m20.txt`: the common parts.
- `build.py`: rebuilds the three H graphs and the three graphs (standard library only).
- `verify_hypotheses.py`: checks the construction and the hypotheses of Theorem 3 (standard library only).
- `check_russian_doll.c`, `check_branch_bound.c`: the two exact checkers used by `reproduce.sh`. `check_parts_bb.c`: the exact checker used for the long direct independence searches on the 425- and 426-vertex graphs (usage `file r s part nparts side`, for example `./check_parts_bb R5_20_426.txt 5 20 0 8 1` for part 0 of 8 of the independence side; about 10 to 35 minutes per part).
- `reproduce.sh`, `SHA256SUMS`, `logs/` (outputs of our runs: `reproduce_quick.txt`, the G384 checks and `check_G384.sh` that produced them, the clique side of the 426-vertex graph, and the direct independence searches).

## Method

This work was directed by Peter J. Chrisbacher. The search, construction, proofs and checks were carried out with AI coding agents (Anthropic's Claude Code), under fixed rules: every claimed graph is checked by two independently written exact checkers wherever a direct exact check is feasible (here: all inputs, the clique side of all three graphs, and the independent-set side of all three graphs for at least one exact program; see Verification), an independent adversarial review is done before any announcement, and published results are checked before anything is claimed as new.

## License

- Code (`build.py`, `build_g384.py`, `verify_hypotheses.py`, the three checkers, `reproduce.sh`, `logs/check_G384.sh`): MIT (see `LICENSE`).
- The new graphs, the common parts, this text and the run outputs in `logs/`: CC BY 4.0 (text in `LICENSES/CC-BY-4.0.txt`); please credit Peter J. Chrisbacher and cite this repository.
- Third-party data. The graphs contain, as induced subgraphs, G384 (Mathon's construction) and the complement of one of McKay's graphs. `mckay_*.g6` are single lines copied unchanged from B. D. McKay's public Ramsey graph lists, and `H24.txt`, `H24_line119677.txt`, `H42.txt` are their complements. **McKay's page states no licence or terms of use that we could find**, so these files are not covered by our licence; they are included as mathematical data with their source and attribution, and anyone reusing them should credit B. D. McKay (and the authors named on his page). `G384.txt` is a construction from the literature (Mathon; Xu and Radziszowski), built here by `build_g384.py`; it is not claimed as our work. Jang's repository is MIT for code and CC BY 4.0 for documentation and the graphs constructed there (his `LICENSE`); we redistribute none of his files, but `G384.txt` equals part of his graph file, which we credit above.

## How to cite

See `CITATION.cff`, or cite the Zenodo record for this repository (each version has its own DOI; cite the one for the version you used, 1.1 for R(5,20) ≥ 427).

## Glossary

- (k, s)-graph: a graph with no clique of size k and no independent set of size s. One on n vertices proves R(k, s) ≥ n + 1.
- Clique, K4, K5: a set of 4 or 5 vertices all joined to each other. Independent set: a set of vertices with no edges among them.
- Common part M, m: a graph that sits as an induced subgraph in both G and H, and its number of vertices.
- W_1, W_2: the two sides into which M is split.
- Twin: a new vertex w_i joined to the neighbours of the matched pair (u_i, v_i) but not to u_i or v_i.
- g6: B. D. McKay's graph6 text format, one graph per line.
- Survey items 2.3.h and 2.3.i: general lower-bound constructions in Radziszowski's survey; 2.3.h is the special case of Theorem 3 in which M has no K_{k−1}.

## Changelog

- **v1.1 (24 November 2026).** R(5,20) ≥ 427 from a new graph on 426 vertices (`R5_20_426.txt`): Theorem 3 with G384, the complement of line 119677 of McKay's `r45_24.g6`, and a common part of 18 vertices (18 copies of K4, each split 2 and 2 between the parts of 10 and 8 vertices). New files: `R5_20_426.txt`, `H24_line119677.txt`, `mckay_r45_24_line119677.g6`, `common_part_r5_20_m18.txt`, and the logs of the direct independence searches (Russian doll on all three graphs, the 8-part search on the 426-vertex graph, the clique side of the 426-vertex graph). `build.py`, `verify_hypotheses.py` (now also checks the 2 and 2 split of every K4) and `reproduce.sh` cover the new graph. README corrected: item 2.3.h applies only to the 425-vertex graph, and the sweep counts are given. R(5,21) ≥ 447 is unchanged; its 446-vertex graph now also has one finished direct independence search. The 425-vertex graph stays as history.
- **v1.0 (23 November 2026).** R(5,20) ≥ 426 (425-vertex graph) and R(5,21) ≥ 447 (446-vertex graph).
