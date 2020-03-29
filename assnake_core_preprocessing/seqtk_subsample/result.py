import click, glob, os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.cli.cli_utils import sample_set_construction_options, add_options
from assnake.core.result import Result


@click.command('seqtk-subsample', short_help='Subsample your reads')
@add_options(sample_set_construction_options)
@click.pass_obj
def seqtk_subsample_invocation(config,  **kwargs):
    # print(config['wc_config'])
    wc_str = '{fs_prefix}/{df}/reads/{preproc}__seqtk_sbsmpl/{df_sample}_R1.fastq.gz'
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)

this_dir = os.path.dirname(os.path.abspath(__file__))
result = Result.from_location(name = 'seqtk-subsample', location = this_dir, input_type = 'illumina_sample', additional_inputs = None, invocation_command = seqtk_subsample_invocation)
