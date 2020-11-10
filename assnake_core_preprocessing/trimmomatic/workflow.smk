from assnake.core.dataset import Dataset
import os

def inputs(wildcards):
    if Dataset(wildcards.df).dataset_type == 'paired-end':
        return [
                wc_config['fastq_gz_R1_wc'],
                wc_config['fastq_gz_R2_wc'],
                os.path.join(config['assnake_db'], "presets/trimmomatic/{preset}.json"),
                ]
    else:
        return [
                wc_config['fastq_gz_R1_wc'],
                os.path.join(config['assnake_db'], "presets/trimmomatic/{preset}.json"),
                ]

rule tmtic:
    input: inputs
    output: 
        r1=wc_config['fastq_gz_tmtic_R1_wc']
    params: 
        r2=wc_config['fastq_gz_tmtic_R2_wc'],
        u =wc_config['fastq_gz_tmtic_S_wc'],
        u1=wc_config['fastq_gz_tmtic_unpaired1_wc'],
        u2=wc_config['fastq_gz_tmtic_unpaired2_wc'],
        dataset_type=lambda wildcards: Dataset(wildcards.df).dataset_type
        
    log: "{fs_prefix}/{df}/reads/{preproc}__tmtic_{preset}/{df_sample}.log"
    threads: 8#config['assnake-core-preprocessing']['results']['trimmomatic']['threads']
    wildcard_constraints:    
        params="[\w\d_-]+",
    conda: 'env_0.38.yaml'
    wrapper: "file://"+os.path.join(config['assnake-core-preprocessing']['install_dir'], 'trimmomatic/wrapper.py')

