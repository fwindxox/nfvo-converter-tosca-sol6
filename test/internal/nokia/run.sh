#!/usr/bin/env bash
root=../../..
export PYTHONPATH=$root/python/nfvo_solcon_tosca

# Run all files in $example_root
tosca=$root/solcon.py
output_dir=$root/outputs/nokia
config_tosca=$root/config/config-nokia.toml
config_sol6=$root/config/config-sol6.toml
example_root=$root/examples/nokia

for filename in $example_root/*.yaml; do
    file=$(basename $filename)
    echo Run $file
    python3 $tosca -f $filename -o "$output_dir/${file%.yaml}.json" -c $config_tosca -s $config_sol6 -r nokia
done

