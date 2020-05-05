import click
import os
import json



class Config(dict):
    def __init__(self, *args, **kwargs):
        config_path= os.path.join(click.get_app_dir('tbox'))
        os.makedirs(config_path, exist_ok=True)
        self.config = os.path.join(click.get_app_dir('tbox'),'config.json')
        super(Config, self).__init__(*args, **kwargs)

        self.verbose = False

    def load(self):
        """load a JSON config file from disk"""
        try:
            with open(self.config,'r') as f:
                self.update(json.load(f))
        except Exception:
            print("Error loading config")
            pass
            
    def save(self):
        #self.config.ensure()
        try:
            with open(self.config,'w') as f:
                f.write(json.dumps(self))
        except Exception:
                print("Error writing config")

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', '-v', is_flag=True, help="verbose mode")
@pass_config
def tbox(config, verbose):
    """ >>>> TBOX <<<<  """
    config.load()
    config.verbose = verbose
    pass