import os, assnake

import assnake_core_preprocessing.count.result
import assnake_core_preprocessing.remove_human_bbmap.result
import assnake_core_preprocessing.trimmomatic.result
import assnake_core_preprocessing.multiqc.result
import assnake_core_preprocessing.count.result
import assnake_core_preprocessing.seqtk_subsample.result
from assnake_core_preprocessing.fastqc.result_fastqc import result_fastqc
import assnake_core_preprocessing.bbtools.tadpole.result
from assnake.utils import read_yaml


this_dir = os.path.dirname(os.path.abspath(__file__))

snake_module = assnake.SnakeModule(
    name = 'assnake-core-preprocessing', 
    install_dir = this_dir,
    results = [
        assnake_core_preprocessing.count.result, 
        assnake_core_preprocessing.trimmomatic.result, 
        result_fastqc,
        assnake_core_preprocessing.remove_human_bbmap.result,
        assnake_core_preprocessing.multiqc.result,
        assnake_core_preprocessing.bbtools.tadpole.result,
        assnake_core_preprocessing.seqtk_subsample.result
    ],

    snakefiles = [],
    invocation_commands = []
)
