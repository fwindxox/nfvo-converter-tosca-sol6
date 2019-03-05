#!/usr/bin/env bash
root=../../..
export PYTHONPATH=$root/python/nfvo_solcon_tosca

# Run the four examples that the program shouldn't *at least* crash with
tosca=$root/solcon.py
config_dir=$root/config
output_dir=$root/outputs
config_tosca=$config_dir/config-nokia.toml
config_sol6=$config_dir/config-sol6.toml

one=../../../examples/VNFD-CMRepo-for-cisco.yaml
two=../../../examples/VNFD-CSD-for-cisco.yaml
echo Run $one...
python3 $tosca -f $one -o $output_dir/output_CMRepo.json -c $config_tosca -s $config_sol6
echo Run $two...
python3 $tosca -f $two -o $output_dir/output_CSD.json -c $config_tosca -s $config_sol6
