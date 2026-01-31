import os
import subprocess
from sys import platform

if platform == "linux":
    clear = "clear"   
elif platform == "win32":
    clear = "cls"

def step1():
    iso_to_patch = str(input("insert the file"))
    print(iso_to_patch)

    print(os.path.exists(iso_to_patch))

    try:
        test = f"extract_xiso\\extract-xiso.exe -l \'{iso_to_patch}\'"
        subprocess.run(test)
    except:
        test = f"extract_xiso\\extract-xiso.exe -l {iso_to_patch}"
        subprocess.run(test)


# step1()
# def step2():
    # subprocess.run(f"XePatcher\XexTool.exe -m r -r a \"{file_to_patch}\"") # comand for patching a file