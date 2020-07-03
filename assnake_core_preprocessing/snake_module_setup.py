import os, assnake

import assnake_core_preprocessing.count.result as count
import assnake_core_preprocessing.trimmomatic.result as trimmomatic
import assnake_core_preprocessing.multiqc.result as multiqc
import assnake_core_preprocessing.fastqc.result as fastqc


# import assnake_core_preprocessing.bbtools.remove_human_bbmap.result
# import assnake_core_preprocessing.bbtools.dedup.result
# import assnake_core_preprocessing.seqtk_subsample.result
# import assnake_core_preprocessing.bbtools.tadpole.result
# import assnake_core_preprocessing.bbtools.reformat.result
from assnake.utils.general import read_yaml


this_dir = os.path.dirname(os.path.abspath(__file__))

snake_module = assnake.SnakeModule(
    name = 'assnake-core-preprocessing', 
    install_dir = this_dir,
    results = [
        count, 
        trimmomatic, 
        multiqc,
        fastqc
        # assnake_core_preprocessing.bbtools.dedup.result,
        # assnake_core_preprocessing.bbtools.remove_human_bbmap.result,
        # assnake_core_preprocessing.bbtools.tadpole.result,
        # assnake_core_preprocessing.seqtk_subsample.result,
        # assnake_core_preprocessing.bbtools.reformat.result
    ],

    snakefiles = [os.path.join(this_dir, 'fastq_dump/workflow.smk')],
    invocation_commands = []
)
