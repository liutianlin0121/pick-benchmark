import os
import subprocess

os.environ["BENCHMARK_DEFAULT_WORKERS"] = "8"

# Define the directory where your config files are located
config_directory = '/home/liu0003/Desktop/projects/pick-benchmark/configs/'

# List all the config files in the directory
config_files = [
    'ethz_basicphaseae.json', 'ethz_cred.json', 'ethz_dppdetect.json', 'ethz_dpppickerp.json', 
    'ethz_dpppickers.json', 'ethz_eqtransformer.json', 'ethz_gpd.json', 'ethz_gpdpick.json', 
    'ethz_phasenet.json', 'geofon_basicphaseae.json', 'geofon_cred.json', 'geofon_dppdetect.json', 
    'geofon_dpppickerp.json', 'geofon_dpppickers.json', 'geofon_eqtransformer.json', 'geofon_gpd.json', 
    'geofon_gpdpick.json', 'geofon_phasenet.json', 'instance_basicphaseae.json', 'instance_cred.json', 
    'instance_dppdetect.json', 'instance_dpppickerp.json', 'instance_dpppickers.json', 
    'instance_eqtransformer.json', 'instance_gpd.json', 'instance_gpdpick.json', 'instance_phasenet.json', 
    'iquique_basicphaseae.json', 'iquique_cred.json', 'iquique_dppdetect.json', 'iquique_dpppickerp.json', 
    'iquique_dpppickers.json', 'iquique_eqtransformer.json', 'iquique_gpd.json', 'iquique_gpdpick.json', 
    'iquique_phasenet.json', 'lendb_basicphaseae.json', 'lendb_cred.json', 'lendb_dppdetect.json', 
    'lendb_dpppickerp.json', 'lendb_dpppickers.json', 'lendb_eqtransformer.json', 'lendb_gpd.json', 
    'lendb_gpdpick.json', 'lendb_phasenet.json', 'neic_basicphaseae.json', 'neic_cred.json', 
    'neic_dppdetect.json', 'neic_dpppickerp.json', 'neic_dpppickers.json', 'neic_eqtransformer.json', 
    'neic_gpd.json', 'neic_gpdpick.json', 'neic_phasenet.json', 'ross2018gpd_gpd.json', 
    'scedc_basicphaseae.json', 'scedc_cred.json', 'scedc_dppdetect.json', 'scedc_dpppickerp.json', 
    'scedc_dpppickers.json', 'scedc_eqtransformer.json', 'scedc_gpd.json', 'scedc_gpdpick.json', 
    'scedc_phasenet.json', 'stead_basicphaseae.json', 'stead_cred.json', 'stead_dppdetect.json', 
    'stead_dpppickerp.json', 'stead_dpppickers.json', 'stead_eqtransformer.json', 'stead_gpd.json', 
    'stead_gpdpick.json', 'stead_phasenet.json'
]

# Loop through each config file and run the training script
for config_file in config_files:
    config_path = os.path.join(config_directory, config_file)
    command = f"python train.py --config '{config_path}'"
    print(f"Running: {command}")
    subprocess.run(command, shell=True)
