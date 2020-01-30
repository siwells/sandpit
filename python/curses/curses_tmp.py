import curses

screen = curses.initscr()
screen.addstr("Press any key...")
screen.refresh()

pad = curses.newpad(100, 100)
for y in range(0, 99):
    for x in range(0, 99):
        pad.addch(y, x, ord('a') + (x) % 26)

pad.refresh(0,0, 5,5, 20,75)

c = ''
while(113 != c):
    c = screen.getch()

curses.endwin()    
print("QUIT on Q")


