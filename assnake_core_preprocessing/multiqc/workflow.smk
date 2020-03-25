import os
import pandas as pd

rule multiqc_ist_from_sample_set:
    input:  '{fs_prefix}/{df}/profile/multiqc/{sample_set}/sample_set.tsv'
    output: wc_config['sample_list_wc'],
    run: 
        fastqc_list = []
        sample_set = pd.read_csv({input}, sep = '\t')
        for s in sample_set.to_dict(orient='records'):
            fastqc_list.append(wc_config['fastqc_data_wc'].format(df = s['df'], fs_prefix = s['fs_prefix'], fs_name = s['fs_name'], preproc = s['preproc'], strand = {wildcards.strand}))

        multiqc_dir = os.path.dirname({input})
        os.makedirs(multiqc_dir, exists_ok = True)
        try:
            with open({output}, 'x') as file:
                file.writelines('\n'.join(fastqc_list))
        except FileExistsError:
            print('List already exists')

def get_fastqc_files_for_multiqc(wildcards):
    fastqc_files = []
    if os.path.isfile('{fs_prefix}/{df}/profile/multiqc/{sample_set}/{strand}/samples.list'.format(**wildcards)):
        with open('{fs_prefix}/{df}/profile/multiqc/{sample_set}/{strand}/samples.list'.format(**wildcards), 'r') as sample_list:
            fastqc_files = [s.strip() for s in sample_list.readlines()]
        return fastqc_files
    else: 
        return []

rule multiqc_fastqc:
    input:
        sample_list = wc_config['sample_list_wc'],
        samples = get_fastqc_files_for_multiqc
    output:
        multiqc_report = '{fs_prefix}/{df}/profile/multiqc/{sample_set}/multiqc_report_{strand}.html'
    params:
        wd = wc_config['work_dir_wc'],
        prerep = '{fs_prefix}/{df}/profile/multiqc/{sample_set}/{strand}/multiqc_report.html'
    conda: "multiqc.yaml"
    shell: ("export LC_ALL=en_US.UTF-8; export LANG=en_US.UTF-8; multiqc --file-list {input.sample_list} -o {params.wd}; mv {params.prerep} {output.multiqc_report}")


