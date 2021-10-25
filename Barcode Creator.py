#Created by Cyrus Baybay
#November 22, 2020
#Open Source 


#==========================================================================================
#==========================================================================================
#==================================Begin code area=========================================
#==========================================================================================
#==========================================================================================

#### import libraries
from tkinter import *
def getLegend(c):                             # covert character to Code39 legend
 legend = "";
 switch = {
  '0': "bwbWBwBwb",
  '1': "BwbWbwbwB",
  '2': "bwBWbwbwB",
  '3': "BwBWbwbwb",
  '4': "bwbWBwbwB",
  '5': "BwbWBwbwb",
  '6': "bwBWBwbwb",
  '7': "bwbWbwBwB",
  '8': "BwbWbwBwb",
  '9': "bwBWbwBwb",
  'A': "BwbwbWbwB",
  'B': "bwBwbWbwB",
  'C': "BwBwbWbwb",
  'D': "bwbwBWbwB",
  'E': "BwbwBWbwb",
  'F': "bwBwBWbwb",
  'G': "bwbwbWBwB",
  'H': "BwbwbWBwb",
  'I': "bwBwbWBwb",
  'J': "bwbwBWBwb",
  'K': "BwbwbwbWB",
  'L': "bwBwbwbWB",
  'M': "BwBwbwbWb",
  'N': "bwbwBwbWB",
  'O': "BwbwBwbWb",
  'P': "bwBwBwbWb",
  'Q': "bwbwbwBWB",
  'R': "BwbwbwBWb",
  'S': "bwBwbwBWb",
  'T': "bwbwBwBWb",
  'U': "BWbwbwbwB",
  'V': "bWBwbwbwB",
  'W': "BWBwbwbwb",
  'X': "bWbwBwbwB",
  'Y': "BWbwBwbwb",
  'Z': "bWBwBwbwb",
  '-': "bWbwbwBwB",
  '.': "BWbwbwBwb",
  ' ': "bWBwbwBwb",                         #(space) not empty
  '$': "bWbWbWbwb",
  '/': "bWbWbwbWb",
  '+': "bWbwbWbWb",
  '%': "bwbWbWbWb",
  '*': "bWbwBwBwb"
 }
 return switch[c]
#####                                       draw rectangles as bars
def drawBars(c, x):
 w=0
 clr=""
 if c=='b':
  clr="#000000"
  w=2
 elif c=='B':
  clr="#000000"
  w=4
 elif c=='w':
  clr="#ffffff"
  w=2
 elif c=='W':
  clr="#ffffff"
  w=4

 canvas1.create_rectangle(x, 0, x+w, 100, fill=clr, width=0) # width=0 no border
 x+=w
 return x
###                               get user entry and try to convert to barcode legend
def getText():
 canvas1.delete("all")          # clear the current drawing if nay
 s = entry1.get()               # get the user entry
 s=s.upper()                    # convert to uppercase
 s = "*" + s + "*"              # Code39 format: *data*
 result="bW"                    # Code39 uses "bW" as starting character
 for i in s:
  result += getLegend(i) + "w"  # Code39 use "w" as delimiter
 x=0
 for c in result:
  x=drawBars(c, x)
#                                 display the text in label2
 label2['text'] = s
#                                 reset the width of Canvas
 canvas1['width'] = x
#                                 draw a blank rectangle as background of text
 canvas1.create_rectangle(30, 0, x-30, 20, fill="white", width=0) # no border
#                                 draw text
 canvas1.create_text(x/2, 10, fill="black", font="courier 12", text=s)

 
#### create GUI
root = Tk()
root.title("Barcode Creater")
label1 = Label(root, text="Enter a string: ")                 ## caption
label1.grid(row=0, column=0)
entry1 = Entry(root, width=30)                                ## user input
entry1.grid(row=0, column=1)
button1 = Button(root, text='Convert', command=getText)
button1.grid(row=0, column=2)
label2 = Label(root, height=1, text="")                       ## display output
label2.grid(row=1, columnspan=3)
# create a Canvas for drawing
canvas1 = Canvas(root, width=0, height=100)                   ## set original width=0
canvas1.grid(row=2, columnspan=3)
root.mainloop()

#==========================================================================================
#=========================================End==============================================
#==========================================================================================
