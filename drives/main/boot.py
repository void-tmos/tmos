#-------TDNE/NEL---------
import ast
import os

bootConfig = ast.literal_eval(open("boot/boot.conf", "r").read())

exec(open("boot/%s"%bootConfig["loader"], "r").read())