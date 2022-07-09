""" Project Matchmaker
nested loops (2D array)
lambda function
"""
import random, time
from tkinter import Tk, Button, DISABLED, messagebox
#DISABLED stops a button from responding after its symbol has been matched

def show_symbol(x,y):
    global first #cal on the variables outside of function
    global previousX, previousY

    buttons[x,y]['text'] = button_symbols[x,y]
    print(buttons[x,y]['text']) #the button object contains the characterstic (text=) so it can be called this way Button(text='unicode',etc)
    buttons[x,y].update_idletasks() #proccesses events that are currently not running
    if first: #if its the first turn
        previousY = y
        previousX = x
        first = False #it is no longer the first turn
    elif previousX!=x or previousY!=y: #second turn (first is false)
        if buttons[previousX,previousY]['text']!=buttons[x,y]['text']: #if the symbols do not match
            time.sleep(0.5)
            buttons[previousX,previousY]['text'] = ''  #make the button blank. It will show the symbol again when the function is called ( see line 13)
            buttons[x,y]['text']=''
        else:  #if the symbols do match
            buttons[previousX,previousY]['command']=DISABLED #disable matching buttons so player can't press them again
            buttons[x,y]['command'] = DISABLED
        first = True

root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False) #prevents resizing of the window

buttons = {}
first = True
previousX=0 ## these two variables are going to keeep track of the previous button pressed
previousY=0

button_symbols={} #the symbol for each button is stored in this dictionary
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']  #unicode character

"""
A Unicode string is a sequence of code points, which are numbers from 0 to 0x10FFFF. -> encdoed to a sequence of bytes
  P           y           t           h           o           n
0x50 00 00 00 79 00 00 00 74 00 00 00 68 00 00 00 6f 00 00 00 6e 00 00 00
   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
"""

random.shuffle(symbols) #shuffle the symbols

#build the grid. Our grid is a 2 dimensional list -> nested loop (a loop within a loop)
for x in range (6): #range is from 0->5
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x,y), width=3,height=3) #BUTTON(command-function or method to be called when the button is clicked)
        button.grid(column=x,row=y) #button is placed on the GUI
        buttons[x,y] = button #saves each button in the button dictionary
        #the key is a coordiante pair (x,y) and the corresponding value is the button object itself
         #{(0, 0): <tkinter.Button object .!button>} <--item that is added into dictionary looks like this
        button_symbols[x,y]=symbols.pop() #remove the last item in the symbols list and add it to this dictionary as the value
         #{(0, 0): '✅'}



root.mainloop()

