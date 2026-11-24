#!/bin/bash
# Rebuild the three graphs from their inputs and check every hypothesis of Theorem 3 (Xu, Shao, Radziszowski 2011),
# plus the clique side of all three graphs, with two independently written exact checkers.
# Needs: python3 (standard library only), gcc. Stops at the first failure.
# Time: everything except step 6 takes a few seconds. Step 6 (G384 has no independent 17-set, both checkers)
# takes a few minutes on one core; run "QUICK=1 ./reproduce.sh" to skip it.
set -euo pipefail
cd "$(dirname "$0")"
OUT=rebuilt
rm -rf "$OUT"; mkdir -p "$OUT"

echo "== 1. checksums"
sha256sum -c SHA256SUMS

echo "== 2. G384 from the published rule (Mathon; Xu and Radziszowski 2009)"
python3 build_g384.py "$OUT/G384.txt"
cmp "$OUT/G384.txt" G384.txt
echo "G384.txt is identical to the graph built from the rule"

echo "== 3. H24, H24_line119677, H42 from McKay's g6 lines, and the three graphs from G384 + H + common part"
python3 build.py "$OUT"
for f in H24.txt H24_line119677.txt H42.txt R5_20_425.txt R5_20_426.txt R5_21_446.txt; do
  cmp "$OUT/$f" "$f"; echo "$f is identical to the rebuilt file"
done

echo "== 4. Theorem 3 structure and hypotheses (recovered from each finished graph; the 426-vertex graph with the 2 + 2 split of every K4)"
python3 verify_hypotheses.py R5_20_425.txt G384.txt H24.txt common_part_r5_20_m17.txt 5 17 4 | tee "$OUT/hyp_r5_20.txt"
grep -q "^HYPOTHESES OK" "$OUT/hyp_r5_20.txt"
python3 verify_hypotheses.py R5_20_426.txt G384.txt H24_line119677.txt common_part_r5_20_m18.txt 5 17 4 | tee "$OUT/hyp_r5_20_426.txt"
grep -q "^HYPOTHESES OK" "$OUT/hyp_r5_20_426.txt"
grep -q "each of the 18 K4 of M has exactly 2 vertices in W1 and 2 in W2" "$OUT/hyp_r5_20_426.txt"
python3 verify_hypotheses.py R5_21_446.txt G384.txt H42.txt common_part_r5_21_m20.txt 5 17 5 | tee "$OUT/hyp_r5_21.txt"
grep -q "^HYPOTHESES OK" "$OUT/hyp_r5_21.txt"

echo "== 5. exact checks with two checkers: H graphs (both sides) and the finished graphs (no K5)"
gcc -O3 -o "$OUT/check_russian_doll" check_russian_doll.c
gcc -O3 -o "$OUT/check_branch_bound" check_branch_bound.c
RD="$OUT/check_russian_doll"; BB="$OUT/check_branch_bound"
run() { echo "\$ $*"; "$@" | tee "$OUT/last.txt"; }
# Russian doll prints "independent set of size T exists: no"; in mode c it searches the complement (cliques).
run $RD H24.txt 5 c; grep -q "exists: no" "$OUT/last.txt"
run $RD H24.txt 4 i; grep -q "exists: no" "$OUT/last.txt"
run $BB H24.txt 5 4; grep -q "^PASS" "$OUT/last.txt"
run $RD H42.txt 5 c; grep -q "exists: no" "$OUT/last.txt"
run $RD H42.txt 5 i; grep -q "exists: no" "$OUT/last.txt"
run $BB H42.txt 5 5; grep -q "^PASS" "$OUT/last.txt"
run $RD H24_line119677.txt 5 c; grep -q "exists: no" "$OUT/last.txt"
run $RD H24_line119677.txt 4 i; grep -q "exists: no" "$OUT/last.txt"
run $BB H24_line119677.txt 5 4; grep -q "^PASS" "$OUT/last.txt"
for f in R5_20_425.txt R5_20_426.txt R5_21_446.txt; do
  run $RD $f 5 c; grep -q "exists: no" "$OUT/last.txt"
  run $BB $f 5 -1; grep -q "^PASS" "$OUT/last.txt"
done
echo "-- controls (the searches are not vacuous): K4 present in both graphs; independent sets one below the limit exist"
echo "   (the checker's own FAIL line below is expected: each control looks for something that exists)"
run $BB R5_20_425.txt 4 -1; grep -q "K_4 present: YES" "$OUT/last.txt"
run $BB R5_20_426.txt 4 -1; grep -q "K_4 present: YES" "$OUT/last.txt"
run $BB R5_21_446.txt 4 -1; grep -q "K_4 present: YES" "$OUT/last.txt"
run $BB R5_20_425.txt -1 19; grep -q "independent 19 present: YES" "$OUT/last.txt"
run $BB R5_20_426.txt -1 19; grep -q "independent 19 present: YES" "$OUT/last.txt"
run $BB R5_21_446.txt -1 20; grep -q "independent 20 present: YES" "$OUT/last.txt"

if [ "${QUICK:-0}" = "1" ]; then
  echo "QUICK=1: skipped step 6 (G384 has no independent 17-set)"
  echo "ALL QUICK CHECKS PASSED"
  exit 0
fi
echo "== 6. G384 is a (5,17)-graph: no K5, no independent 17-set (both checkers; a few minutes)"
run $RD G384.txt 5 c; grep -q "exists: no" "$OUT/last.txt"
run $RD G384.txt 17 i; grep -q "exists: no" "$OUT/last.txt"
run $BB G384.txt 5 17; grep -q "^PASS" "$OUT/last.txt"
echo "ALL CHECKS PASSED"
echo "(The independent-set side of the three graphs follows from Theorem 3; direct searches that also finished are in logs/ and listed in README.md.)"
