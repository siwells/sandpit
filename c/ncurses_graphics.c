#include <ncurses.h>

#define WORLD_WIDTH 50
#define WORLD_HEIGHT 20
 
int main(int argc, char *argv[]) {
 
    WINDOW *world;
    int offsetx, offsety;
 
    initscr();
    refresh();
 
    offsetx = (COLS - WORLD_WIDTH) / 2;
    offsety = (LINES - WORLD_HEIGHT) / 2;
 
    snakeys_world = newwin(WORLD_HEIGHT,
                           WORLD_WIDTH,
                           offsety,
                           offsetx);
 
    box(world, 0 , 0);
 
    wrefresh(world);
 
    getch();
 
    delwin(world);
 
    endwin();
 
    return 0;
 
}
