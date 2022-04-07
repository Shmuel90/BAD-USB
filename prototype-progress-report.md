# Progress Report (insert date here)
## Overview
(insert brief overview of efforts made)
To this point in the project, we have been able to advance in an event based detection for PNP devices in Windows. Additionally we have advanced efforts in creating scripts that leverages our intended defense mechanism and test cases to use them against. We have had our first successful interjection into the BadUSBs attempt to deliver its payload. 

## Outcomes
(brief overview of outcomes - what did you achieve?)
So far in this project we have been able to achieve a fully working prototype that was able to stop a sample BadUSB attack that we created.  
also list them out like this:
* Began work on Windows and Linux programs as intro prototypes to the final product - BAD-USB/BUCS Dev start/Windows/Obsolete & BAD-USB/BUCS Dev start/Linux
* Obtained event based detection in Windows - BAD-USB/BUCS Dev start/Windows/hid_test.xml 
* Crafted a number of BadUSB attacks to leverage against our BUCS - BAD-USB/BadUSB scripts/
* Created a script that applies out intended defense mechanism - BAD-USB/BUCS Dev start/Windows/myscript.bat & /Cap.py
* Began work on GUI - BAD-USB/BUCS Dev start/Windows/BUCS_GUI_FRAME.py

## Hinderances
(insert brief discussion of challenges encountered)
Our proficiency and knowledge about Windows behaviour when it comes to PNP and HID devices has been our largest hinderence. The way that Windows handles HID devices is a very low level process in the drivers, which led to confusion and a large need to learn as much as possible about different ways the devices interact. Additionally generating an event based program gave us difficulty as there is no events that relate to HID devices by default. Fortunatley, after a lot of digging we were able to find an advanced audit policy that would tie HID devices to an event.

## Ongoing Risks
(address your project risks identified from Milestone 1 and update them based on your current progress, this should be a table)
