try:
    user = args[0].lower()
except:
    user = input("Username? ").lower()

allusers = open(file("/etc/passwd"), "r").read().splitlines()
for i in allusers:
    if i[0] == user:
        print("useradd: user '%s' already exists")
        raise forceExit("user already exists")
ids = []
for i in allusers:
    ids.append(int(i.split(":")[2]))
uid = gid = max(ids)+1
userinfo = "%s:x:%d:%d:%s:/home/%s:/py/tmsh.py" % (user, uid, gid, user, user)
shadowinfo = "%s:$2$8c81f50542a4a9017f127a200418ee1db88846c29735e4484dd6c15e6f1c99a8" % user
open(file("/etc/passwd"), "a").write("\n%s"%userinfo)
open(file("/etc/shadow"), "a").write("\n%s"%shadowinfo)
run("mkdir /home/%s"%user)
del user, allusers, ids, uid, gid, userinfo, shadowinfo
