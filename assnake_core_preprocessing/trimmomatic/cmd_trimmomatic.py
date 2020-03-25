import assnake.api.loaders
import assnake
import click, glob
from assnake.cli.cli_utils import sample_set_construction_options, add_options, generic_command_individual_samples, generate_result_list

parameters = [p.split('/')[-1].replace('.json', '') for p in glob.glob('/data11/bio/databases/ASSNAKE/params/tmtic/*.json')]

@click.command('trimmomatic', short_help='Quality based trimming')
@click.option('--params', help='Parameters id to use. Available parameter sets: ' + str(parameters), required=False, default = 'def')
@add_options(sample_set_construction_options)
@click.pass_obj

def trimmomatic_invocation(config, params, **kwargs):
    wc_str = '{fs_prefix}/{df}/reads/{preproc}__tmtic_{params}/{sample}_R1.fastq.gz'
    kwargs.update({'params': params})
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)