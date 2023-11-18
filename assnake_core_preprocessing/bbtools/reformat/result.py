import os
from assnake.core.Result import Result

import click, glob, os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.cli.command_builder import sample_set_construction_options, add_options
from assnake.core.Result import Result
parameters = []

@click.command('bbtools-reformat-subsample', short_help='Subsample')
@click.option('--params', help='Parameters id to use. Available parameter sets: ' + str(parameters), required=False, default = 'def')
@add_options(sample_set_construction_options)
@click.pass_obj
def bbtools_tadpole_invocation(config, params, **kwargs):
    wc_str = '{fs_prefix}/{df}/reads/{preproc}__bbtsbsmpl_{params}/{df_sample}_R1.fastq.gz'
    kwargs.update({'params': params})
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)

this_dir = os.path.dirname(os.path.abspath(__file__))
result = Result.from_location(name = 'bbtools-reformat-subsample', location = this_dir, input_type = 'illumina_sample', additional_inputs = None, invocation_command = bbtools_tadpole_invocation)


