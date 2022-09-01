while True:
    try:
        command = input("/1984:§ ")
    except KeyboardInterrupt:
        print("^C")
    except EOFError:
        print("^D")
    print("no")