#!/usr/bin/env bash
cd $(dirname $0)
root=../../..
export PYTHONPATH=$root/src

# Run all files in $example_root
tosca=$root/solcon.py
output_dir=$root/outputs/cbam
config_tosca=$root/config/config-cbam.toml
example_root=$root/examples/cbam

for filename in $example_root/*.yaml; do
    file=$(basename $filename)
    echo Run $file
    python3 $tosca -f $filename -o "$output_dir/${file%.yaml}.json" -c $config_tosca -r nokia
done

