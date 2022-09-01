parser = Parser() #init the parser
parser.addCmd("-r", None, "recursive")
parser.addCmd("-f", None, "force")
parser.parse(args) #parse the args
args = parser.args #set args to parser output
opts = parser.output #set opts to parser output

try:
    args[0][0]
except:
    print("rm: missing operand")
    raise codeExit()
    
run("getdir -of '%s' '%s'" % (args[0], getCD()))

try:
    os.remove(file("/".join(directory)))
except FileNotFoundError:
    if not opts["force"]:
        print('rm: %s: No such file or directory'%args[0])
        raise codeExit()
except IsADirectoryError:
    if opts["recursive"]:
        for dirpath, dirnames, filenames in os.walk(file("/".join(directory))):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    os.remove(fp)
                except FileNotFoundError:
                    if not opts["force"]:
                        print('rm: %s: No such file or directory'%fp)
                        raise codeExit()
        os.rmdir(file("/".join(directory)))
    else:
        if not opts["force"]:
            print('rm: %s: is a directory'%args[0])
            raise codeExit()
except PermissionError:
    if opts["recursive"]:
        for dirpath, dirnames, filenames in os.walk(file("/".join(directory))):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    os.remove(fp)
                except FileNotFoundError:
                    if not opts["force"]:
                        print('rm: %s: No such file or directory'%fp)
                        raise codeExit()
        os.rmdir(file("/".join(directory)))
    else:
        if not opts["force"]:
            print('rm: %s: is a directory'%args[0])
            raise codeExit()