import sys
import pywinusb.hid as hid
import time

def enum_devs():
    return set([item for item in hid.core.find_all_hid_devices()])

def enum(hidlist):
    devs = enum_devs()
    dif = hidlist.difference_update(devs)
    #removed = hidlist.difference(devs)
    if sys.getsizeof(dif) > 16:
        print('added: {}')
    #if removed:
        #print('removed: {}')
    
    return devs

if __name__ == '__main__':
    if sys.version_info < (3,):
        import codecs
        output = codecs.getwriter('mbcs')(sys.stdout)
    else:
        # python3, you have to deal with encodings, try redirecting to any file
        output = sys.stdout
    try:
        hidlist = enum_devs()
    except UnicodeEncodeError:
        print("\nError: Can't manage encodings on terminal, try to run the script on PyScripter or IDLE")
    while True:
        hidlist = enum(hidlist)
        time.sleep(.5)
