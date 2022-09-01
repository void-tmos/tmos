try:
    user = args[0].lower()
except:
    user = username

userinfo = open(file("/etc/passwd"), "r").read().splitlines()
exist = False
for i in userinfo:
    if i.split(":")[0] == user:
        exist = True

if not exist:
    print("passwd: user '%s' does not exist" % user)
    raise forceExit("user does not exist")

if username != "root" and user != username:
    print("passwd: You may not view or modify password information for %s." % user)
    raise forceExit("no perms")
print("Changing password for %s."%user)
shadowinfo = open(file("/etc/shadow"), "r").readlines()
if username != "root":
    current = hashlib.sha256(getpass("Current password: ").encode()).hexdigest()
    correctpass = False
    for i in shadowinfo:
        if i in ["", " "]:
            continue
        info = i.split(":")
        if info[0].lower() == user:
            if libhash.passwd(current, info):
                correctpass = True
    if not correctpass:
        print("passwd: Password incorrect")
        raise forceExit("wrong password")

new = hashlib.sha256(getpass("New password: ").encode()).hexdigest()
retype = hashlib.sha256(getpass("Retype new password: ").encode()).hexdigest()
if new != retype:
    print("passwd: Passwords do not match")
info = "%s:$2$%s" % (user, hashlib.sha256(new.encode()).hexdigest())
for i in shadowinfo:
    if i in ["", " "]:
        continue
    if i.split(":")[0].lower() == user:
        usertochange = i
shadowinfo.remove(usertochange)
shadowinfo.append(info)
open(file("/etc/shadow"), "w").write("\n".join(shadowinfo))
print("passwd: Password updated successfully")