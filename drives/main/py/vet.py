import curses

global inputfile
if args:
    run("getdir -efo '%s' '%s'"%(args[0], getCD()))
    inputfile = open(file("/".join(directory)), "r").readlines()
else:
    inputfile = None

def main(stdscr):
    global text, cols, save
    import curses
    stdscr.clear()
    lines = curses.LINES
    cols = curses.COLS
    cl = 0
    cc = 0
    text = []
    for i in range(1, lines):
        text.append([" " for i in range(0,cols)])
    for i in range(0, cols):
        stdscr.addstr(0, i, " ", curses.A_REVERSE)
    stdscr.refresh()
    if inputfile:
        stdscr.move(1, 0)
        for i in inputfile:
            for j in i:
                stdscr.addstr(j)
                if j == "\n":
                    cl += 1
                    cc = 0
                else:
                    text[cl][cc] = j
                    cc += 1
        stdscr.move(1, 0)
        cl, cc = 0, 0
    while True:
        try:
            c = stdscr.getch()
        except:
            continue
        if c in [8, 263]:
            if cc == 0:
                continue
            text[cl][cc-1] = " "
            cursor = stdscr.getyx()
            stdscr.move(cursor[0], cursor[1]-1)
            stdscr.addstr(" ")
            cursor = stdscr.getyx()
            stdscr.move(cursor[0], cursor[1]-1)
            cc -= 1
        elif c in [259]: #up
            cursor = stdscr.getyx()
            if cursor[0] > 1:
                stdscr.move(cursor[0]-1, cursor[1])
                cl -= 1
        elif c in [258]: #down
            cursor = stdscr.getyx()
            if cursor[0] < cols:
                stdscr.move(cursor[0]+1, cursor[1])
                cl += 1
        elif c in [260]: #left
            cursor = stdscr.getyx()
            if cursor[1] > 0:
                stdscr.move(cursor[0], cursor[1]-1)
                cc -= 1
        elif c in [261]: #right
            cursor = stdscr.getyx()
            if cursor[1] < lines:
                stdscr.move(cursor[0], cursor[1]+1)
                cc += 1
        elif c in [27, -1]:
            cursor = stdscr.getyx()
            stdscr.move(0, 0)
            stdscr.addstr("Would you like to save y/n? ")
            c = stdscr.getch()
            save = chr(c)
            break
        elif c in [10]:
            cl += 1
            cc = 0
            stdscr.addstr(chr(c))
        else:
            if cc >= cols-1:
                pass
            else:
                stdscr.addstr(chr(c))
                text[cl][cc] = chr(c)
                cc += 1

curses.wrapper(main)
for i in reversed(text):
    if i == [" " for i in range(0,cols)]:
        text.pop()
    else:
        break
finaltext = []
for i in text:
    for j in reversed(i):
        if j == " ":
            i = i[:-1]
        else:
            break
    finaltext.append("".join(i))

if inputfile != None:
    if save in ["y", "Y"]:
        f = open(file("/".join(directory)), "w")
        f.write("\n".join(finaltext))
        f.close()
else:
    print("\n".join(finaltext))