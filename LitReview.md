<h1>Literature Review</h1>


Citation:
F. Griscioli, M. Pizzonia and M. Sacchetti, "USBCheckIn: Preventing BadUSB attacks by forcing human-device interaction," 2016 14th Annual Conference on Privacy, Security and Trust (PST), 2016, pp. 493-496, doi: 10.1109/PST.2016.7907004. https://ieeexplore-ieee-org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=7907004&isnumber=7906913

Abstract

INTRODUCTION: In the paper they gave an overview on what a BadUSB is, what it does along with why it is difficult to protect against. They then put forward two solutions: a software solution called GoodUSB which just asks the user what the device is, and a hardware solution which is the main focus of the paper called USBCheckIn which requires a human to do certain actions so that a USB device can be verified.

OBJECTIVES: The objective of this paper was to create a hardware middle man between a USB and a Host.

METHODS: The method they used to accomplish this was the middleman device could be used by a user to validate a USB peripheral through various actions displayed on a screen embedded on the middleman varying my Peripheral type.

RESULTS: The results they accomplished was the creation of a middle man device that did not affect responsiveness of HID devices, while allowing for decision-less USB security.

CONCLUSION:Their conclusion was that they were able to create a Hardware approach to protect against simple BadUSBs that merely mimic HID devices that did not cause any noticeable difference in user experience once it was validated. They accomplished basically what we are attempting to accomplish using hardware when we are going to do software.

***

Citation:
E. Karystinos, A. Andreatos and C. Douligeris, "Spyduino: Arduino as a HID Exploiting the BadUSB Vulnerability," 2019 15th International Conference on Distributed Computing in Sensor Systems (DCOSS), 2019, pp. 279-283, doi: 10.1109/DCOSS.2019.00066. https://ieeexplore-ieee-org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=8804730&isnumber=8804474

Abstract

INTRODUCTION: In this paper the authors started via giving background regarding what a Bad USB is, and then explained why attempted to create an Ardino that could be inserted and act as a Smart BadUSB which inserted keystrokes, and extracted files that were sent to an FTP server.

OBJECTIVES: They wanted to create an SMart BADUSB type device that could be inserted into a USB keyboard and exfiltrate files to an external server.

METHODS: for their methodology they used an Arduino UNO, they created a script using the free arduino IDE, and reflash/upgraded the firmware using a utility known as flip. They first wrote a script using Bash, DOS, or powershell depending on the target OS, then converted it into a keystroke sequence, which once loaded was installed into a keyboard via the USB wires.

RESULTS: There SPYdrino acted like a smart BADUSB keyboard, and were able to inject scripts that allowed FTP file exfiltration, they were able to determine a number of potential countermeasures for it.

CONCLUSION: The conclusions that they came to were the fact that their SPYdrino is unable to be detected by any standard currently known procedure at the time of publication, and that the SPYdrino was small, lightweight, adn capable of doing its objectives while hiding in a keyboard. 

***

Citation:
H. Lu, Y. Wu, S. Li, Y. Lin, C. Zhang and F. Zhang, "BADUSB-C: Revisiting BadUSB with Type-C," 2021 IEEE Security and Privacy Workshops (SPW), 2021, pp. 327-338, doi: 10.1109/SPW53761.2021.00053. https://ieeexplore-ieee-org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=9474274&isnumber=9474266

Abstract

INTRODUCTION: The writers took the existing BAD-USB type attacks and proceeded to attempt to move them to USB-C connections to exploit the additional features and continuing lack of security present. 

OBJECTIVES: Take the current BADUSB type attacks and move it a step further to allow active screen capturing and mouse inputs. Exploit further features enabled by USB 3.0 

METHODS: The new version of BADUSB used five main parts: a USB 3.x hub for connection between the victim and attacker components, a video capturing device to convert the DisplayPort data from the USB to data compatible with the SBC, an HID emulator, a SBC to handle the controlling of all the components and passing malicious data, and a wifi or GSM module for remote connection by the attacker. BADUSB-C was capable of running in low profile HID mode for attacks similar to the previous BADUSB generation, video capture mode which captures the device’s screen and attempts to identify valuable private information, and a more overt full control mode which allows for an effective full backdoor into the device. The writers proceeded to plug the BADUSB-C device into a multitude of different mobile and desktop devices from varying manufacturers and test the various attack functions. 


RESULTS: Some pre existing USB defenses are fully effective against BADUSB-C including GoodUSB and USBeSafe. Additionally some OS systems provide software cues alerting the user that the USB device is mirroring their screen. BADUSB-C was overall effective in it’s goal to take control of a user’s device or extract data and was capable of carrying out attacks on mobile and desktop devices.

CONCLUSION: The USB protocol itself should not be expected to provide security as a feature. The most effective countermeasures for BADUSB are the types that provide the user knowledge of an unexpected state. Countermeasures should require that all input and output to and from the newly connected device be suspect and treated accordingly.

***

Citation: 
El Bouanani, F. & Association for Computing Machinery-Digital Library. (2018). Proceedings of the 2nd international conference on smart digital environment. http://dl.acm.org/citation.cfm?id=3289100 

Abstract

INTRODUCTION: The inception of the bad USB caused quite an issue for the computing world, as it has caused us to have to rethink how we create and operate with USB devices. One particular issue with how USB is handled is that while we can scan the contents of USB devices, the firmware is always trusted. One potential solution is to require firmware to be signed by the manufacturer and have the host determine if the device is legitimate. The issue with that is there are already millions of USB devices in the world and that would require them all to be reflashed. Therefore this approach is better for the next generation of devices. However an alternative approach that would be host based is whitelisting for authentication of USB devices.

OBJECTIVES: The objectives for this project are that an effective whitelist will be built against bad USB attacks by using a unique to every device fingerprint, show how unreliable currentwhitelisting methods are, show how to generate unique fingerprints, verify accuracy using real collected data, and validate accuracy via proof of concept using bad USB.  

METHODS: They achieved their goals in many ways. Firstly they used a set of features that is collected about a device on a plugin to create a unique fingerprint. Next, they showed unreliability of current whitelist methods by showing how many devices do not provide serial numbers, which is often a part of the whitelist, as well as how this information can be spoofed. Next, they used those unique identifiers, removed redundant ones, and created an efficient way to fingerprint USB devices. Lastly they verified accuracy and validated effectiveness by collecting data and testing bad USBs against their method. 

RESULTS: Using their method of whitelisting to counter bad USB attacks, they were able to achieve a success rate of 98.5%. This means that only 1.5% of items tested were incorrectly identified, making their product overall effective. 

CONCLUSION: This approach to whitelisting is seen in some of the other research entered in this paper, and seems to be effective given the testing performed by multiple groups. The testing method they took should be fairly similar to ours, as they recorded lots of data with different devices and tested that against their method, then tested it against bad USBs. 

***

Citation:
Proceedings of the 14th international conference on availability, reliability and security. (2019). https://dl.acm.org/action/showBook?doi=10.1145/3339252 

Abstract

INTRODUCTION: The USB is a known popular delivery method of attacks given its widespread use and portability. One such attack is the delivery of Stuxnet, a worm that was delivered through a USB drive that was dropped in a parking lot. This paper covers the design and open source implementation of a baseline mitigation technique against attacks through a USB vector, that follows security by design patterns thus minimizing the need for user interaction.  

OBJECTIVES: The objective is to have a more usable defense mechanism that is integrated into the USB stack, and be portable to any OS, a stronger protection and wider coverage than existing tools, and be the only protection mechanism needed. 

METHODS: The methods used on this project include creating new policies, and sending notifications to alert the user of suspicious USB activity. The first method is introducing a always or never block USB policy. The next is to block only when locked, so that a device that is plugged in while you are away cannot be used. They will also show new but blocked devices on the lock screen so that a user can be alerted to a new device being attached to their system. Next they will handle new input devices naively meaning that if a new device is attached with keyboard capabilities the screen will lock and not allow usage. Then a notification will arise so that if the device is masquerading as something other than a keyboard, the user will be aware of what is happening. Lastly, the method of using provenance to assist in filtering out input devices will allow the user to be disturbed less, and allow the computer to determine whether the device is malicious or not, or could be used maliciously. 

RESULTS: This method was proposed at a conference, and therefore has not had any testing performed as of yet. However, they had discussed related work that points out the needs to increase security when it comes to USB. Additionally, with the creation of USB-C, there is a new found need to fix USB authentication.

CONCLUSION: This article discusses some interesting solutions to the USB authentication issue that we face nowadays. However, there is no follow up to this article, so our method may be a potential solution to the issues raised in this article. The one thing that this article overlooked is the idea that a malicious individual could know the password, and bypass lock screen issues. The bad USB attack might just be a way to automate attacks instead of being a stealth way to get into the system. Otherwise the authors did a good job of explaining what the issue is and what needs to be done about it. 

***

Citation:
Hussein, Karmand & Kaya, Mehmet. (2016). AN EVALUATION OF DIFFERENT TYPES OF CAPTCHA: EFFECTIVENESS, USER- FRIENDLINESS, AND LIMITATIONS. 2. 12-19.
https://www.researchgate.net/publication/340006275_AN_EVALUATION_OF_DIFFERENT_TYPES_OF_CAPTCHA_EFFECTIVENESS_USER-_FRIENDLINESS_AND_LIMITATIONS 

Abstract

INTRODUCTION: CAPTHCAs are a security test usually found on websites during a signup or some other process that requires input to the website. The goal of a CAPTCHA is to make sure the user inputting the information is a human and not a bot scripted to put information into the site. CAPTCHAs can be thought of as a reverse Turing test. 

OBJECTIVES: The goal of this paper is to review the history and determine the effectiveness of CAPTCHA versions as they have been used over the years. 

METHODS: Methods used to review the CAPTCHAs is based on past literature and the intentions of the creators of CAPTCHA. It is stated that in order for a CAPTCHA to be effective, they should be easy for a human to pass, while difficult for a bot to pass.

RESULTS: The results of the study found that text based were the most preferred method of CAPTCHA, but they weren't the hardest to break. They were preferred for the reason of usability, but they were able to be broken using advanced scripting. 

CONCLUSION: This paper shows that CAPTCHAs are an effective means of preventing simple bots from being able to perform malicious input. They reviewed many different versions of CAPTCHAs and discovered what the most common type used was. They were able to beat text based CAPTCHAs with sophisticated bots and many steps, which while that is bad for CAPTCHAs in general, we fortunately will be dealing with very low ability devices that cannot read the screen. Therefore, a CAPTCHA style method of dealing with our problem should be effective.

***

Citation:
Vouteva, S., Verbij, R., & Roos, J. (2015). Feasibility and Deployment of Bad USB. University of Amsterdam, System and Network Engineering Master Research Project. https://rp.os3.nl/2014-2015/p49/report.pdf 

Abstract

INTRODUCTION: With new technology cropping up daily, lots of new attack vectors enter the cyber world with them. One of these attack vectors is USB based attacks, and while the idea of a flash drive containing a virus is easy to understand, lots of people push off the idea of bad usbs because of their seemingly larger technical requirement. The purpose of this paper is to demonstrate a proof of concept of the feasibility of a bad usb attack using an Arduino Micro as the bad usb. 

OBJECTIVES: The objectives of this paper is to 1. Find an attack that works without admin rights. 2. Run the attack in less than 10 seconds. 3. Download a file and bypass security measures to run an executable. 4. Obtain access from an outside computer and run a key logger. 5. Install a root certificate for http traffic interception. And 6. Install a backdoor. 

METHODS: The three steps taken to perform this proof of concept are: Kali preparation, execution on the victim machine, and running exploits from Kali. For Kali prep, Veil-Evasion was used to generate a payload and then upload it to the Arduino using Arduino IDE. Next the execution on the victim. On the victim when the Arduino is plugged in, the file containing the payload is downloaded and executed locally. Then the remote attacker is able to establish a connection. Next, on the attacker, all the exploits previously mentioned are executed and tested.

RESULTS: The results deemed that the feasibility of just a bad usb by itself being an effective attacker is fairly low. But combined with other tools from a remote attacker the feasibility increases greatly. The main draw to having physical access to a computer is that you defeat quite a few network security tools just by having a victim reach out to a host instead of the other way around. The impact of an attack of this caliber would be quite substantial as they were able to gain remote access to a victim in less than 10 seconds using a bad usb. However, they were unable to create an attack that bypassed the lock screen using a bad usb. 

CONCLUSION: The group that performed this research shows why bad usb protection is important. They were able to gain remote access to an unprivileged victim in under 10 seconds using a bad usb and openly available software. This proof of concept used basic tools and testbeds and covered all important bases while performing a penetration test. 

***

Citation:
fE. G. Chekole and H. Guo, "DARUD: Detecting and Arresting Rogue USB Devices in the V2X Ecosystem," 2021 IEEE International Conference on Service Operations and Logistics, and Informatics (SOLI), 2021, pp. 1-6, doi: 10.1109/SOLI54607.2021.9672338. https://ieeexplore-ieee-org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=9672338&isnumber=9672337

Abstract

INTRODUCTION: USB had been a widely adopted interface in the computing industry since its inception in the early 2000’s. Because of this it is an open standard and many USB technologies have been developed. Many of these developed technologies have been made insecurly, and attackers have been able to exploit vulnerabilities within USB historically. Most commonly by infecting a host machine with a malware of some form. Because of these vulnerabilities the group trying to craft V2X (vehicle to everything) must find a way to keep their systems secure, especially because it requires a large interconnected network of USB based devices in order to keep the system effective. In the IT world, USB device security is a problem, and some solutions found include: Disabling ports/filling them so they cannot be used, scanning of USB storage devices for malware, and whitelisting. These methods, while effective for the purpose they serve, do not work for V2X systems. Therefore the group decided to craft a system known as DARUD (Detects and Arrests Rouge USB Devices) as a way to assist in keeping rouge USB devices from joining the network.

OBJECTIVES: The objectives of the group’s project is to develop a lightweight toolkit that authorizes USB devices at runtime, while rejecting rouge USB devices from being able to be run. Additionally, with a whitelist enabled, it should protect against dishonest users sharing properties of whitelisted devices. It should add policies over the air, using a secure VPN tunneling approach so that physical access is not required to add policies. The effectiveness will be tested on a realistic V2X infrastructure, and should not hinder the operation of V2X.

METHODS: The methods they followed were first to scan attributes from the USB device to gain important information about the device and what it represents. Next DARUD constructs rules for the USB device, which will be used to authorize the device. These rules are based on the device attributes, and are important to be unique and non volatile as to make it as unique as possible while still being persistent. Next, they compute a fingerprint of the device to thwart attempts at bruteforcing or attribute sharing. This fingerprint is generated by the rules mentioned previously and a timestamp of when the device was added to the system. This fingerprint is then hardcoded to the USB device in a read only format and can be later queried so to make sure that authorization is given to the proper device. Next, is the authorization policy which is just a boolean value that is made with the rule and the fingerprint. Next, enforcing the policy. This is done by DARUD’s over the air security configuration, which allows for the policy to be updated without physical intervention. Lastly, they log the port activity so that audits and debugging can be performed.

RESULTS: The results are evaluated using the SmartMMS V2X infrastructure and in doing so determined there were no false positives or false negatives. Additionally the efficiency of the system was not compromised as there was no significant delay or service degradation with the introduction of DARUD. 

CONCLUSION: In all this paper is a good example of other responses to USB port security, which is a similar approach that we are taking. With that in mind, the approach they take is to prevent usb device brute forcing with regards to a whitelist, or properties sharing which would allow a malicious actor to place what seems like a legitimate device on the network. This approach is interesting because it uses a system of prebuilt rules that get generated to assist in defeating rouge USB devices. While that is also the intent of our project, we intend to focus on auto typing devices instead of malware based ones. However it is interesting to see how the effectiveness of DARUD was and the way they crafted the rules in a UDEV format so that it worked easily with linux and V2X. Overall the groups project seems to be sound with no large oversights other than the over the air policy delivery method, as that could be vulnerable to MitM attacks, but the introduction of VPN tunneling should keep that secure.
