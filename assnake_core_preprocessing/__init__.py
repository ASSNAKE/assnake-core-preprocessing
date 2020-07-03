import os, assnake

snake_module = assnake.SnakeModule(
    name = 'assnake-core-preprocessing', 
    install_dir = os.path.dirname(os.path.abspath(__file__)),
)
