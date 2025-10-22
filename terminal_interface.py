from art import text2art
from termcolor import colored
from tkinter.filedialog import askdirectory

# creating the program title
Art = text2art("ARLO", font="sub-zero")
print(colored(Art, "magenta"))

Art = text2art("AUTO", font="sub-zero")
print(colored(Art, "magenta"))

Art = text2art("PATCHER", font="sub-zero")
print(colored(Art, "magenta"))

# setup for the start of the application
iso_path = False
extract_path = False
ready = False
reload = True

def first_option() -> str:
    global iso_path

    """
    This function promt the user
    to chose witch directory to check for ISOs
    """

    # promt for selecting a folder for the ISOs
    input_folder: str = chose_folder()

    # update the interface to display that a folder has been chosen
    iso_path = True

    return input_folder


def second_option()-> str:
    global extract_path

    """
    This function promt the user
    to chose witch directory to check for ISOs
    """

    # promt for selecting a folder for the ISOs
    extract_folder: str = chose_folder()

    # update the interface to display that a folder has been chosen
    extract_path = True

    return extract_folder


def third_option():
    # check if the input and the output folder are chosed
    if iso_path and extract_path:
        # start
        pass
    elif not iso_path or not extract_path:
        # stop the start 
        print(colored('ERROR THE ISO OR THE OUTPUT DIRECTORY HAS NOT BEEN CHOSED','red'))
        return
    


def chose_folder() -> str:
    """
    Function that ask to the user a file path to use,
    the function return the where the file is
    """

    path: str = askdirectory(title="select a directory")
    return path

# application main loop
while reload:


    # update the interface
    if iso_path:
        iso_path_output = "DONE"
    else:
        iso_path_output = "X"

    if extract_path:
        extract_path_output = "DONE"
    else:
        extract_path_output = "X"

    if ready:
        ready_output = colored("READY TO START", 'light_blue')
    else:
        ready_output = colored("NOT READY", 'red')

    # the program is ready for the third option
    if iso_path and extract_path:
        ready = True

    # the options creation
    # 1
    print(colored(f"1 |{iso_path_output}| select the folder of the ISOs", "green"))
    # 2
    print(
        colored(
            f"2 |{extract_path_output}| select the folder to put the extracted fies",
            "white",
        )
    )
    # 3
    print(f"3 |{ready_output}| START AUTOMATIC PROCESS")


