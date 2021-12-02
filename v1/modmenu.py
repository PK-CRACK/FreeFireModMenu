import shutil
src = input("Enter your asset_indexer location: ")
mods = {"A" : input("Enter the location of the file in folder antena!"), "H": input("Enter the location of the file in folder head! "), "D":input("Enter the location of the file in folder default! ")}
src = rf"{src}"
def replace():
    mod = input("Press D,H and A for Default, Head Mod, Antena Mod respectively: ")
    shutil.copyfile(rf"{mods[mod]}", src)
    print("replaced succesfully")
while True:
    try:
        replace()
    except Exception as e:
        print("Cannot Replace")
        print(e)