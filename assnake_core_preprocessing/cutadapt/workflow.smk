rule cutadapt:
    input:
        r1=wc_config['fastq_gz_R1_wc'],
        r2=wc_config['fastq_gz_R2_wc']
    output:
        r1='{fs_prefix}/{df}/reads/{preproc}__cutadapt3/{df_sample}_R1.fastq.gz',
        r2='{fs_prefix}/{df}/reads/{preproc}__cutadapt3/{df_sample}_R2.fastq.gz'
    log: "{fs_prefix}/{df}/reads/{preproc}__cutadapt3/{df_sample}.log"
    threads: 8#config['assnake-core-preprocessing']['results']['cutadapt']['threads']
    wildcard_constraints:    
        params="[\w\d_-]+",
    conda: 'env.yaml'
    shell: '''
    cutadapt --cores {threads} -g CCTACGGGNGGCWGCAG -a GGATTAGATACCCBDGTAGTC \
     -G GACTACHVGGGTATCTAATCC -A CTGCWGCCNCCCGTAGG\
     --pair-filter=any --discard-untrimmed	--maximum-length 235 --minimum-length 223\
     -n 2 -o {output.r1} -p {output.r2} {input.r1} {input.r2}  > {log} 2>&1;
    '''