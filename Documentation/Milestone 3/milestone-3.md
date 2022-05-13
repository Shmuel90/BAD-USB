# Progress Report 05/13/2022
## Overview
For this milestone we continued off our previous progress of a successful method to stop BadUSB attacks. We began with refining the program, creating a custom library to help support the program and deliver a custom CAPTCHA that is more user friendly. We additionally learned more about BadUSB scripts and the devices that can deliver them. We also theorized more methods to potentially thwart BadUSB attacks. \
\
As for the results of all our testing, results were great. We had only seen one software solution to this problem, and so the onset of this project was a mostly unworked area. When we finally acheived detection and successful interjection in Milestone 2 we were able to use that as our baseline to test against. With testing on multiple devices and with multiple attack types, we were able to successfully interject into all of the attacks, thwarting them. After we studied the basic attacks and tested them, we began to try and find work arounds of our program. We were able to identify a few, but using that we were able to theorize solutions that could be implemented into BUCS in the future.

## Outcomes
We continued to refine our project and learned more about BadUSB scripts so that we could better protect against them. 

	* Created a new library to create the CAPTCHA that better fit needs of users BAD-USB/BUCS Dev start/Windows/dictionary.py && Cap.py			* Maintained detection of BadUSBs and was able to interject into them successfuly
	* Discovered areas where BUCS was able to be defeated
	* Researched BadUSB scripts more in depth and discovered common methods among them
	* Researched common BadUSB methods to better defend against them
	* Crafted ideas as to how additional protections could be implemented
## Hinderances
Our biggest challenge in this milestone was time remaining. We were able to learn more and understand the problem at hand a lot more after we began thwarting the attacks. With this greater understanding we have been able to come up with newer methods that can increase protections. Some of them do not appear to be able to be done with the access that we have to developing on Windows, but the methods that could potentially be implemented we were running out of time at the end of the project to do. We have additional protections we would like to implement to the project in the future.
