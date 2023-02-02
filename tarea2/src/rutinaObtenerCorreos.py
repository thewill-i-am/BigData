import re
import yaml
import os 

config_path = os.path.join("/home","william","claseJimmy","tarea2","config", "config.yml")
config = yaml.load(open(config_path), Loader=yaml.FullLoader)

io = open(os.path.join(config['file_path']), 'r')
texto = io.read()
correos = re.findall(config['regex'], texto)
io.close()

print("Cantidad de correos", len(correos))
print(correos)
    
