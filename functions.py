from colorama import init, Fore, Style
import ctypes
import constant as const
import re
import os
import shutil
import tempfile
import time
import zipfile

init()
temp = os.path.join(tempfile.gettempdir(), "InstallMySofts")
if not os.path.exists(temp):
    os.makedirs(temp)


def remove_temp():
    log_show(f"Deleting {temp}")
    shutil.rmtree(temp)
    time.sleep(1)


def clear():
    if os.name == "nt":
        os.system("cls")


def set_console_title(string):
    ctypes.windll.kernel32.SetConsoleTitleW(string)


def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        log_show(f"Please wait for {timeformat} seconds its automatically goto back", end="\r")
        time.sleep(1)
        t -= 1


def find_files(file_name, file_path, file_ext=".zip"):
    new_file_with_ext = file_name.replace(file_name, file_name + file_ext)
    for root, dirs, files in os.walk(file_path):
        if new_file_with_ext in files:
            return os.path.join(root, new_file_with_ext)


def unzip_file(file_name):
    try:
        zip_file = zipfile.ZipFile(file_name, "r")
        zip_file.extractall(path=temp)
        zip_file.close()
    except RuntimeError:
        exception_heading("File is password protected or encounter runtime error")


def install_software(file_name, setup_exe_with_arg, is_setx=False):
    try:
        getting_file = find_files(file_name, "F:\\")
        if not getting_file:
            getting_file = find_files(file_name, "D:\\")
        if not getting_file:
            exception_heading("File not found")
        else:
            log_show(getting_file)
            time.sleep(1)
            unzip_file(getting_file)
            file_path_is = f"{temp}{os.sep}{file_name}{os.sep}"
            log_show("Unzipping to " + file_path_is)
            time.sleep(1)
            os.chdir(file_path_is)
            log_show(f"Installing {file_name}")
            time.sleep(1)
            os.system(f"{setup_exe_with_arg}")
            if is_setx:
                setx = ""
                output = re.findall(r'[\d.]+', file_name)
                new_output = re.findall(r'[\d]+', output[0])
                java_home = "JAVA_HOME"
                setx_jdk_8 = f"{os.environ['ProgramFiles']}{os.sep}Java{os.sep}jdk1.8.0_{output[1]}"
                setx_jdk_12 = f"{os.environ['ProgramFiles']}{os.sep}Java{os.sep}jdk-{output[0]}"
                if os.environ.get(java_home) is not None:
                    log_show(f"Already existed JAVA_HOME {os.environ['JAVA_HOME']}")
                    if new_output[0] == "8":
                        setx = setx_jdk_8
                        os.environ[java_home] = setx
                    elif new_output[0] == "12":
                        setx = setx_jdk_12
                        os.environ[java_home] = setx
                    log_show(setx)
                    log_show(f"Now updated to {setx}")
                else:
                    if new_output[0] == "8":
                        setx = setx_jdk_8
                        os.environ[java_home] = setx
                    elif new_output[0] == "12":
                        setx = setx_jdk_12
                        os.environ[java_home] = setx
                    time.sleep(1)
                    log_show(setx)
            countdown(4)
    except FileNotFoundError:
        exception_heading(f"{file_name} not found")


def center_text(string):
    print(string.center(shutil.get_terminal_size().columns))


def main_heading():
    print("\n")
    center_text(Fore.CYAN + Style.BRIGHT + const.heading_main_title.center(
        shutil.get_terminal_size().columns) + Style.RESET_ALL)
    print("\n")


def sub_heading(string):
    center_text(f"{Fore.LIGHTGREEN_EX}Categorized List of {string} Softwares{Style.RESET_ALL}")
    print("\n")


def back_heading():
    print(f"{Fore.LIGHTCYAN_EX}    [01] BACK TO MAIN{Style.RESET_ALL}")


def main_heading_softwares(num, string):
    print(f"{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Installing{Style.RESET_ALL} "
          f"{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Softwares{Style.RESET_ALL}")


def sub_heading_softwares(num, string):
    print(f"{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Install{Style.RESET_ALL} "
          f"{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL}")


def eixt_heading(num):
    print(f"{Fore.LIGHTRED_EX}    [{num}] EXIT{Style.RESET_ALL}")


def input_heading():
    return int(input(f"\n{Fore.LIGHTWHITE_EX}  Please enter your choice: {Style.RESET_ALL}"))


def exception_heading(string):
    print(f"\n{Fore.LIGHTRED_EX}    {string}{Style.RESET_ALL}")


def under_progress_heading(string):
    print(f"\n{Fore.CYAN}  {string}{Style.RESET_ALL}")


def exception_range_heading(num1, num2):
    print(
        f"\n{Fore.LIGHTRED_EX}    Value is not between {num1} to {num2}! "
        f"Please try again with valid options{Style.RESET_ALL}")


def log_show(string, end=""):
    print(f"\n{Fore.LIGHTYELLOW_EX}    {string}{Style.RESET_ALL}", end=end)
