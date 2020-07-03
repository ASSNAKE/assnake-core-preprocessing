import os
from assnake.core.result import Result

result = Result.from_location(name='trimmomatic',
                              description='Quality based trimming',
                              result_type = 'preprocessing',
                              input_type='illumina_sample',
                              with_presets=True,
                              static_files_dir_name = 'adapters',
                              location=os.path.dirname(os.path.abspath(__file__)))