## What is BUCS

BUCS (Bad-Usb Challenge System) is a method to prevent or mitigate bad-usb damage to Windows systems. Currently BUCS is in early stages allowing it simply to step in the way of a bas-usb, but will eventually be able to fully stop attacks.

## Install Instructions 
### Requirements
1. python3
2. Windows 10 or newer

### Installation Instructions
### Step 1:
Download and install the appropriate python3 for your windows machine from `python.org/downloads/windows`

### Step 2:

Enable PNP auditing in the Windows Group Policy Editor under:
```
Computer Configuration \ Windows Settings \ Security Settings \ Advanced Audit Policy Configuration \ Detailed Tracking \ Audit PNP Activity
```
![Alt text](https://github.com/abladow/BAD-USB/blob/main/Documentation/Group%20policy%20config.png)\
Enable Success and Failure.

### Step 3: Download the 1.0_Pack.zip

https://github.com/abladow/BAD-USB/raw/main/Install/1.0_Pack.zip \
Unzip the contents
  

You are ready to make changes to the code without throwing dependency errors!

### Step 4: Configure Task scheduler
1. In task scheduler import the BUCS_Task.xml file:
```
  Actions -> Import Task
  ```
2. Navigate to where BUCS_Task.xml is downloaded and select it
3. Set the group or user for it to run with if you wish to change it from default (Administrators) by selecting Change User of Group
4. Select the Actions tab at the top to configure the actions
5. The default action is a place holder to open a command prompt. Select the action and choose edit to change it.
6. Under Program/Script browse to where the BUCS download is and choose the BUCS_Script.bat file
7. Under triggers is where the the delay can be edited, this is important to have proper interjection to the attack, default is 5 seconds. This may need to change for your system. To do this navigate to the triggers tab and select the trigger. Then select edit. There you can edit the delay.
8. Hit Ok on the task window and close task scheduler
### Step 5: Configure BUCS_Script.bat
1. Open the BUCS_Script.bat in a text editor of your choice.
2. On line 3 set the calue of the statements within the <> brackets
	1. The first <> statement will be the PATH to the python3 executable on your system
	2. The second <> statement will be the PATH to the Cap.py file
3. Save and close
### Getting started
If properly configured, when a HID device is plugged in to the system BUCS will activate
