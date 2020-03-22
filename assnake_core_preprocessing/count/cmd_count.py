import assnake.api.loaders
import assnake
from tabulate import tabulate
import click, os
import pandas as pd

@click.command('count', short_help='Count number of reads and basepairs in fastq file')

@click.option('--df','-d', help='Name of the dataset', required=True )
@click.option('--preproc','-p', help='Preprocessing to use' )

@click.option('--meta-column', '-c', help='Select samples based on metadata column' )
@click.option('--column-value','-v', help='Value of metadata column by which select samples' )

@click.option('--samples-to-add','-s', 
                help='Samples from dataset to process', 
                default='', 
                metavar='<samples_to_add>', 
                type=click.STRING )

@click.pass_obj

def count_invocation(config, df, preproc, meta_column, column_value, samples_to_add):
    samples_to_add = [] if samples_to_add == '' else [c.strip() for c in samples_to_add.split(',')]
    df = assnake.api.loaders.load_df_from_db(df)

    meta_loc = os.path.join(df['fs_prefix'], df['df'], 'mg_samples.tsv')
    if os.path.isfile(meta_loc):
        meta = pd.read_csv(os.path.join(df['fs_prefix'], df['df'], 'mg_samples.tsv'), sep = '\t')

        if meta_column is not None and column_value is not None:
            subset_by_col_value = meta.loc[meta[meta_column] == column_value]
            if len(subset_by_col_value) > 0:
                samples_to_add = list(subset_by_col_value['new_sample_name'])

    

    ss = assnake.SampleSet.SampleSet(df['fs_prefix'], df['df'], preproc, samples_to_add=samples_to_add)
    config['requested_dfs'] += [df['df']] 

    click.echo(tabulate(ss.samples_pd[['fs_name', 'reads', 'preproc']].sort_values('reads'), headers='keys', tablefmt='fancy_grid'))

    res_list = []
    for s in ss.samples_pd.to_dict(orient='records'):
        if preproc == '':
            preprocessing = s['preproc']
        else:
            preprocessing = preproc
        for strand in ['R1', 'R2']:
            res_list.append(config['wc_config']['count_wc'].format(
                fs_prefix = s['fs_prefix'].rstrip('\/'),
                df = s['df'],
                preproc = s['preproc'],
                sample = s['fs_name'],
                strand = strand
            )) 


    if config.get('requests', None) is None:
        config['requests'] = res_list
    else:
        config['requests'] += res_list