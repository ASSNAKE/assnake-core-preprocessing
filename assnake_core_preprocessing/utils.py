import assnake.api.loaders
import assnake
from tabulate import tabulate
import click
import os
import pandas as pd

def format_cmdinp2obj(config, df, preproc, meta_column, column_value, samples_to_add):
    samples_to_add = [] if samples_to_add == '' else [c.strip() for c in samples_to_add.split(',')]
    df_loaded = assnake.api.loaders.load_df_from_db(df)
    config['requested_dfs'] += [df_loaded['df']]

    # Now for the meta column stuff
    meta_loc = os.path.join(df_loaded['fs_prefix'], df_loaded['df'], 'mg_samples.tsv')
    if os.path.isfile(meta_loc):
        meta = pd.read_csv(meta_loc, sep = '\t')

        if meta_column is not None and column_value is not None:
            subset_by_col_value = meta.loc[meta[meta_column] == column_value]
            if len(subset_by_col_value) > 0:
                samples_to_add = list(subset_by_col_value['new_sample_name'])


    SampleSetObj = assnake.SampleSet.SampleSet(df_loaded['fs_prefix'], df_loaded['df'], preproc,
                                          samples_to_add=samples_to_add)

    click.echo(tabulate(SampleSetObj.samples_pd[['fs_name', 'reads', 'preproc']].sort_values('reads'),
                        headers='keys', tablefmt='fancy_grid'))
    return SampleSetObj, df_loaded


# DONE self to ss
def prepare_fastqc_list_multiqc(sample_setObj, strand, set_name):
    fastqc_list = []

    for s in sample_setObj.samples_pd.to_dict(orient='records'):
        fastqc_list.append(sample_setObj.wc_config['fastqc_data_wc'].format(**s, strand=strand))

    dfs = list(set(sample_setObj.samples_pd['df']))

    if len(dfs) == 1:
        fs_prefix = list(set(sample_setObj.samples_pd['fs_prefix']))[0]
        sample_list = sample_setObj.wc_config['multiqc_fastqc_wc'].format(
            df=dfs[0],
            fs_prefix=fs_prefix,
            strand=strand,
            sample_set=set_name)
        # print(sample_list)

        multiqc_dir = os.path.dirname(sample_list)
        if not os.path.isdir(multiqc_dir):
            os.makedirs(multiqc_dir)
        try:
            with open(sample_list, 'x') as file:
                file.writelines('\n'.join(fastqc_list))
        except FileExistsError:
            print('List already exists')

    return fastqc_list
