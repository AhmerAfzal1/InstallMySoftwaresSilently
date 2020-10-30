from colorama import init, Fore, Style
import constant as const
import os
import subprocess
import tempfile
import zipfile

init()
temp = tempfile.gettempdir()


def clear_screen():
    os.system("cls")


def set_console_title(string):
    os.system("title " + string)


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
        print("File is password protected or encounter runtime error")


def install_software(file_name, setup_exe, args=""):
    try:
        getting_file = find_files(file_name, "F:\\")
        if not getting_file:
            getting_file = find_files(file_name, "D:\\")
        if not getting_file:
            print("File not found")
        else:
            print(getting_file)
            unzip_file(getting_file)
            subprocess.call([f"{temp}{os.sep}{file_name}{os.sep}{setup_exe}", args])
            # os.startfile(f"{temp}{os.sep}{file_name}{os.sep}{setup_exe} {args}") # For manually installation something
    except FileNotFoundError:
        print(f"{file_name} not found")


def main_heading():
    print(Fore.CYAN + const.heading_main_title + Style.RESET_ALL)
    print("\n")


def sub_heading(string):
    print(Fore.LIGHTGREEN_EX + string + Style.RESET_ALL)
    print("\n")


def back_heading():
    print(f"{Fore.LIGHTCYAN_EX}[01] BACK TO MAIN{Style.RESET_ALL}")


def main_heading_softwares(num, string):
    print(f"{Fore.LIGHTGREEN_EX}[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Installing{Style.RESET_ALL} "
          f"{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Softwares{Style.RESET_ALL}")


def sub_heading_softwares(num, string):
    print(f"{Fore.LIGHTGREEN_EX}[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Install{Style.RESET_ALL} "
          f"{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL}")


def eixt_heading(num):
    print(f"{Fore.LIGHTRED_EX}[{num}] EXIT{Style.RESET_ALL}")
