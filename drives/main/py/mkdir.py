try:
    args[0][0]
except:
    print("mkdir: missing operand")
    raise codeExit("missing operand")

parser = Parser()
parser.addCmd("-p", "--parent", "parent")
parser.parse(args)
args = parser.args
opts = parser.output

run("getdir -oe '%s' '%s'" % (args[0], getCD()))

if opts["parent"]:
    os.makedirs(file("/".join(directory)), exist_ok=True)
else:
    try:
        os.mkdir(file("/".join(directory)))
    except FileExistsError:
        print("mkdir: cannot create directory '%s': File exists"%args[0])
    except FileNotFoundError:
        print("mkdir: cannot create directory '%s': No such file or directory"%args[0])

raise codeExit()
