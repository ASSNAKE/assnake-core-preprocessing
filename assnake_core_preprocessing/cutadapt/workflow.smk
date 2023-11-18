

rule cutadapt:
    input:
        r1=wc_config['fastq_gz_R1_wc'],
        r2=wc_config['fastq_gz_R2_wc'],
        params=os.path.join(config['assnake_db'], "presets/cutadapt/{preset}.txt")
    output:
        r1='{fs_prefix}/{df}/reads/{preproc}__cutadapt_{preset}/{df_sample}_R1.fastq.gz',
        r2='{fs_prefix}/{df}/reads/{preproc}__cutadapt_{preset}/{df_sample}_R2.fastq.gz',
        info='{fs_prefix}/{df}/reads/{preproc}__cutadapt_{preset}/{df_sample}.info'
    log: "{fs_prefix}/{df}/reads/{preproc}__cutadapt_{preset}/{df_sample}.log"
    threads: 8
    wildcard_constraints:    
        params="[\w\d_-]+",
    conda: 'env.yaml'
    wrapper:  "file://"+os.path.join(config['assnake-core-preprocessing']['install_dir'], 'cutadapt/wrapper.py')