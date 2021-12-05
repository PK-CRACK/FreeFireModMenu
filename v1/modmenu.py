import shutil
import os
src = input("Enter your asset_indexer location: ")
src = rf"{src}"
modname = input("Enter the name of the 3d or hack file: ")
moddirpath = input("Enter the path for Mods folder: ")
moddirpath = rf"{moddirpath}"
mods = os.listdir(moddirpath)
modsdict = {}
for i in mods:
    print(i, end="\n")
    modsdict[i[0]] = rf"{moddirpath}\{i}\{modname}"

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
