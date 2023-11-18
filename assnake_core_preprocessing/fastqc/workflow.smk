rule fastqc:
    input: wc_config['fastq_gz_file_wc']
    output: 
        zipped=wc_config['fastqc_zip_wc'],
        fastqc_data = wc_config['fastqc_data_wc']
    params: 
        out="{fs_prefix}/{df}/profile/fastqc/{preproc}/{df_sample}/",
        zip_out="{fs_prefix}/{df}/profile/fastqc/{preproc}/{df_sample}/fastqc",
        
    log: "{fs_prefix}/{df}/profile/fastqc/{preproc}/{df_sample}/{df_sample}_{strand}.log"
    threads: 6
    conda: 'env_v0.11.8.yaml'
    shell: ('''export PERL5LIB='';\nfastqc -t {threads} --nogroup -o {params.out} {input} >{log} 2>&1; \n
          unzip -qq -o {output.zipped} -d {params.out}''')

rule fastqc_nogroup:
    input: "{prefix}/{df}/reads/{preproc}/{df_sample}/{df_sample}_{strand}.fastq.gz"
    output: 
        zipped="{prefix}/{df}/reads/{preproc}/{df_sample}/profile/fastqc_nogroup/{df_sample}_{strand}_fastqc.zip"
    params: 
        out="{prefix}/{df}/reads/{preproc}/{df_sample}/profile/fastqc_nogroup/",
        zip_out="{prefix}/{df}/reads/{preproc}/{df_sample}/profile/fastqc_nogroup/"
    log: "{prefix}/{df}/reads/{preproc}/{df_sample}/profile/fastqc_nogroup/{df_sample}_{strand}.log"
    threads: 6
    conda: 'env_v0.11.8.yaml'
    shell: ('''export PERL5LIB='';\nfastqc -t {threads} --nogroup -o {params.out} {input} >{log} 2>&1; \n
          unzip -qq -o {output.zipped} -d {params.zip_out}''')
