class libmotd:
    def printmotd(user):
        userinfo = open(file("/etc/motd/users"), "r").readlines()
        for i in userinfo:
            info = i.split(":")
            if info[0] == user:
                if info[1] == "y":
                    for i in info[2]:
                        if i == "g":
                            print(open(file("/etc/motd/motd"), "r").read())
                        if i == "t":
                            print("Tip:", random.choice(open(file("/etc/tips"), "r").read().splitlines()))
                        if i == "c":
                            print(open(file("%s/.motd" % gethome(user)), "r").read())