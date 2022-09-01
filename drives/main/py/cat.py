if args:
    run("getdir -eo '%s' '%s'"%(args[0], getCD()))
    try:
        f = open(file("/".join(directory)), "r")
        print(f.read())
        f.close()
    except Exception as e:
        print("cat: %s" % (e))
else:
    print("cat: missing operand")