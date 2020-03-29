rule seqtk_subsample:
    input: 
        r1 = wc_config['fastq_gz_R1_wc'],
        r2 = wc_config['fastq_gz_R2_wc']
    output: 
        r1 = wc_config['seqtk_subsample_R1_wc'],
        r2 = wc_config['seqtk_subsample_R2_wc']
    log: wc_config['seqtk_subsample_log_wc']
    threads: 1
    conda: 'env.yaml'
    shell: ('''seqtk sample -s100 {input.r1} 0.004 > {output.r1}; seqtk sample -s100 {input.r2} 0.004 > {output.r2}''')
