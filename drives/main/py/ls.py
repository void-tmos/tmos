parser = Parser() #init the parser
parser.addCmd("-l", None, "list") #add the no out argument
parser.addCmd("-a", "--all", "all")
parser.addCmd("-A", "--almost-all", "almost-all")
parser.parse(args) #parse the args
args = parser.args #set args to parser output
opts = parser.output #set opts to parser output

try:
    args[0][0]
    run("getdir --no-output '%s' '%s'" % (args[0], getCD()))
    dirToSearch = file("/".join(directory))
except Exception:
    dirToSearch = file(getCD())

if dirToSearch == "":
    dirToSearch = "."

def get_size(path):
    total_size = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

files = os.listdir(dirToSearch)
files = sorted(files)
if opts["all"]:
    files.reverse()
    files.append("..")
    files.append(".")
    files.reverse()
if opts["list"]:
    print("total %d"%len(files))
for i in files:
    item = dirToSearch + "/" + i
    if i[0] == ".":
        if opts["all"] or opts["almost-all"]:
            pass
        else:
            continue
    if opts["list"]:
        timeModded = time.ctime(os.path.getmtime(item))[:-4]
    if os.path.isfile(item):
        if opts["list"]:
            size = get_size(item)
            sizeSpaces = " "*(6-len(str(size)))
            print("-rwxrwxrwx 1 root root %d%s %s %s" % (size, sizeSpaces, timeModded, i))
            continue
        print(i)
    elif os.path.isdir(item):
        if opts["list"]:
            size = get_size(item)
            sizeSpaces = " "*(6-len(str(size)))
            print("drwxrwxrwx 1 root root %d%s %s \033[96m%s\033[0m" % (size, sizeSpaces, timeModded, i))
            continue
        print("\033[96m%s\033[0m"%i)

"""
try:
    dirToSearch = file(getCD() + args[0])
    args[0][0]
except:
    dirToSearch = file(getCD())

if dirToSearch == "":
    dirToSearch = "."

files = os.listdir(dirToSearch)
for i in files:
    print(i)
"""