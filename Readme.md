# Details 😃
This is the first legal mod menu for Free Fire! On using this mod menu your Free Fire account
will not be banned! For more details on [How your Account is Safe?](#how-your-account-is-safe) click the markdown! The package has many folders. Let's start with the version 1.
### Version 1[v1 folder]
Version 1 is command-lined and is very basic. It only has the code and few mods.
Each of the folders and files are discussed below:
* `modmenu.py` file: This file is the main file of the menu.
* Mods: The Mods folder by default contains three folders:
    * Antena: The 'Antena' will folder contains all the files related to location hack.
    * Head: As like the 'Antena', it contains all the files related to Headshot Hack.
    * Default: It contains the default files.
    * Others: For appending other mods one should check [How to Add Mods](#how-to-add-mods)
* [Test Framework](#Test-Framework): It is a test for the menu. It is Optional and is manual.
### Version 2[v2 folder]
Version 2 is GUI Based. It contains a Mods folder, modmenu.py and menu.kv
Each of the folders and files are discussed below:
* `modmenu.py` file ad discussed in version 1 of the package. It is the main file and all the processing are done here.
* Mods: Like the previous version, it also contains three folders by default and additional mods can be appended here.
* `menu.kv` is the design file and it is responsible for the gui interface.
* [Test Framework](#Test-Framework):See Test FrameWork for more details.
### Design Folder
This folder contains the layout of the mod-menu and the GUI of the main menu is based on it.
It generally contains `index.html` and `style.css`
## How your Account is Safe?
Free generally detects hacks on the using of cheats or scripts. Due to presence cheats-detector in Free Fire, Free Fire can detect cheats in it! But with the help of this file Free Fire's anti-cheats will fail to detect the python file as Cheat and will subsequently ignore this file. Thus, your account will never be caught even you turn on the file. But if files which are being in the mods is a script there is a chance of getting your id banned! Be careful to use files named as 'assetindexer'.
# Installations ⬇️
For Installing the mod menu one should have 
* ## Pre-Requirements
    * Python: Python is required for running the mod menu. It should be installed by checking the "Add python to path" checkbox.
* ## Installation
    Installing the mod-menu is simple.
    * Just download any of the version i.e. 'v1' or 'v2' and keep the files in one folder.
    * Then open modmenu.py. This is should start the file.
    * Follow the instructions in the console to complete the process.
* ## How to add Mods
    * Create an image of the mod
    * Create a folder which contains the mod files and the image(is required for version 2)
    * Copy and Paste the folder in Mods folder in main directory
# Test Framework
The Test Framework starts from the Test folder. For the Test Framework you will need the 'index.html', 'img\default.png' and Mods
* Start with the index.html, Open it and ready it for further use
* Open the modmenu.py, and enter the path for the img\default.png in the 
* Then Enter the path for the Mods folder.
* Follow the instructions on the Console to complete the Test.

## Expected Errors ⁉️
The most expected errors are the file not found error. For this cases Recheck the file locations and renter the location if required. For the mod menu to work properly, one must look at the file locations carefully and the locations entered must match the particular file.
