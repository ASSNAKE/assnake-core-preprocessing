import click, glob, os
# from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.cli.command_builder import sample_set_construction_options, add_options
from assnake.core.Result import Result

this_dir = os.path.dirname(os.path.abspath(__file__))
result = Result.from_location(name = 'remove-human-bbmap', 
                        location = this_dir, 
                        description='Human DNA removal',
                              result_type = 'preprocessing',
                              input_type='illumina_sample',)
