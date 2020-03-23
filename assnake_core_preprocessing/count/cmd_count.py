import assnake.api.loaders
import assnake
from tabulate import tabulate
import click, os
import pandas as pd
from assnake.cli.cli_utils import sample_set_construction_options, add_options, generic_command_individual_samples, generate_result_list

@click.command('count', short_help='Count number of reads and basepairs in fastq file')
@add_options(sample_set_construction_options)
@click.pass_obj

def count_invocation(config, **kwargs):
    wc_str = config['wc_config']['count_wc'] 
    kwargs.update({'strand': 'R1'})
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
