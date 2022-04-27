from random_word import RandomWords
from tkinter import *
from tkinter import ttk
		
rw = RandomWords()
#init tkint
gui = Tk()

def keyValidate(event=None):
   global entrybox
   string= entrybox.get()
   if string == cap:
      exit()
   else:
      problem.configure(text='The device that was just plugged in may be a malicious device, or the words were typed incorrectly. Please ensure the device is what it\'s meant to be.')

# set fwindow features
gui.wm_title("BUCS Check")
gui.geometry("400x150")
topFrame = Frame(gui)
topFrame.pack(side=TOP)

bottomFrame=Frame(gui)
bottomFrame.pack(side=BOTTOM)

#create random words
cap = rw.get_random_word(maxLength=6)+' '+rw.get_random_word(maxLength=6)+' '+rw.get_random_word(maxLength=6)

#set window contents
label1=Label(topFrame, text=cap, font="Arial 16 bold")
label1.pack(side=TOP)

label2=Label(topFrame, text="Enter the words above:", font="Arial")
label2.pack(side=LEFT)

entrybox=Entry(topFrame, bd=2, bg="white", text="Enter Here", width=30,font="Arial")
entrybox.focus_set()
entrybox.pack(side=RIGHT)

problem=Label(bottomFrame,text="", fg='#ff0000', wraplength=380, justify=LEFT)
problem.pack(side=BOTTOM)

button=Button(bottomFrame, text="Check", command=keyValidate, font="Arial")
gui.bind("<Return>", keyValidate)
button.pack(side=TOP)


#display

gui.mainloop()
