import tkinter
import tkinter.filedialog

root = tkinter.Tk()
def openFileName():
  return tkinter.filedialog.askopenfilename(parent=root,title='Choose a file',filetypes=[('pars pl','.psl')])
#
str1=openFileName()
if str1 =='': exit()
file=open(str1,encoding='utf-8')
if file != None:
    data = file.read()
    file.close()
    print("I got %d bytes from this file." % len(data))

root = tkinter.Tk()
S = tkinter.Scrollbar(root)
T = tkinter.Text(root, height=30, width=100)
n=0
def EscapeKeyPress(event):
  exit()
def EnterKeyPress(event):
  print('sdfsdaaaaaaaaaa')
  T.insert(tkinter.END, '\n')
  T.insert(tkinter.END, T.get(str(float(7)),tkinter.END))
  #n+=1
def Contents():
  print('sfds')      

btn1 = tkinter.Button(root, text = "Sنتانتاhow contents", command = Contents)
btn1.pack(side = tkinter.LEFT, padx = 20)
T.bind("<Escape>", EscapeKeyPress)
T.bind("<Return>", EnterKeyPress)
S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
T.pack(side=tkinter.RIGHT, fill=tkinter.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """ بیلبی بیلیs
یبلییل
یبلon
 to be wished."""
n=len(quote)
T.insert(tkinter.END, quote)
quote="""
یسنبت
یکی دوتا
سه بتا
"""

T.insert(tkinter.END, quote)
n+=len(quote)
T.focus_set()
tkinter.mainloop()


#http://www.python-course.eu/tkinter_text_widget.php
#from tkinter import *
#http://fossies.org/dox/Python-3.3.0/namespacetkinter_1_1filedialog.html#a3528c1f3f8c761181b16fb958620d5b5
#http://docs.pythonsprints.com/python3_porting/py-porting.html
#http://pythonhosted.org/six/
#http://python3porting.com/stdlib.html
#http://14mb.de/u/ralubenow/tkinter.html#12
#http://etutorials.org/Programming/Python+tutorial/Part+III+Python+Library+and+Extension+Modules/Chapter+16.+Tkinter+GUIs/16.6+The+Text+Widget/
'''
t.get(i[,j])	


t.get(i) returns t's character at index i. t.get(i,j) returns a string made up of all characters from index i to index j, included.

'''
