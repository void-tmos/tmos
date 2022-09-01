#-------™OS--------
#fuck you
import os
import ast
import time
import readline
from getpass import getpass
import hashlib
import shlex
import random
import traceback
import tarfile
import sys

class errors:
    with open("errors.py", "r") as f:
        errors = ast.literal_eval(f.read())

class BIOS:
    class Drive():
        def __init__(self, name, loc, bootable="no", conf=None):
            self.name = name
            self.loc = loc
            self.bootable = bootable
            self.conf = conf
    class DriveError(Exception):
        pass

drives = []
driveDir = os.listdir("./drives")
for i in driveDir:
    if i in [".DS_Store"]:
        continue
    bootable = True
    try:
        if i[0] != ".":
            open("./drives/%s/boot.py"%i, "r")
    except FileNotFoundError:
        bootable = False
    drive = BIOS.Drive(i, i, bootable=bootable)
    drives.append(drive)
    
    """
    f = open("./drives/%s/drive.conf"%i, "r")
    driveConf = ast.literal_eval(f.read())
    drive = BIOS.Drive(driveConf["name"], i, bootable=driveConf["bootable"], conf=driveConf)
    drives.append(drive)
    f.close()
    del drive, driveConf
    #except Exception as e:
    #    raise BIOS.DriveError(errors.errors["0x00000006"]%i)
    """

f = open("config.json", "r")
config = ast.literal_eval(f.read())
f.close()

print(config["startupmsg"])
action = input(config["actionmsg"])
if action == "s":
    pass
    #TODO: this

for i in config["bootOrder"]:
    for j in drives:
        if j.loc == i:
            #try:
            os.chdir("./drives/%s"%i)
            os.system('clear')
            exec(open("boot.py", "r").read())
            #except Exception as e:
            #    print("FATAL: Error occured, %s" % e)