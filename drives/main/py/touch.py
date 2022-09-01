try:
    args[0][0]
except:
    print("touch: missing file operand")
    raise codeExit()

run("getdir -eo '%s' '%s'"%(args[0], getCD()))

try:
    f = open(file("/".join(directory)), "w")
    f.write('')
    f.close()
except Exception as e:
    print("touch: %s" % e)