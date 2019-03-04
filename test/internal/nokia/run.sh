#!/usr/bin/env bash
export PYTHONPATH=../../../python/nfvo_solcon_tosca

# Run the four examples that the program shouldn't *at least* crash with
tosca=../../../solcon.py
config_dir=../../../config
config_tosca=$config_dir/config-nokia.toml
config_sol6=$config_dir/config-sol6.toml

one=../../../examples/VNFD-CMRepo-for-cisco.yaml
two=../../../examples/VNFD-CSD-for-cisco.yaml
echo Run $one...
/usr/local/bin/python3 $tosca -f $one -o ..././../outputs/output_CMRepo.json -c $config_tosca -s $config_sol6
echo Run $two...
/usr/local/bin/python3 $tosca -f $two -o ../../../outputs/output_CSD.json -c $config_tosca -s $config_sol6
