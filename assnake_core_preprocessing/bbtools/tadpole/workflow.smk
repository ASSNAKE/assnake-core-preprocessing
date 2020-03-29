rule bbtools_tadpole:
    input:
        r1=wc_config['fastq_gz_R1_wc'],
        r2=wc_config['fastq_gz_R2_wc'],
    output:
        r1=wc_config['fastq_gz_bbtools_tadpole_R1_wc'],
        r2=wc_config['fastq_gz_bbtools_tadpole_R2_wc'],
    log: wc_config['fastq_gz_bbtools_tadpole_log_wc']
    conda: '../../remove_human_bbmap/bbmap_env.yaml'
    shell: ''' tadpole.sh in={input.r1} in2={input.r2} out={output.r1} out2={output.r2} mode=correct ecc=t prefilter=2  -Xmx20g > {log} 2>&1'''