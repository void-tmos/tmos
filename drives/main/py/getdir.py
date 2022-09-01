global directory                                        #make directory global

try:
    args[0][0]                                          #check for arguments
except:
    directory = ["", ""]                                #make it blank if no args
    beforeExit(opts, error="No Arguments Provided")     #run this everytime before stopping program
    raise codeExit("No Arguments Provided")             #stop the program

parser = Parser()                                       #init the parser
parser.addCmd("-o", "--no-output", "no-out")            #add the no out argument
parser.addCmd("-e", "--no-exist", "no-exist")
parser.addCmd("-f", "--files", "add-files")
parser.addCmd(None, "--no-error", "no-error")
parser.parse(args)                                      #parse the args
args = parser.args                                      #set args to parser output
opts = parser.output                                    #set opts to parser output

direc = args[0]                                         #directory to go to (tmos)
directory = args[1]                                     #current directory (/sys)
directory = directory.split("/")                        #split directory into a list

def beforeExit(opts, error=None):                       #define beforeExit
    global direc, directory, cmdName                    #make some vars global
    if len(directory) == 1:                             #if directory is 1 long, or [""], set it to ["", ""] (this is very important)
        directory = ["", ""]
    if error:                                           #if error is a keyword arg
        if not opts["no-error"]:
            print(error)                                #print it
        return                                          #exit
    if opts["no-out"]:                                  #if no-output is an argument 
        pass                                            #pass
    else:                                               #if not
        print("/".join(directory))                      #print it

if direc == "/":                                        #if direc is root
    directory = ["", ""]                                #set directory to root
    beforeExit(opts)
    raise codeExit("Directory is root")
if direc[0] == "/":
    directory = ["", ""]
    direc = direc[1:]
folders = direc.split("/")                              #split direc into a list
for i in folders:                                       #for every folder in direc
    if directory == ["", ""]:                           #if its root,
        directory = [""]                                #set it to this
    if i == ".." and len(directory) > 1:                #if its .. and length of directory is 2 or more
        directory.pop()                                 #go back
        continue                                        #skip to next directory
    if i == "":                                         #if its blank
        continue                                        #skip
    if "/".join(directory) in ["", "/"]:                #if current directory is root
        pathToSearch = i                                #search for i
    else:                                               #if not
        pathToSearch = "/".join(directory) + "/" + i    #search for directory + i
    if os.path.isfile(file(pathToSearch, currentd="/".join(directory))) and not opts["no-exist"]: #if its a file, 
        if not opts["add-files"]:
            errormsg = "getdir: /%s: Not a directory" % file(pathToSearch)                            #error message
            beforeExit(opts, error=errormsg)                                                          #before exit
            raise forceExit(errormsg)                                                                  #exit
    if os.path.exists(file(pathToSearch, currentd="/".join(directory))) or opts["no-exist"]:      #if it exists
        directory.append(i)                                                                       #add it to the directory
        if len(directory) == 2:                                                                   #if its only 2 long,  
            if directory[0] == "/":                                                               #if its root,
                directory[0] = ""                                                                 #set it to blank
    else:                                                                                         #if it doesnt exist
        errormsg = "getdir: /%s: No such file or directory" % file(pathToSearch)                  #error message
        directory = currentDirectory
        beforeExit(opts, error=errormsg)                                                          #before exit
        raise forceExit(errormsg)                                                                  #exit

beforeExit(opts)                                        #before exit
raise codeExit(0)                                       #exit