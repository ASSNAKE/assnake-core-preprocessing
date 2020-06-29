import click, glob, os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.core.command_builder import sample_set_construction_options, add_options
from assnake.core.result import Result
from assnake.core.config import read_assnake_instance_config

from pathlib import Path



parameters = [p.split('/')[-1].replace('.json', '') for p in glob.glob('/data11/bio/databases/ASSNAKE/params/tmtic/*.json')]
additional_options = [
    click.option(
        '--params', 
        help='Parameters id to use. Available parameter sets: ' + str(parameters), 
        required=False, 
        default = 'def')
]

@click.command('trimmomatic', short_help='Quality based trimming')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def trimmomatic_invocation(config, **kwargs):
    print(config['requested_results'])

    wc_str = '{fs_prefix}/{df}/reads/{preproc}__tmtic_{params}/{df_sample}_R1.fastq.gz'
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'trimmomatic', 'sample_set': sample_set, 'preprocessing': True, 'preprocessing_addition': 'tmtic_'+kwargs['params']}]


this_dir = os.path.dirname(os.path.abspath(__file__))

def params_preparation():
    instance_config = read_assnake_instance_config()
    print('in params')
    if instance_config is not None:
        print('in params')

        print(this_dir)
        # Check for directory for params in current database
        directory_for_param_files_in_db = os.path.join(instance_config['assnake_db'], 'params/tmtic')
        if Path(directory_for_param_files_in_db).exists():
            print('Dir already in database')
            # Now check for files we want to import into database
        else:
            print('Dir is not in database, creating')
            os.makedirs(directory_for_param_files_in_db, exist_ok=True)
    #     # Try to copy default parameters json
    #     shutil.copyfile('./assnake_core_preprocessing/trimmomatic/def.json', os.path.join(config['assnake_db'], 'params/tmtic/def.json'))
    #     # Prepare for parameter copying
    #     dest_folder = os.path.join(instance_config['assnake_db'], 'params/tmtic/adapters')
    #     # Why are we deleting everything??
    #     if os.path.exists(dest_folder):
    #         shutil.rmtree(dest_folder)
    #     # Copying
    #     shutil.copytree('./assnake_core_preprocessing/trimmomatic/adapters', dest_folder)
    # else:
    #     print('NOT PROPERLY CONFIGURED\nRun assnake config init')

result = Result.from_location(name = 'trimmomatic', location = this_dir, input_type = 'illumina_sample', additional_inputs = None, invocation_command = trimmomatic_invocation, params_preparation = params_preparation)
