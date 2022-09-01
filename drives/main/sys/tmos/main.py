print("Loading TMos") #wtf do you think this does

currentDirectory = ["", ""] #sets the current directory to /

class codeExit(Exception):
    pass #sets code exit exception (duh)
class forceExit(Exception):
    pass

def getCD():
    return "/".join(currentDirectory) #do shit with the list to make a human readable directory
def file(direc, currentd=getCD()): #when you run this with a file, it gives a directory to that file for the actual system (/sys/tmos would output ./sys/tmos)
    try:
        direc[0] #check if the dick put something in the directory
    except:
        return
    if direc[0] == "/":
        return direc[1:] #get rid of / if it starts with it, so /sys would be sys
    d = currentd + direc #if no /, get current directory and add it onto direc
    if d[0] == "/":
        return d[1:] #if starts with /, get rid of /
    return d #if no /, return the whole thing
def run(thing, raiseExit=False): #run a command (like cd, ls, mkdir)
    command = shlex.split(thing) #get all arguments, so ["cd", "/sys"]
    commandRun = False #command hasnt been run
    if thing == "":
        command = [""]
    for i in cmds: #go through every command in non-existance
        if i == command[0]: #if the command matches
            try:
                args = command[1:] #check for arguments
            except:
                args = [] #if none, make the list empty
            globals().update(locals()) #make every variable global (surprise communism'd from stack)
            try:
                exec(open(file("/py/%s.py"%i), "r").read()) #open the file from /py and run it
            except codeExit as e:
                commandRun = True
                globals().update(locals())
                if raiseExit:
                    raise codeExit(e)
            except forceExit as e:
                commandRun = True
                globals().update(locals())
                raise forceExit(e)
            except Exception as e:
                print(traceback.format_exc())
            commandRun = True #command has been run
    globals().update(locals()) #make everything global
sys.path.insert(0, file("/usr/lib"))
def include(pkg):
    #os.chdir(file("/usr/lib"))
    exec("globals()[\""+pkg+"\"] = __import__(\"%s\")"%pkg)
    #importlib.import_module("."+pkg, )
    #exec("globals()[\""+pkg+"\"] = __import__(\"%s\")"%pkg)
    #exec("globals()[\""+pkg+"\"] = __import__(\"."+pkg+"\")")
    #exec("class %s:\n    "+open("__init__.py", "r").read())
    #os.chdir("../..")
def includecus(pkg):
    exec(open(file("/usr/lib/%s/main.py"%pkg), "r").read())
    globals().update(locals())
def gethome(user):
    etcpasswd = open(file("/etc/passwd"), "r").readlines()
    for i in etcpasswd:
        userinfo = i.split(":")
        if userinfo[0] == user.lower():
            return userinfo[5]

include("requests")
os.environ["REQUESTS_CA_BUNDLE"]=os.getcwd()+"/usr/lib/requests"

cmdFiles = os.listdir(file("/py")) #look through /py for commands
cmds = [] #make cmds empty
for i in cmdFiles:
    cmds.append(i[:-3]) #add the command to the list but without the .py

includecus("parser")#exec(open(file("/usr/lib/parser/main.py"), "r").read()) #run the parser TEMPORARY
includecus("hash")#exec(open(file("/usr/lib/hash/main.py"), "r").read())
includecus("motd")#exec(open(file("/usr/lib/motd/main.py"), "r").read())

exec(open(file("/sys/tmos/login.py"), "r").read())
args = []
exec(open(file("/py/tmsh.py"), "r").read())
