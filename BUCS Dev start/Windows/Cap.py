from dictionary import buildCap
from tkinter import *
from tkinter import ttk

def deliver_cap():
    cap = buildCap()
    print(cap)
    answer = input('Enter the words above:')
    if answer == cap:
        exit()
    else:
        print('The device that was just plugged in may be a milicious device, or the words were typed incorrectly. Please ensure the device is what it\'s meant to be.')
        deliver_cap()

#rw = RandomWords()
deliver_cap()

