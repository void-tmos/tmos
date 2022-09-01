while True:
    correctpass = False
    hostname = open(file("/etc/hostname"), "r").read()
    username = input("%s login: " % hostname).lower()
    password = hashlib.sha256(getpass("Password: ").encode()).hexdigest()
    
    etcpasswd = open(file("/etc/passwd"), "r").readlines()
    etcshadow = open(file("/etc/shadow"), "r").readlines()
    for i in etcpasswd:
        if i in ["", " "]:
            continue
        userinfo = i.split(":")
        if userinfo[0].lower() == username:
            for i in etcshadow:
                if i in ["", " "]:
                    continue
                shadowinfo = i.split(":")
                if shadowinfo[0].lower() == username:
                    if libhash.passwd(password, shadowinfo):
                        correctpass = True
                    else:
                        print("Password Incorrect")
    if correctpass:
        break

del correctpass, hostname, password, etcpasswd, etcshadow, userinfo, shadowinfo
