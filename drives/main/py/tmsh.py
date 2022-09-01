if len(args) != 0:
    script = open(file(args[0]), "r").read().splitlines()

libmotd.printmotd(username)
while True:
    try:
        command = input("%s:§ "%getCD()) #get command from input
    except KeyboardInterrupt:
        command = ""
        print("^C")
    except EOFError:
        print("^D")
        break
    if command == "exit":
        break
    try:
        run(command) #run it
    except forceExit:
        pass
    if commandRun: #if it was run, 
        pass #do nothing
    else: #if it wasnt run,
        print("tmsh: command not found: %s"%command[0]) #error msg