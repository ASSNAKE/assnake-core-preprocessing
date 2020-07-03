import os
from assnake.core.result import Result

result = Result.from_location(name='count',
                              result_type = 'quality_profile',
                              description='Count number of reads and basepairs in fastq file',
                              input_type='illumina_strand_file',
                              location=os.path.dirname(os.path.abspath(__file__))
                              ) 