try:
    args[0][0]
except:
    currentDirectory = ["", ""]
    raise codeExit()

direc = args[0]

if direc == ".." and len(currentDirectory) > 1:
    currentDirectory.pop()
    if len(currentDirectory) == 1:
        currentDirectory.append("")
else:
    if direc[0] == "/":
        currentDirectory = ["", ""]
        """
        folders = direc.split("/")
        print(folders)
        for i in folders:
            if i == ".." and len(currentDirectory) > 1:
                currentDirectory.pop()
                backwards = True
            else:
                currentDirectory.append(i)
                backwards = False
                if len(currentDirectory) == 2:
                    if currentDirectory[0] == "/":
                        currentDirectory[0] = ""
        if backwards:
            currentDirectory.append("")
        print(currentDirectory)
        """
    folders = direc.split("/")
    if direc == "/":
        currentDirectory = ["", ""]
        raise codeExit()
    for i in folders:
        if currentDirectory == ["", ""]:
            currentDirectory.pop()
        if i == ".." and len(currentDirectory) > 1:
            currentDirectory.pop()
            backwards = True
        else:
            if i == "":
                continue
            if getCD() in ["", "/"]:
                pathToSearch = i
            else:
                pathToSearch = getCD() + "/" + i
            if os.path.isfile(file(pathToSearch)):
                print("tmsh: cd: /%s: Not a directory" % file(pathToSearch))
                raise codeExit()
            if os.path.exists(file(pathToSearch)):
                currentDirectory.append(i)
                backwards = False
                if len(currentDirectory) == 2:
                    if currentDirectory[0] == "/":
                        currentDirectory[0] = ""
            else:
                print("tmsh: cd: /%s: No such file or directory" % file(pathToSearch))
                raise codeExit()
    try:
        if backwards:
            currentDirectory.append("")
    except:
        pass