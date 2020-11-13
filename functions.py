from colorama import init, Fore, Style
import constant as const
import os
import re
import shutil
import sys
import tempfile
import time
import zipfile

init()
temp = os.path.join(tempfile.gettempdir(), const.__product__)
if not os.path.exists(temp):
    os.makedirs(temp)


def center_text(string):
    print(string.center(shutil.get_terminal_size().columns))


def clear():
    if os.name == "nt":
        os.system("cls")


def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        log_show(f"Please wait for {timeformat} seconds its automatically goto back", end="\r")
        time.sleep(1)
        t -= 1


def find_files(drive_path, is_dir_find=False, dir_name=None, file_name=None, file_ext=None):
    for root, dirs, files in os.walk(drive_path):
        if is_dir_find:
            if dir_name in dirs:
                return os.path.join(root, dir_name)
        else:
            new_file_with_ext = file_name.replace(file_name, file_name + file_ext)
            if new_file_with_ext in files:
                return os.path.join(root, new_file_with_ext)


def find_files_from_drive(is_dir_find=False, dir_name=None, file_name=None, file_ext=None):
    try:
        if is_dir_find:
            find_dir = find_files("F:\\", is_dir_find=is_dir_find, dir_name=dir_name)
            if not find_dir:
                find_dir = find_files("D:\\", is_dir_find=is_dir_find, dir_name=dir_name)
            if not find_dir:
                exception_heading("Directory not found")
            else:
                log_show(find_dir)
                return find_dir
        else:
            find_file = find_files("F:\\", is_dir_find=is_dir_find, file_name=file_name, file_ext=file_ext)
            if not find_file:
                find_file = find_files("D:\\", is_dir_find=is_dir_find, file_name=file_name, file_ext=file_ext)
            if not find_file:
                exception_heading("File not found")
            else:
                log_show(find_file)
                time.sleep(1)
                log_show("Unzipping to " + get_temp_path_by_file(file_name))
                unzip_file(find_file)
                time.sleep(1)
    except Exception as err:
        exception_heading(f"Error: {err}")


def get_temp_path_by_file(file_name):
    return f"{temp}{os.sep}{file_name}{os.sep}"


def install_software(is_dir_find=False, dir_name=None, file_name=None, setup_with_arg=None, is_setx=False, ext=".zip"):
    try:
        if is_dir_find:
            found_dir = find_files_from_drive(is_dir_find=is_dir_find, dir_name=dir_name)
            if len(os.listdir(found_dir)):
                log_show(f"Installing from directory {found_dir}")
                os.chdir(found_dir)
                time.sleep(1)
                os.system(f"{setup_with_arg}")
            else:
                log_show(f"{found_dir} is empty")
        else:
            find_files_from_drive(is_dir_find=is_dir_find, file_name=file_name, file_ext=ext)
            log_show(f"Installing {file_name}")
            os.chdir(get_temp_path_by_file(file_name))
            time.sleep(1)
            os.system(f"{setup_with_arg}")
            if is_setx:
                setx = ""
                output = re.findall(r"[\d.]+", file_name)
                new_output = re.findall(r"[\d]+", output[0])
                java_home = "JAVA_HOME"
                setx_jdk_8 = f"{os.environ['ProgramFiles']}{os.sep}Java{os.sep}jdk1.8.0_{output[1]}"
                setx_jdk_12 = f"{os.environ['ProgramFiles']}{os.sep}Java{os.sep}jdk-{output[0]}"
                if os.environ.get(java_home) is not None:
                    log_show(f"Already existed JAVA_HOME {os.environ[java_home]}")
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
    except Exception as err:
        exception_heading(f"Error: {err}")


def portable_crack_patch(file_name, setup_with_arg, file_ext=".zip"):
    if os.path.exists(get_temp_path_by_file(file_name)):
        if len(os.listdir(get_temp_path_by_file(file_name))) > 0:
            log_show(f"Opening from existing {file_name}")
            os.chdir(get_temp_path_by_file(file_name))
            time.sleep(1)
            os.system(setup_with_arg)
        else:
            find_files_from_drive(file_name=file_name, file_ext=file_ext)
            log_show(f"Opening {file_name}")
            os.chdir(get_temp_path_by_file(file_name))
            time.sleep(1)
            os.system(setup_with_arg)
            # os.startfile(path, setup_exe_with_arg)
    else:
        find_files_from_drive(file_name=file_name, file_ext=file_ext)
        log_show(f"Opening {file_name}")
        os.chdir(get_temp_path_by_file(file_name))
        time.sleep(1)
        os.system(setup_with_arg)
        # os.startfile(path, setup_exe_with_arg)


def remove_temp():
    try:
        if not len(os.listdir(temp)) == 0:
            log_show(f"Deleting {temp}")
            shutil.rmtree(temp)
            time.sleep(1)
    except PermissionError as err:
        exception_heading("Some files are still running and working in background")
        exception_heading(err)
        time.sleep(2)
        sys.exit()


def set_console_title(string):
    if os.name == "nt":
        os.system("title " + string)


def unzip_file(file_name):
    try:
        zip_file = zipfile.ZipFile(file_name, "r")
        zip_file.extractall(path=temp)
        zip_file.close()
    except Exception as err:
        exception_heading(f"Error: {err}")


def back_heading():
    print(f"{Fore.LIGHTCYAN_EX}    [01] BACK TO MAIN{Style.RESET_ALL}")


def eixt_heading(num):
    print(f"{Fore.LIGHTRED_EX}    [{num}] EXIT{Style.RESET_ALL}")


def exception_heading(string):
    print(f"\n{Fore.LIGHTRED_EX}    {string}{Style.RESET_ALL}")


def exception_range_heading(num1, num2):
    print(
        f"\n{Fore.LIGHTRED_EX}    Value is not between {num1} to {num2}! "
        f"Please try again with valid options{Style.RESET_ALL}")


def input_heading():
    return int(input(f"\n{Fore.LIGHTWHITE_EX}  Please enter your choice: {Style.RESET_ALL}"))


def log_show(string, end=None):
    print(f"\n{Fore.LIGHTYELLOW_EX}    {string}{Style.RESET_ALL}", end=end)


def main_heading():
    print("\n")
    center_text(Fore.CYAN + Style.BRIGHT + const.heading_main_title.center(
        shutil.get_terminal_size().columns) + Style.RESET_ALL)
    print("\n")


def main_heading_softwares(num, string):
    print(f"{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Installing{Style.RESET_ALL} "
          f"{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Softwares{Style.RESET_ALL}")


def sub_heading(string):
    center_text(f"{Fore.LIGHTGREEN_EX}Categorized List of {string} Softwares{Style.RESET_ALL}")
    print("\n")


def sub_heading_portable(num, string):
    print(f"{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Program{Style.RESET_ALL} "
          f"{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}(Portable){Style.RESET_ALL}")


def sub_heading_softwares(num, string):
    print(f"{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Install{Style.RESET_ALL} "
          f"{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL}")


def under_progress_heading(string):
    print(f"\n{Fore.CYAN}  {string}{Style.RESET_ALL}")
