import os, assnake

import assnake_core_preprocessing as ass_proc
from assnake_core_preprocessing.count.result import result
from assnake_core_preprocessing.fastqc.result_fastqc import result_fastqc
from assnake_core_preprocessing.multiqc.cmd_multiqc import multiqc_invocation

from assnake.utils import read_yaml


this_dir = os.path.dirname(os.path.abspath(__file__))

snake_module = assnake.SnakeModule(
    name = 'assnake-core-preprocessing', 
    install_dir = this_dir,
    results = [
        result, 
        ass_proc.trimmomatic.result, 
        result_fastqc,
        ass_proc.remove_human_bbmap.result
    ],

    snakefiles = ['./fastq_dump/download.py','./multiqc/multiqc.py'],
    invocation_commands = [ multiqc_invocation],
    wc_configs = [ read_yaml(os.path.join(this_dir, './multiqc/wc_config.yaml'))]
)
