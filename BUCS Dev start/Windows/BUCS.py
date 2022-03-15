import time
import sys
import pywinusb.hid as hid
from random_words import RandomWords # build captcha
#import win32gui


#enumerate windows function
"""
def enum_callback(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
"""
#enumerate HID devices function
def enum_devs():
    return set([item for item in hid.core.find_all_hid_devices()])
#look for new or removed devices
def enum(hidlist):
    global check
    devs = enum_devs()
    dif = hidlist.difference_update(devs)
    #removed = hidlist.difference(devs)
    if sys.getsizeof(dif) > 16:
        check = True
        print('added: {}')
    #if removed:
        #print('removed: {}')
    return devs

#captcha function - recursive
def deliver_cap():
    cap = rw.random_word()+' '+rw.random_word()+' '+rw.random_word()
    print(cap)
    answer = input('Enter the words above:')
    if answer == cap:
        return True
    else:
        print('The device that was just plugged in may be a milicious device, or the words were typed incorrectly. Please ensure the device is what it\'s meant to be.')
        deliver_cap()
          
# Main loop setup 
rw = RandomWords() # Init random word
hidlist = enum_devs() #Initial enumeration upon start
#TODO: Add something to check keyboards
while True:
    check = False
    hidlist = enum(hidlist)
    if bool(check):
        #TODO:figure out best way to focus window  - tkinter maybe
        """
        #generate some arrays to hold window info
        toplist = []
        winlist = []
        #enumerate window list and focus on the CMD prompt
        win32gui.EnumWindows(enum_callback, toplist)
        cmd = [(hwnd, title) for hwnd, title in winlist if 'command' in title.lower()]
        # just grab the first window that matches
        cmd = cmd[0]
        # use the window handle to set focus
        win32gui.SetForegroundWindow(cmd[0])
        """
        # send in the captcha
        deliver_cap()
    time.sleep(0.5)






