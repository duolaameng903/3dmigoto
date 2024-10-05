import configparser
import subprocess
import pyuac
import time
import sys
import os

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()
    sys.exit()

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path, "config.ini")

if not os.path.isfile(config_path):
    config = configparser.ConfigParser()

    config['PATH'] = {'Genshin exe path': '', '3dmigoto path': ''}

    with open(config_path, 'w') as configfile:
        config.write(configfile)
    raise FileNotFoundError("Edit config.ini")

config = configparser.ConfigParser()
config.read(config_path)
if config['DEBUG']['Debug Process'] == 1:
    subprocess.Popen(config['PATH']['3dmigoto path'], cwd=str(os.path.dirname(config['PATH']['3dmigoto path']) + '\\"').replace('"',''))    
else:
    subprocess.Popen(config['PATH']['3dmigoto path'], cwd=str(os.path.dirname(config['PATH']['3dmigoto path']) + '\\"').replace('"',''), shell=False)
time.sleep(int(config['DELAY']['delay']))
print(int(config['DELAY']['delay']))
if config['DEBUG']['Debug Process'] == 1:
    subprocess.run(config['PATH']['Genshin exe path'], shell = True)
else:    
    subprocess.run(config['PATH']['Genshin exe path'], capture_output = True, text = True)