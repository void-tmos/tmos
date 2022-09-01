#-----TDNE/NEL------

oses = bootConfig["oses"]

if len(oses) > 1:
    print("Select an OS to boot from or press Return for the default")
    for i in range(0, len(oses)):
        print("%d) %s" % (i+1, oses[i][1]))
    sel = input("Enter selection: ")
    if sel == "":
        sel = bootConfig["default"]
    else:
        sel = int(sel)
    toBoot = oses[sel-1]
else:
    toBoot = oses[0]

print("Booting into %s" % toBoot[1])
exec(open(toBoot[0], "r").read())