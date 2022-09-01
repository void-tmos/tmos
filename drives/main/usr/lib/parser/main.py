class Parser:
    def __init__(self):
        self.commands = []
    def addCmd(self, short, extended, key, opt=False):
        try:
            if short[0] == "-":
                short = short[1:]
        except Exception:
            pass
        self.commands.append((short, extended, key, opt))
    def parse(self, args):
        self.output = {}
        self.args = args
        for i in self.commands:
            try:
                self.output[i[2]]
            except KeyError:
                if i[3]:
                    self.output[i[2]] = None
                else:
                    self.output[i[2]] = False
        try:
            args[0][0]
        except Exception:
            return
        for i in args:
            if i[0] == "-":
                if i[1] == "-":
                    cmd = i[2:]
                    foundArg = False
                    for j in self.commands:
                        if j[1] == "--%s"%cmd:
                            if j[3]:
                                try:
                                    self.output[j[2]] = args[args.index(i)+1]
                                except IndexError:
                                    print("Parsing Error: --%s requires an argument, but was given none" % cmd)
                            else:
                                self.output[j[2]] = True
                            foundArg = True
                    if not foundArg:
                        print("error: unrecognised option '%s'" % (i))
                        raise codeExit()
                else:
                    for j in i[1:]:
                        foundArg = False
                        for k in self.commands:
                            if j == k[0]:
                                if k[3]:
                                    try:
                                        self.output[k[2]] = args[args.index(i)+1]
                                    except IndexError:
                                        print("Parsing Error: -%s requires an argument, but was given none" % j)
                                else:
                                    self.output[k[2]] = True
                                foundArg = True
                        if not foundArg:
                            print("error: unrecognised option '-%s'" % (j))
                            raise codeExit()
                self.args.remove(i)