import os
from assnake.core.result import Result

import click, glob, os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.core.command_builder import sample_set_construction_options, add_options
from assnake.core.result import Result
parameters = []

@click.command('bbtools-dedup', short_help='Reads deduplication')
@click.option('--params', help='Parameters id to use. Available parameter sets: ' + str(parameters), required=False, default = 'def')
@add_options(sample_set_construction_options)
@click.pass_obj
def bbtools_tadpole_invocation(config, params, **kwargs):
    wc_str = '{fs_prefix}/{df}/reads/{preproc}__bbtdedup_{params}/{df_sample}_R1.fastq.gz'
    kwargs.update({'params': params})
    if (kwargs['df'] is None):
        previous_requested_result = config['requested_results'][-1]
        if previous_requested_result['preprocessing']:
            sample_set = previous_requested_result['sample_set']
            sample_set['preproc'] = sample_set['preproc']+'__'+previous_requested_result['preprocessing_addition']
    else:
        sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)



    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'bbtools-dedup', 'sample_set': sample_set, 'preprocessing': True}]


this_dir = os.path.dirname(os.path.abspath(__file__))
result = Result.from_location(name = 'bbtools_dedup', location = this_dir, input_type = 'illumina_sample', additional_inputs = None, invocation_command = bbtools_tadpole_invocation)


