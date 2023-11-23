import os
import pandas as pd

def get_fastqc_files_for_multiqc(wildcards):
    fastqc_list = []
    sample_set_loc = '{fs_prefix}/{df}/profile/multiqc/{sample_set}_{sample_set_hash}/sample_set_{sample_set_hash}.tsv'.format(**wildcards)
    sample_set = pd.read_csv(sample_set_loc, sep = '\t')
    for s in sample_set.to_dict(orient='records'):
        fastqc_list.append(wc_config['fastqc_data_wc'].format(df = s['df'], fs_prefix = s['fs_prefix'], df_sample = s['df_sample'], preproc = s['preproc'], strand = wildcards.strand))
    return fastqc_list

rule multiqc_list_from_sample_set:
    input:  
        sample_set_loc = '{fs_prefix}/{df}/profile/multiqc/{sample_set}_{sample_set_hash}/sample_set_{sample_set_hash}.tsv',
        fastqc_data = get_fastqc_files_for_multiqc
    output: sample_list = '{fs_prefix}/{df}/profile/multiqc/{sample_set}_{sample_set_hash}/{strand}/samples.list',
    run: 
        fastqc_list = []
        sample_set = pd.read_csv(input.sample_set_loc, sep = '\t')
        for s in sample_set.to_dict(orient='records'):
            fastqc_list.append(wc_config['fastqc_data_wc'].format(df = s['df'], fs_prefix = s['fs_prefix'], df_sample = s['df_sample'], preproc = s['preproc'], strand = wildcards.strand))

        multiqc_dir = os.path.dirname(output.sample_list)
        os.makedirs(os.path.join(multiqc_dir), exist_ok = True)
        try:
            with open(output.sample_list, 'x') as file:
                file.writelines('\n'.join(fastqc_list))
        except FileExistsError:
            print('List already exists')

rule multiqc_fastqc:
    input:
        sample_list    = '{fs_prefix}/{df}/profile/multiqc/{sample_set}_{sample_set_hash}/{strand}/samples.list',
    output:
        multiqc_report = '{fs_prefix}/{df}/profile/multiqc/{sample_set}_{sample_set_hash}/multiqc_report_{strand}.html'
    params:
        wd =     '{fs_prefix}/{df}/profile/multiqc/{sample_set}_{sample_set_hash}/{strand}/',
        prerep = '{fs_prefix}/{df}/profile/multiqc/{sample_set}_{sample_set_hash}/{strand}/multiqc_report.html'
    conda: "multiqc.yaml"
    shell: ("multiqc --file-list {input.sample_list} -o {params.wd}; mv {params.prerep} {output.multiqc_report}")


