#!/usr/bin/env python3

import subprocess as sp
from random_words import RandomWords

def deliver_cap():
    cap = rw.random_word()+' '+rw.random_word()+' '+rw.random_word()
    print(cap)
    answer = input('Enter the words above:')
    if answer == cap:
        return True
    else:
        print('The device that was just plugged in may be a milicious device, or the words were typed incorrectly. Please ensure the device is what it\'s meant to be.')
        deliver_cap()

rw = RandomWords()

sp.run(['bash', '-li'])
deliver_cap()
