# Progress Report 4/10/2022
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


|Risk name (value)  | Impact     | Likelihood | (original) Description | Updated Value(IxL) and Description |
|-------------------|------------|------------|-------------|-------------|
|Security bypassed(36) | 6 | 6 | The security check that detects a new keyboard fails to detect or start. Mitigate this risk by researching a lower level method of finding new devices | 6x6=36 This remains a larger risk of the project, as with our current prototype security can be bypassed quite simply, however we are actively searching for methods to fix that. |
|Failure to unlock(28) | 7 | 4 | Even if check is passed the keyboard is not allowed to type. Accept this risk until further research is performed. | 7x1=7 We have went a different direction for the prototype instead of locking the keyboard. This has caused the likelihood to significantly decrease. |
|USB disable(18) | 9 | 2 | Through security policy or other USB ports become unusable. Mitigate this rish by using a VM or other system that allows us to flash it and restart. | 9x1=9 This risk was assesed whithout full knowledge of how we would need to interact with the system. Since then we have gained a better understanding of our programs intereaction. Therefore, we now know this should never happen. | 
|Lockout(24) | 8 | 3 | Our Utility stop any form of keyboard input. Accept this risk until further research is done.  | 8x1=8 Upon further research, we are not using a locking method, therefore this risk should not occur. |
|Project failure(30) | 10 | 3 | Failure to create a effective method to stop Bad USBs. Monitor this risk, and potentially shift project focus if our idea cannot be completed.  | 10x2=20 This risk remains present, but due to our finding a prototype that has so far been effective the likelihood has decreased. | 
| Lack of knowledge of windows hardware stack(28) | 4 | 7 | Our team lacks proper knowledge about the windows hardware stack which makes it more difficult to gauge if our idea will work at a higher level. Mitigate this risk by researching and gaining a better understanding of how the windows hardware stack operates. | 4x4=16 This risk has decreased significantly since the onset of this project. This is due to our research and effort to better understand the Windows hardware stack. | 
| Python not low enough of a language (24)| 4 | 6 | Python is not a low level language which could cause issues with our program not performing the way we expect computationally or speed wise. We will accept this risk by understanding that we may need to move to C to complete the program. | 4x2=8 This risk has almost been eliminated, as our greatest concern with this risk was that device detection would not be possible. We have since found alternative ways baked into Windows to acheive device detection. |
| Administration level not reached in Python (45)| 9 | 5 | Unable to get the permissions on Windows to keep the program alive. Accept this risk until further research is done. | 6x3=18 This risk has decreased in likelihood and impact since the beginning of this project, as we have been able to succesfully stop an attack by using our prototype that does not require an elevated administration level. Additionally, we have found methids in Python to gain higher administration levels. |
