rule bbtools_clumpify:
    input:
        r1=wc_config['fastq_gz_R1_wc'],
        r2=wc_config['fastq_gz_R2_wc'],
    output:
        r1=wc_config['fastq_gz_bbtools_dedup_R1_wc'],
        r2=wc_config['fastq_gz_bbtools_dedup_R2_wc'],
    log: wc_config['fastq_gz_bbtools_dedup_log_wc']
    conda: '../../remove_human_bbmap/bbmap_env.yaml'
    shell: '''clumpify.sh in={input.r1} in2={input.r2} out={output.r1} out2={output.r2} dedupe subs=0 passes=2 -Xmx20g > {log} 2>&1'''