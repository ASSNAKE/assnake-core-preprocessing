import os
from assnake.core.Result import Result

result = Result.from_location(name='count',
                              description='Count number of reads and basepairs in fastq file',
                              result_type = 'quality_profile',
                              input_type='illumina_strand_file',
                              location=os.path.dirname(os.path.abspath(__file__))
                              ) 