parser = Parser()
parser.addCmd("-S", "--sync", "sync")
parser.addCmd("-u", "--update", "update")
parser.parse(args)
args = parser.args
opts = parser.output

run("mkdir -p /tmp")

if opts["sync"]:
    allRepos = open(file("/etc/nebps/repo.list", "w")).read().splitlines()
    for i in allRepos:
        print("[*] Updating Repository '%s'"%i)
        try:
            r = requests.get(i, allow_redirects=True)
        except Exception as e:
            print("ERROR: "+str(e))
            raise forceExit(e)
        allDirs = i.split("/")
        open(file("/etc/nebps/repos/"+allDirs[-1]), "wb").write(r.content)

global allPkgs
allPkgs = []
files = os.listdir(file("/etc/nebps/repos"))
for i in files:
    if i[-5:] == ".repo":
        items = ast.literal_eval(open(file("/etc/nebps/repos/"+i), "r").read())
        for i in items:
            allPkgs.append(i)

installed = ast.literal_eval(open(file("/etc/nebps/installed.conf"), "r").read())

def isinstalled(pkg, installed):
    return next((item for item in installed if item["name"] == pkg), None)
def find(pkg):
    package = next((item for item in allPkgs if item["name"] == pkg), None)
    if package == None:
        print("Package '%s' not found in repository pool." % pkg)
        return None
    else:
        return package

toInstall = []
dependancies = []
for i in args:
    pkg = find(i)
    if pkg != None:
        installedPkg = isinstalled(pkg["name"], installed)
        if installedPkg != None:
            if pkg["version"] >= installedPkg["version"]:
                toInstall.append(("update", pkg, installedPkg))
            else:
                print("Package `%s` already installed." % pkg["name"])
            continue
        if not pkg in toInstall:
            toInstall.append(("install", pkg))

while True:
    origlen = len(toInstall)
    for i in toInstall:
        for j in i[1]["dependancies"]:
            pkg = find(j)
            if pkg:
                if not pkg in toInstall:
                    toInstall.append(("install", pkg))
    newlen = len(toInstall)
    if origlen == newlen:
        break

if not toInstall:
    raise forceExit()

toInstall.reverse()

print ("{:<12} {:<9} {:<15} {:<15} {:<15}".format('Name','Action','Version','New version', 'Download size')) # https://www.educba.com/python-print-table/
for i in toInstall:
    print("{:<12} {:<9} {:<15} {:<15} {:<15}".format(i[1]["name"], i[0], i[2]["version"] if i[0]=="update" else "-", i[1]["version"], "69KB"))

print("""
Size to download:         69MB
Size required on disk:    69MB
Space available on disk: 420MB
""")

yn = input("Do you want to continue? [Y/n] ")
if yn != "y":
    print("Aborting!")
    raise forceExit

def md5(fname): #https://stackoverflow.com/users/370483/quantumsoup
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

print("\n[*] Collecting package files")
for i in toInstall:
    print(i[1]["name"]+'-'+i[1]["version"]+': collecting files...')
    try:
        r = requests.get(i[1]["location"]+"/%s.tar.xz"%i[1]["version"], allow_redirects=True)
    except Exception as e:
        print("ERROR: "+str(e))
        raise forceExit(e)
    run("mkdir -p /tmp/%s"%i[1]["name"])
    open(file("/tmp/%s/%s.tar.xz" % (i[1]["name"], i[1]["version"])), "wb").write(r.content)

print("\n[*] Verifying package integrity")
for i in toInstall:
    print(i[1]["name"]+'-'+i[1]["version"]+': verifying RSA signature...')
    try:
        r = requests.get(i[1]["location"]+"/%s.tar.xz.md5"%i[1]["version"], allow_redirects=True)
    except Exception as e:
        print("ERROR: "+str(e))
        raise forceExit(e)
    run("mkdir -p /tmp/%s"%i[1]["name"])
    open(file("/tmp/%s/%s.tar.xz.md5" % (i[1]["name"], i[1]["version"])), "wb").write(r.content)
    sig = md5(file("/tmp/%s/%s.tar.xz" % (i[1]["name"], i[1]["version"])))
    if sig != open(file("/tmp/%s/%s.tar.xz.md5" % (i[1]["name"], i[1]["version"])), "r").read().strip():
        #print(sig)
        #print(open(file("/tmp/%s/%s.tar.xz.md5" % (i["name"], i["version"])), "r").read().strip())
        print("failiure")
        raise forceExit()

print("\n[*] Unpacking packages")
for i in toInstall:
    print(i[1]["name"]+'-'+i[1]["version"]+': unpacking...')
    try:
        tar = tarfile.open(file("/tmp/%s/%s.tar.xz") % (i[1]["name"], i[1]["version"]))
        tar.extractall(path=file("/tmp/%s"%i[1]["name"]), numeric_owner=True)
        tar.close()
    except Exception as e:
        print("ERROR: "+str(e))
        raise forceExit()

print("\n[*] Installing unpacked packages")
for pkg in toInstall:
    print(pkg[1]["name"]+'-'+pkg[1]["version"]+': installing...')
    exec(open(file("/tmp/%s/install.py"%pkg[1]["name"]), "r").read())
    print(pkg[1]["name"]+'-'+pkg[1]["version"]+': installed successfully.')

for i in toInstall:
    if i[0] == "install":
        installed.append(i)
    elif i[0] == "update":
        installed.remove(i[2])
        installed.append(i[1])

open(file("/etc/nebps/installed.conf"), "w").write(str(installed))

#-----CLEAN-UP-----
for i in toInstall:
    run("rm -rf /tmp/%s"%i[1]["name"])

print("\n%d downloaded, %d installed, %d updated, %d configured, %d removed" % (len(toInstall), len(toInstall), 0, len(toInstall), 0))
