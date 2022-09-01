class libhash:
    def passwd(inp, shadow):
        passwdinfo = shadow[1].split("$")
        if passwdinfo[1] == "0":
            if inp == passwdinfo[2].split()[0]:
                return True
        if passwdinfo[1] == "2":
            if passwdinfo[2].split()[0] == hashlib.sha256(inp.encode()).hexdigest():
                return True
        return False