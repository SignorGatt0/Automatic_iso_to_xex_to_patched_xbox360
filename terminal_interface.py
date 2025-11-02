from art import text2art
from termcolor import colored

from steps import step1

import os
from sys import platform

if platform == "win32":
    clear = "cls"   
else:
    clear = "clear"


os.system(clear)

# setup for the start of the application
iso_path = False
extract_path = False
ready = False
reload = True

def chose_folder() -> str:
    """
    Function that ask to the user a file path to use,
    the function return the where the file is
    """
    test_exist = False
    while not test_exist:
        path = str(input("insert FULL directory path..."))
        
        path = path.replace('"','') #remove "" from the inserted path
        test_exist = os.path.isdir(path) #check if the folder exist 
    return path


def option1() -> str:
    global iso_path

    """
    This function promt the user
    to chose witch directory to check for ISOs
    """

    # promt for selecting a folder for the ISOs
    input_folder:str = chose_folder()
    input_folder:str = colored(input_folder,'yellow') #color the path for better highlighting

    print(f"CURRENT ISO DIRECTORY SET TO | {input_folder}")
    # update the interface to display that a folder has been chosen
    iso_path = True

    return input_folder


def option2()-> str:
    global extract_path

    """
    This function promt the user
    to chose witch directory to check for ISOs
    """

    # promt for selecting a folder for the ISOs
    extract_folder:str = chose_folder()

    extract_folder = colored(extract_folder,'yellow') #color the path for better highlighting

    print(f"CURRENT EXTRACTION DIRECTORY SET TO | {extract_folder}")
    # update the interface to display that a folder has been chosen
    extract_path = True

    return extract_folder


def option3():
    # check if the input and the output folder are chosed
    if iso_path and extract_path:
        step1()
    elif not iso_path or not extract_path:
        # stop the start from the missing requirement 
        print(colored('ERROR THE ISO OR THE OUTPUT DIRECTORY HAS NOT BEEN CHOSED','red'))
        x = input("")

# application main loop
while reload:

    # creating the program title
    Art = text2art("ARLO", font="sub-zero")
    print(colored(Art, "magenta"))

    Art = text2art("AUTO", font="sub-zero")
    print(colored(Art, "magenta"))

    Art = text2art("PATCHER", font="sub-zero")
    print(colored(Art, "magenta"))

    # update the interface
    
        # the program is ready for the third option
    if iso_path and extract_path:
        ready = True

    if iso_path:
        iso_path_output = "DONE"
    else:
        iso_path_output = "X"

    if extract_path:
        extract_path_output = "DONE"
    else:
        extract_path_output = "X"

    if ready:
        ready_output = colored("READY TO START", 'magenta')
    else:
        ready_output = colored("NOT READY", 'red')

    

    
    # the options creation
    # 1
    print(colored(f"1 |{iso_path_output}| select the folder of the ISOs", "green"))
    # 2
    
    print(colored(f"2 |{extract_path_output}| select the folder to put the extracted fies","white",))

    # 3
    print(f"3 |{ready_output}| START AUTOMATIC PROCESS")
    
    choice = int(input("... "))
    match choice:
        case 1:
            input_folder = option1()
            
        case 2:
            extract_folder = option2()
            
        case 3:
            option3()
    os.system(clear)


