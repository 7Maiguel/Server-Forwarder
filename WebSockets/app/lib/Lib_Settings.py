import json
import os

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def Get_Rout_server():
    file = open(CURRENT_DIR_PATH + "/../../../Config.json")
    data = json.load(file)
    file.close()
    return data["fuseaccessServer"]

def Get_Forward_server():
    file = open(CURRENT_DIR_PATH + "/../../../Config.json")
    data = json.load(file)
    file.close()
    return data["serverToForward"]


def Get_Socket_Timeout():
    file = open(CURRENT_DIR_PATH + "/../../../Config.json")
    data = json.load(file)
    file.close()
    return data["sockectsTimeout"]
