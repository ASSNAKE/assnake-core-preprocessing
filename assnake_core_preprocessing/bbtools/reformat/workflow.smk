rule bbtools_reformat_subsample:
    input:
        r1=wc_config['fastq_gz_R1_wc'],
        r2=wc_config['fastq_gz_R2_wc'],
    output:
        r1=wc_config['fastq_gz_bbtools-reformat-subsample_R1_wc'],
        r2=wc_config['fastq_gz_bbtools-reformat-subsample_R2_wc'],
    log: wc_config['fastq_gz_bbtools-reformat-subsample_log_wc']
    conda: '../../remove_human_bbmap/bbmap_env.yaml'
    shell: '''reformat.sh in={input.r1} in2={input.r2} out={output.r1} out2={output.r2} samplerate=0.01 > {log} 2>&1'''

rule bbmap_minlen:
    input:
        r1 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R2.fastq.gz',
    output:
        r1 = '{fs_prefix}/{df}/reads/{preproc}__minlen{minlen}/{df_sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}__minlen{minlen}/{df_sample}_R2.fastq.gz',
    conda: '../bbmap/bbmap_env.yaml'
    shell: ('''reformat.sh in1={input.r1} in2={input.r2} out1={output.r1} out2={output.r2} minlength={wildcards.minlen}''')
