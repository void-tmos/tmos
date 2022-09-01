try:
    args[0][0]
    args[1][0]
except:
    print("cp: missing file operand")
    raise codeExit()

run("getdir -eo '%s' '%s'"%(args[0], getCD()))
try:
    f = open(file("/".join(directory)), "r")
    origfile = f.read()
    f.close()
    run("getdir -eo '%s' '%s'"%(args[1], getCD()))
    f = open(file("/".join(directory)), "w")
    f.write(origfile)
    f.close()
except Exception as e:
    print("cp: %s" % (e))