import shutil
import os
src = input("Enter your asset_indexer location: ")
src = rf"{src}"
modpath = input("Enter the path for Mods folder: ")
modpath = rf"{modpath}"
mods = os.listdir(modpath)
modsdict = {}
for i in mods:
    modsdict[i[0]] = mods[i]
def replace():
    modint = input("Press the first letter of the mod to activate it: ")
    shutil.copyfile(rf"{modsdict[modint]}", src)
    print("replaced succesfully")
while True:
    try:
        replace()
    except Exception as e:
        print("Cannot Replace")
        print(e)