import os
from assnake.core.result import Result

result = Result.from_location(name='cutadapt',
                              description='CUTADAPT',
                              result_type = 'preprocessing',
                              input_type='illumina_sample',
                              with_presets=False,
                              location=os.path.dirname(os.path.abspath(__file__)))