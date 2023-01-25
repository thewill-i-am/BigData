import pandas as pd
import yaml 
import os

config_path = os.path.join("/home/william/claseJimmy/config", "config.yml" )

config = yaml.load(open(config_path), Loader=yaml.FullLoader)

df = pd.read_csv(config['file_path'])

print(df)
