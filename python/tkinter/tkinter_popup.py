#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this program, we create
a popup menu. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

from Tkinter import Tk, Frame, Menu



class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Popup menu")
        self.menu = Menu(self.parent, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell())
        self.menu.add_command(label="Exit", command=self.onExit)

        self.parent.bind("<Button-2>", self.showMenu)
        self.pack()
        
        
    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)
       

    def onExit(self):
        self.quit()


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  