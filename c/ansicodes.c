#include <stdio.h>
#include <unistd.h>

#define BLACK       30
#define RED         31
#define GREEN       32
#define YELLOW      33
#define BLUE        34
#define MAGENTA     35
#define CYAN        36
#define WHITE       37
#define B_BLACK     90
#define B_RED       91
#define B_GREEN     92
#define B_YELLOW    93
#define B_BLUE      94
#define B_MAGENTA   95
#define B_CYAN      96
#define B_WHITE     97

void alert(void);
void colour_text(int);
void pause_for_input(void);
void reset_terminal(void);

int main(void)
{
    char daka [4][4];
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            daka[i][i] = 'x';
        }
    }

    printf("\x1b[2J \n");
    printf("\x1b[H");
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            printf("%c", daka[i][i]);
        }
        printf("\n");
    }
    
    colour_text(B_RED);
    pause_for_input();
    alert();
    pause_for_input();

    reset_terminal();
    

//    printf("\x1b[H");  //cursor to home position
/*    for (int j = 0; j < screen_height; j++) 
    {
        for (int i = 0; i < screen_width; i++) 
        {
            putchar(output[i,j]);
        }
        putchar('\n');
    }*/
    return 0;
}

void colour_text(int colour)
{
    printf("\x1b[%dm HELLO", colour);
}


void pause_for_input(void)
{
    printf("Press <ENTER> to continue");
    int tmp = getchar();
}

void reset_terminal(void)
{
    printf("\033c");
}

void alert(void)
{ 
    printf("\033[?5h INVERT\n");
    sleep(1);
    printf("\033[?5l RESET\n");
}
