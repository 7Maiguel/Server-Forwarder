import json
import os

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def Get_ID_Dispositivo():
    file = open(CURRENT_DIR_PATH + "/../../../Config.json")
    data = json.load(file)
    file.close()
    return data["companyChannel"]
