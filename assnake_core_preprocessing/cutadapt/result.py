import os
from assnake.core.Result import Result

result = Result.from_location(name='cutadapt',
                              description='CUTADAPT',
                              result_type = 'preprocessing',
                              input_type='illumina_sample',
                              with_presets=True,
                              preset_file_format='txt',
                              location=os.path.dirname(os.path.abspath(__file__)))