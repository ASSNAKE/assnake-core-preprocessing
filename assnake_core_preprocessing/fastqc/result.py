import os
from assnake.core.result import Result

result = Result.from_location(name='fastqc',
                              description='Quality control checks on raw sequence data',
                              result_type = 'quality_profile',
                              input_type='illumina_strand_file',
                              location=os.path.dirname(os.path.abspath(__file__))
                              ) 