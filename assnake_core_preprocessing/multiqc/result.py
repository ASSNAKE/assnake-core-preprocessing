import os
from assnake.core.result import Result

result = Result.from_location(name='multiqc',
                              description='Multiqc report from FastQC',
                              result_type='quality_profile',
                              input_type='illumina_strand_file_set',
                              location=os.path.dirname(os.path.abspath(__file__))
                              )
