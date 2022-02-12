# BAD-USB

# Executice Project Summary
## Problem Statement
Users need an easy way to input data to a computer. This led to the creation of devices such as mice and keyboards to allow users to achieve that goal. Throughout the years, technology of mice and keyboards alike grew, and we now have created USB and HID to assist in creating easy input methods for users.
The issue with HID is that it is an innately trusted device for operating systems. While there is no issue with innately trusting a keyboard, there is a problem with trusting a device that can masquerade as a keyboard. In 2014 the power of devices known generically as BadUSBs was demonstrated at Defcon. These devices can pretend to be a keyboard and automatically inputting malicious commands upon plug in. 

## Project Goals 
1. Develop a prototype **Maybe name prouduct here** in Python
2. Research effectivness in Python \
2a. If Found effective in Python continue development to a final product \
3. If found ineffective research methods to develop prototype in C
3a. Develop prototype in C \
3b. Research effectivness in C \
3c. If found effective in C continue development to a final product
4. If found ineffective research what other options there are to develop a prouduct for Windows
## Merit
This project can potentially save companies from headaches in the future. There is no current ethical issue with developing an application to assist in the protection of a computer, and while there are currently mitigations in place to protect against BadUSB attacks, this will introduce a full protection against it. 

# Proposed Timeline

# Risk List

|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
|security bypassed(36) | 6 | 6 | The security check that detects a new keyboard fails to detect or start  |
|Failure to unlock(28) | 7 | 4 | Even if check is passed the keyboard is not allowed to type  |
|USB disable(18) | 9 | 2 | Through security policy or other USB ports become unusable |
|Lockout(24) | 8 | 3 | Our Utility stop any form of keyboard input  |
|Project failure(30) | 10 | 3 | Failure to create a effective method to stop Bad USBs  |

# Project Methodology

# Resources Needed

|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|-------------------|---------|---------------------------|-------------|
|AiTrip Digispark MicroUSB Dev Board | No | All | Board that will be used to craft the BadUSB|
|Windows 10 VM | No | All | VM on which we can test the function of the BadUSB and our code|
|Windows 10 PC| No | Mitchell | PC on which we can test the function of our BadUSB and our code|

# First Sprint Plan

