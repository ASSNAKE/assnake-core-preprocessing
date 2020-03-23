import assnake.api.loaders
import assnake
from tabulate import tabulate
import click
from assnake.cli.cli_utils import sample_set_construction_options, add_options, generic_command_individual_samples, generate_result_list
import os, datetime 
import pandas as pd

@click.command('fastqc', short_help='Fastqc - quality control checks on raw sequence data')
@add_options(sample_set_construction_options)

@click.pass_obj

def fastqc_start(config, **kwargs):
    wc_str = config['wc_config']['fastqc_zip_wc']

    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)

    kwargs.update({'strand': 'R1'})
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    kwargs['strand'] = 'R2'
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)