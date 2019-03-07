#!/usr/bin/env bash
root=../../..
output_dir=$root/outputs/nokia

for filename in $output_dir/*.json; do
    scp $filename $anu_vm:~/aaron/nokia
done
