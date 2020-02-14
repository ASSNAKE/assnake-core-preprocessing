import os
from assnake.api.snake_module import SnakeModule
from assnake_core_preprocessing.count.cmd_count import count_invocation
from assnake_core_preprocessing.trimmomatic.cmd_trimmomatic import trimmomatic_invocation
from assnake.utils import read_yaml
this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = SnakeModule(name = 'assnake-core-preprocessing', 
                           install_dir = this_dir,
                           snakefiles = ['./count/count.py', './trimmomatic/trimmomatic.py'],
                           invocation_commands = [count_invocation, trimmomatic_invocation],
                           wc_configs = [read_yaml(os.path.join(this_dir, './count/wc_config.yaml')),
                            read_yaml(os.path.join(this_dir, './trimmomatic/wc_config.yaml'))])
