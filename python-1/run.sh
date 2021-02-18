#!/usr/bin/env bash

rm -f "stack_out.txt"

for n in `seq 200 200 3000`; do
    echo "Running with input n = $n"
    ./main.py $n >> "stack_out.txt"
done
