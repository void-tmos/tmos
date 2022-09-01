try:
    args[0][0] #check for any args
except:
    currentDirectory = ["", ""] #if no args, set directory to blank
    raise codeExit("No Arguments Provided") #stop the program

try:
    run("getdir --no-output '%s' '%s'" % (args[0], getCD())) #run getdir
except codeExit:
    raise codeExit()
    currentDirectory = getCD().split("/")

currentDirectory = directory #set the directory to the output of getdir