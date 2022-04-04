# Progress Report (insert date here)
## Overview
(insert brief overview of efforts made)
To this point in the project, we have been able to advance in an event based detection for PNP devices in both Windows and Linux. Additionally we have created a number of BadUSB attacks that we are using for testing against BUCS.

## Outcomes
(brief overview of outcomes - what did you achieve?)

also list them out like this:
* outcome 1
* outcome 2

## Hinderances
(insert brief discussion of challenges encountered)
Our proficiency and knowledge about Windows behaviour when it comes to PNP and HID devices has been our largest hinderence. The way that Windows handles HID devices is a very low level process in the drivers, which led to confusion and a large need to learn as much as possible about different ways the devices interact. Additionally generating an event based program gave us difficulty as there is no events that relate to HID devices by default. Fortunatley, after a lot of digging we were able to find an advanced audit policy that would tie HID devices to an event. 

## Ongoing Risks
(address your project risks identified from Milestone 1 and update them based on your current progress, this should be a table)
