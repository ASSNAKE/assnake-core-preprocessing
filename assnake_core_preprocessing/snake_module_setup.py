import os
import assnake
from assnake_core_preprocessing.count.cmd_count import count_invocation
from assnake_core_preprocessing.trimmomatic.cmd_trimmomatic import trimmomatic_invocation
from assnake_core_preprocessing.remove_human_bbmap.init_remove_human_bbmap import init_remove_human_bbmap
from assnake_core_preprocessing.remove_human_bbmap.cmd_remove_human_bbmap import remove_human_bbmap
from assnake_core_preprocessing.multiqc.cmd_multiqc import multiqc_invocation

from assnake_core_preprocessing.fastqc.cmd_fastqc import fastqc_start
from assnake.utils import read_yaml
this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = assnake.SnakeModule(name = 'assnake-core-preprocessing', 
                           install_dir = this_dir,
                           snakefiles = ['./count/count.py', 
                            './trimmomatic/trimmomatic.py',
                            './fastqc/fastqc.py',
                            './remove_human_bbmap/remove_human_bbmap.py',
                            './multiqc/multiqc.py'],
                           invocation_commands = [count_invocation, trimmomatic_invocation, remove_human_bbmap, fastqc_start, multiqc_invocation],
                           initialization_commands = [init_remove_human_bbmap],
                           wc_configs = [read_yaml(os.path.join(this_dir, './count/wc_config.yaml')), 
                            read_yaml(os.path.join(this_dir, './remove_human_bbmap/wc_config.yaml')),
                            read_yaml(os.path.join(this_dir, './trimmomatic/wc_config.yaml')),
                            read_yaml(os.path.join(this_dir, './multiqc/wc_config.yaml'))])
