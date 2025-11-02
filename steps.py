import os
import subprocess
from sys import platform

if platform == "linux":
    clear = "clear"   
elif platform == "win32":
    clear = "cls"

def step1():
    iso_to_patch = r"G:\BECKUP_PC\rom\XBOX_360\iso_GREZZE\Dead Island - Riptide - Complete Edition (Europe) (En,Fr,De,Es,It,Pl)\Dead Island - Riptide - Complete Edition (Europe) (En,Fr,De,Es,It,Pl).iso"
    print(iso_to_patch)

    print(os.path.exists(r"G:\BECKUP_PC\rom\XBOX_360\iso_GREZZE\Dead Island - Riptide - Complete Edition (Europe) (En,Fr,De,Es,It,Pl)\Dead Island - Riptide - Complete Edition (Europe) (En,Fr,De,Es,It,Pl).iso"))

    
    test = f"extract_xiso\\extract-xiso.exe -l \'{iso_to_patch}\'"
    print(test)
    subprocess.run(test)

step1()
# def step2():
    # subprocess.run(f"XePatcher\XexTool.exe -m r -r a \"{file_to_patch}\"") # comand for patching a file