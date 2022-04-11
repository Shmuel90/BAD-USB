# BUCS (BADUSB Challenge System)

# Executive Project Summary
## Problem Statement
Users need an easy way to input data to a computer. This led to the creation of devices such as mice and keyboards to allow users to achieve that goal. Throughout the years, technology of mice and keyboards alike grew, and we now have created USB and HID to assist in creating easy input methods for users.
The issue with HID is that it is an innately trusted device for operating systems. While there is no issue with innately trusting a keyboard, there is a problem with trusting a device that can masquerade as a keyboard. In 2014 the power of devices known generically as BadUSBs was demonstrated at Defcon. These devices can pretend to be a keyboard and automatically input malicious commands upon plug in. The user is powerless to stop the USB after they plug the device into their machine since the takeover occurs in an incredibly short amount of time. This project seeks to create a small amount of required human interaction in the device handshake to mitigate the threat from a BadUSB.

## Project Goals 
1. Determine optimal programming language
2. Build prototype of BUCS
3. Test prototype of BUCS
4. If an effective countermeasure is created, package for delivery via package handlers like apt, rpm, windows installer, OSX.
5. If found ineffective research what other options there are to develop a product for Windows

These goals are the overall goals of the project. The specifics of how they will be accomplished are to be discussed later in this plan, but our project can be expressed in these four main goals. 

## Merit
This project can potentially save companies from headaches in the future. There is no current ethical issue with developing an application to assist in the protection of a computer, and while there are currently mitigations in place to protect against BadUSB attacks, this will introduce a full protection against it. 

# Proposed Timeline
![image](https://user-images.githubusercontent.com/56526625/153780252-0ad2a31a-c621-440e-b48a-008838362a42.png)

# Risk List

|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
|Security bypassed(36) | 6 | 6 | The security check that detects a new keyboard fails to detect or start. Mitigate this risk by researching a lower level method of finding new devices |
|Failure to unlock(28) | 7 | 4 | Even if check is passed the keyboard is not allowed to type. Accept this risk until further research is performed.  |
|USB disable(18) | 9 | 2 | Through security policy or other USB ports become unusable. Mitigate this rish by using a VM or other system that allows us to flash it and restart. |
|Lockout(24) | 8 | 3 | Our Utility stop any form of keyboard input. Accept this risk until further research is done.  |
|Project failure(30) | 10 | 3 | Failure to create a effective method to stop Bad USBs. Monitor this risk, and potentially shift project focus if our idea cannot be completed.  |
| Lack of knowledge of windows hardware stack(28) | 4 | 7 | Our team lacks proper knowledge about the windows hardware stack which makes it more difficult to gauge if our idea will work at a higher level. Mitigate this risk by researching and gaining a better understanding of how the windows hardware stack operates. | 
| Python not low enough of a language (24)| 4 | 6 | Python is not a low level language which could cause issues with our program not performing the way we expect computationally or speed wise. We will accept this risk by understanding that we may need to move to C to complete the program. |
| Administration level not reached in Python (45)| 9 | 5 | Unable to get the permissions on Windows to keep the program alive. Accept this risk until further research is done. | 

# Project Methodology

## Literature Review
https://github.com/abladow/BAD-USB/blob/main/LitReview.md

## Technical Plan

### Develop BUCS (BadUSB Challenge System) Prototype
- Goal 1:  Determine programming language required for optimal program functionality
	
	- Sub Objective 1: Determine if Python optimal
	- Sub Objective 2: Determine if C optimal 

- Goal 2: Program the detection of USB keyboard devices.

	- Sub objective 1: We will begin by researching ways to interact with device manager and enumerate devices connected to the PC.

- Goal 3: Program the ability for the program to lockout input from a peripheral device

	- Sub objective 1: We still begin researching the optimal way to lock-out a USB device for inputting information into the main system outside of the check without authorization.

- Goal 4: Program the ability for the program to unlock input from a peripheral device

	- Sub objective 1: We still begin researching the best way to undo the lock-out of a USB device for inputting information into the main system.
***
### Test BUCS Prototype
- Goal 1: Test with just detection
	
	- Sub Objective 1: Test the effectiveness of plugging in a new keyboard while running BUCS with the expected outcome of succesful detection multiple times with multiple devices to ensure good coverage

	- Sub Objective 2: Test the effectiveness of plugging in a bad USB device while running BUCS with the expected outcome of succesful detection multiple times to ensure good coverage

- Goal 2: Test with detection and lock out
	
	- Sub Objective 1: Test the effectiveness of plugging in a new keyboard while running BUCS with the expected outcome of lock out multiple times with multiple devices to ensure good coverage

	- Sub Objective 2: Test the effectiveness of plugging in a bad USB device while running BUCS with the expected outcome of lock out multiple times to ensure good coverage

- Goal 3: Test with detection, lock out, and CAPTCHA style challenge 

	- Sub Objective 1: Test the effectiveness of plugging in a new keyboard while running BUCS with the expected outcome of succesful detection, lock out, and deployment of CAPTCHA style challenge multiple times with multiple devices to ensure good coverage

	- Sub Objective 2: Test the effectiveness of plugging in a bad USB device while running BUCS with the expected outcome of succesful detection, lock out, and deployment of CAPTCHA style challenge multiple times to ensure good coverage

- Tentative Goal 4: If found fully effective, continue development and testing to a final product (detailed later in Package deliverable software for installation) 
***
### If found ineffective research what other options there are to develop a product for Windows

- Goal 1: Investigate potential Windows configurations that will halt USB communication until user selects otherwise.

- Goal 2: Consider available security policy objects to allow for mass deployment over a domain.
***
### Package deliverable software for installation

- Goal 1: Package project into a zip folder for more general distribution.

	- Sub Objective 1: Prepare documentation for download and setup.

- Goal 2: Package project into files usable by applicable installation managers (apt, rpm, yum, msi).

	- Sub Goal 1: Achieve functionality on multiple platforms. 


# Resources Needed

|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|-------------------|---------|---------------------------|-------------|
|AiTrip Digispark MicroUSB Dev Board | No | All | Board that will be used to craft the BadUSB|
|Windows 10 VM | No | All | VM on which we can test the function of the BadUSB and our code|
|Windows 10 PC| No | Mitchell | PC on which we can test the function of our BadUSB and our code|


# ENV Setup
### Step 1:
Download and install the appropriate python3 for your windows machine from `python.org/downloads/windows`
### Step 2:
Install these python libraries using pip

  ```
  pip install PyYaml
  pip install random-word
  ```
  
### Step 3: Clone the repository
  ```
  git clone https://github.com/abladow/BAD-USB.git
  ```

You are ready to make changes to the code without throwing dependency errors!

### Step 4 

Enable PNP auditing in the Windows Local Security Policy under:
```
Advanced Audit Policy Configuration\Detailed Tracking\Audit PNP Activity
```
Enable Success and Failure.


#Diagrams
![Program Flow Chart](https://github.com/abladow/BAD-USB/blob/main/Documentation/BUCS_FlowChart.png?raw=true)
![Architecture Interaction](https://github.com/abladow/BAD-USB/blob/main/Documentation/BUCS_Windows_Interaction.png?raw=true)
![Process Flow Chart](https://github.com/abladow/BAD-USB/blob/main/Documentation/process%20flow.png?raw=true)
