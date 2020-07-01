import click
import glob
import os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.core.command_builder import sample_set_construction_options, add_options
from assnake.core.result import Result
from assnake.core.config import read_assnake_instance_config

from assnake.utils.general import compute_crc32_of_dumped_dict

from pathlib import Path
import zlib
import json
import shutil

instance_config = read_assnake_instance_config()
if instance_config is not None:
    parameters = [p.split('/')[-1].replace('.json', '')
                  for p in glob.glob(os.path.join(instance_config['assnake_db'], 'params/tmtic/*.json'))]
additional_options = [
    click.option(
        '--params',
        help='Parameters id to use. Available parameter sets: ' +
        str([p.split('.')[0] for p in parameters]),
        required=False,
        default='def')
]


@click.command('trimmomatic', short_help='Quality based trimming')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def trimmomatic_invocation(config, **kwargs):
    print(config['requested_results'])

    wc_str = '{fs_prefix}/{df}/reads/{preproc}__tmtic_{params}/{df_sample}_R1.fastq.gz'
    sample_set, sample_set_name = generic_command_individual_samples(
        config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'trimmomatic', 'sample_set': sample_set,
                                     'preprocessing': True, 'preprocessing_addition': 'tmtic_'+kwargs['params']}]


this_dir = os.path.dirname(os.path.abspath(__file__))


def params_preparation():
    # Check that it assnake initialized
    instance_config = read_assnake_instance_config()
    if instance_config is not None:
        # Check for directory for params in current database and create if not
        os.makedirs(os.path.join(
            instance_config['assnake_db'], 'params/tmtic'), exist_ok=True)

        # Now get params files we want to import into database
        presets_included_files = glob.glob(
            os.path.join(this_dir, 'params/*.json'))

        for preset_file_loc in presets_included_files:
            preset_name = os.path.basename(preset_file_loc).split('.')[0]
            preset_crc32_hex = compute_crc32_of_dumped_dict(preset_file_loc)
            # Try to copy default parameters json
            loc_in_db = os.path.join(instance_config['assnake_db'],
                                     'params/tmtic/{preset}.{hash}.json'.format(
                hash=preset_crc32_hex, 
                preset=preset_name))
            shutil.copyfile(preset_file_loc, loc_in_db)

        # Now go with the static files
        static_files_locs = glob.glob(os.path.join(this_dir, 'adapters/*'))
        os.makedirs(os.path.join(
            instance_config['assnake_db'], 'params/tmtic/adapters/'), exist_ok=True)
        # Prepare for parameter copying
        for static_file_loc in static_files_locs:
            dest_loc = os.path.join(
                instance_config['assnake_db'], 'params/tmtic/adapters/' + os.path.basename(static_file_loc))
            shutil.copyfile(static_file_loc, dest_loc)
        print('SUCCESSFULLY DEPLOYED TRIMMOMATIC PRESET PARAMETERS TO DATABASE')
    else:
        print('NOT PROPERLY CONFIGURED\nRun assnake config init')


result = Result.from_location(name='trimmomatic', location=this_dir, input_type='illumina_sample',
                              additional_inputs=None, invocation_command=trimmomatic_invocation, params_preparation=params_preparation)
