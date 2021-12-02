import os
srcfile = input("Enter your asset_indexer location")
mods = [r"E:\Hack\Non Cheat Table\FreeFire\Test\head.png", r"E:\Hack\Non Cheat Table\FreeFire\Test\antena.png",r"E:\Hack\Non Cheat Table\FreeFire\Test\default.png"]
def replace():
    mod = input("Press D,H and A for Default, Head Mod, Antena Mod respectively: ")
    if mod == "H":
        os.replace(mods[0], srcfile)
        print("replaced succesfully")
    elif mod ==  "A":
        os.replace(mods[1], srcfile)
        print("replaced successfuly")
    elif mod == "D":
        os.replace(mods[2], srcfile)
while True:
    try:
        replace()
    except Exception:
        print("Cannot Replace")