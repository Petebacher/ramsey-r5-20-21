#!/bin/bash
# Independence side of G384 with both checkers (about 2 to 5 minutes in total). Run from the release folder.
set -e
cd "$(dirname "$0")/.."
S=${TMPDIR:-/tmp}/r5chk.$$; mkdir -p $S
gcc -O3 -o $S/crd check_russian_doll.c; gcc -O3 -o $S/cbb check_branch_bound.c
( time $S/crd G384.txt 17 i ) > logs/G384_russian_doll_i17.txt 2>&1
( time $S/crd G384.txt 5 c ) > logs/G384_russian_doll_c5.txt 2>&1
( time $S/cbb G384.txt 5 17 ) > logs/G384_branch_bound_5_17.txt 2>&1
rm -rf $S
