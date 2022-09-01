try:
    args[0][0]
except:
    print("mkdir: missing operand")
    raise codeExit("missing operand")

run("getdir -oe '%s' '%s'" % (args[0], getCD()))

try:
    os.mkdir(file("/".join(directory)))
except FileExistsError:
    print("mkdir: cannot create directory '%s': File exists"%args[0])
except FileNotFoundError:
    print("mkdir: cannot create directory '%s': No such file or directory"%args[0])

raise codeExit()