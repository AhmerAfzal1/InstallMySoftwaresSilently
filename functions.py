import enum
import os
import re
import shutil
import sys
import tempfile
import time
import winreg as reg
import zipfile

from colorama import init, Fore, Style

import constant as const

init()
temp = os.path.join(tempfile.gettempdir(), const.__product__)
if not os.path.exists(temp):
    os.makedirs(temp)


class AnOtherTask(enum.Enum):
    REG_GIT = 'gitbash'


class JavaVersion(enum.IntEnum):
    JAVA_8 = 8
    JAVA_12 = 12


class SetX(enum.Enum):
    JAVA = 'java'


def center_text(string):
    print(string.center(shutil.get_terminal_size().columns))


def clear():
    if os.name == 'nt':
        os.system('cls')


def countdown(t):
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    log_show(f'Please wait for {timeformat} seconds its automatically goto back')
    time.sleep(t)
    # while t >= 0:
    #     mins, secs = divmod(t, 60)
    #     timeformat = '{:02d}:{:02d}'.format(mins, secs)
    #     log_show(f'Please wait for {timeformat} seconds its automatically goto back', end='\r')
    #     time.sleep(1)
    #     t -= 1


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
        if not file_ext.endswith('.zip'):
            exception_heading(f'{file_name + file_ext} is not unsupported format, please use zip')
        else:
            if is_dir_find:
                log_show(f'Finding directory {dir_name}')
                find_dir = find_files('F:\\', is_dir_find=is_dir_find, dir_name=dir_name)
                if not find_dir:
                    find_dir = find_files('D:\\', is_dir_find=is_dir_find, dir_name=dir_name)
                if not find_dir:
                    exception_heading('Directory not found')
                else:
                    return find_dir
            else:
                log_show(f'Finding file {file_name}')
                find_file = find_files('F:\\', is_dir_find=is_dir_find, file_name=file_name, file_ext=file_ext)
                if not find_file:
                    find_file = find_files('D:\\', is_dir_find=is_dir_find, file_name=file_name, file_ext=file_ext)
                if not find_file:
                    exception_heading('File not found')
                else:
                    time.sleep(1)
                    log_show('Unzipping to ' + get_temp_path_by_file(file_name))
                    unzip_file(find_file)
                    time.sleep(1)
    except Exception as err:
        exception_heading(f'Error: {err}')


def get_temp_path_by_file(file_name):
    return f'{temp}{os.sep}{file_name}{os.sep}'


def install_software(is_dir_find=False, dir_name=None, file_name=None, setup_with_arg=None, registry=None,
                     set_environ=None, another_task=None, ext='.zip'):
    try:
        if is_dir_find:
            found_dir = find_files_from_drive(is_dir_find=is_dir_find, dir_name=dir_name)
            if len(os.listdir(found_dir)):
                log_show(f'Installing from directory {found_dir}')
                os.chdir(found_dir)
                time.sleep(1)
                os.system(f'{setup_with_arg}')
            else:
                log_show(f'{found_dir} is empty')
        else:
            find_files_from_drive(is_dir_find=is_dir_find, file_name=file_name, file_ext=ext)
            log_show(f'Installing {file_name}')
            os.chdir(get_temp_path_by_file(file_name))
            time.sleep(1)
            os.system(f'{setup_with_arg}')
            if registry is not None:
                if os.path.isfile(get_temp_path_by_file(file_name) + os.sep + registry):
                    log_show(f'Installing registry {registry}')
                    time.sleep(1)
                    # os.chdir(get_temp_path_by_file(file_name))
                    os.system(f'{registry}')
                else:
                    exception_heading(f'File {registry} not found')
            if set_environ.value is not None:
                set_x(file_name=file_name, setx_enum=set_environ.value)
            if another_task.value is not None:
                perform_another_task(task=another_task.value)
            countdown(3)
    except Exception as err:
        exception_heading(f'Error: {err}')


def perform_another_task(task):
    if task.value == AnOtherTask.REG_GIT.value:
        log_show(f'Installing registry')
        w_root = reg.HKEY_CLASSES_ROOT
        w_sub_dir = r'Directory\shell\bash'  # Shell for directories
        w_sub_ins_dir = r'Directory\Background\shell\bash'  # Shell for inside directories
        w_sub_file = r'*\shell\Git Bash Here'  # Shell for files
        w_name = 'Icon'
        w_value_type = reg.REG_SZ
        w_default = ''  # Like (Default)
        w_value = r'C:\Program Files\Git\git-bash.exe'
        w_value_key = 'Git Bash Here'
        # This will make it appear when you right click on a folder
        set_reg(root_key=w_root, sub_key=w_sub_dir, name_key=w_default, value_type=w_value_type, value_key=w_value_key)
        set_reg(root_key=w_root, sub_key=w_sub_dir, name_key=w_name, value_type=w_value_type, value_key=w_value)
        set_reg(root_key=w_root, sub_key=w_sub_dir + r'\command', value_type=w_value_type, name_key=w_default,
                value_key=f'"{w_value}" "--cd=%1"')

        # This will make it appear when you right click inside a folder
        set_reg(root_key=w_root, sub_key=w_sub_ins_dir, name_key=w_default, value_type=w_value_type,
                value_key=w_value_key)
        set_reg(root_key=w_root, sub_key=w_sub_ins_dir, name_key=w_name, value_type=w_value_type, value_key=w_value)
        set_reg(root_key=w_root, sub_key=w_sub_ins_dir + r'\command', value_type=w_value_type, name_key=w_default,
                value_key=f'"{w_value}" "--cd=%v."')

        # This will make it appear when you right click a file
        set_reg(root_key=w_root, sub_key=w_sub_file, name_key=w_default, value_type=w_value_type, value_key=w_value_key)
        set_reg(root_key=w_root, sub_key=w_sub_file, name_key=w_name, value_type=w_value_type, value_key=w_value)
        set_reg(root_key=w_root, sub_key=w_sub_file + r'\command', value_type=w_value_type, name_key=w_default,
                value_key=f'"{w_value}" "--cd=%1"')
    else:
        exception_heading(f'Invalid AnOtherTask type')
        pass


def portable_crack_patch(file_name, setup_with_arg, file_ext='.zip'):
    if os.path.exists(get_temp_path_by_file(file_name)):
        if len(os.listdir(get_temp_path_by_file(file_name))) > 0:
            log_show(f'Opening from existing {file_name}')
            os.chdir(get_temp_path_by_file(file_name))
            time.sleep(1)
            os.system(setup_with_arg)
        else:
            find_files_from_drive(file_name=file_name, file_ext=file_ext)
            log_show(f'Opening {file_name}')
            os.chdir(get_temp_path_by_file(file_name))
            time.sleep(1)
            os.system(setup_with_arg)
            # os.startfile(path, setup_exe_with_arg)
    else:
        find_files_from_drive(file_name=file_name, file_ext=file_ext)
        log_show(f'Opening {file_name}')
        os.chdir(get_temp_path_by_file(file_name))
        time.sleep(1)
        os.system(setup_with_arg)
        # os.startfile(path, setup_exe_with_arg)


def read_reg(computer_name=None, root_key=None, sub_key=None, name_key=None):
    try:
        _connect = reg.ConnectRegistry(computer_name, root_key)
        read_key = reg.OpenKey(_connect, sub_key, 0, reg.KEY_READ)
        key_value = reg.QueryValueEx(read_key, name_key)
        read_key.Close()
        return key_value
    except FileNotFoundError as not_found:
        return f'Registry not found: {not_found}'
    except PermissionError as permission:
        return f'Permission denied: {permission}'
    except OSError:
        return None


def remove_temp():
    try:
        if not len(os.listdir(temp)) == 0:
            log_show(f'Deleting {temp}')
            shutil.rmtree(temp)
            time.sleep(1)
    except PermissionError as err:
        exception_heading('Some files are still running and working in background')
        exception_heading(err)
        time.sleep(2)
        sys.exit()


def set_console_title(string):
    if os.name == 'nt':
        os.system('title ' + string)


def set_reg(root_key, sub_key, name_key, value_type, value_key):
    try:
        reg.CreateKey(root_key, sub_key)
        write_key = reg.OpenKey(root_key, sub_key, 0, reg.KEY_WRITE)
        reg.SetValueEx(write_key, name_key, 0, value_type, value_key)
        reg.CloseKey(write_key)
        return True
    except FileNotFoundError as not_found:
        return f'Registry not found: {not_found}'
    except PermissionError as permission:
        return f'Permission denied: {permission}'
    except OSError:
        return False


def set_x(file_name, setx_enum):
    if setx_enum.value == SetX.JAVA.value:
        setx = ''
        java_home = 'JAVA_HOME'
        output = re.findall(r'[\d.]+', file_name)
        new_output = re.findall(r'[\d]+', output[0])
        setx_jdk_8 = f'{os.environ["ProgramFiles"]}{os.sep}Java{os.sep}jdk1.8.0_{output[1]}'
        setx_jdk_12 = f'{os.environ["ProgramFiles"]}{os.sep}Java{os.sep}jdk-{output[0]}'
        if os.environ.get(java_home) is not None:
            log_show(f'Already existed JAVA_HOME {os.environ[java_home]}')
            if new_output[0] == JavaVersion.JAVA_8.value:
                setx = setx_jdk_8
                os.environ[java_home] = setx
            elif new_output[0] == JavaVersion.JAVA_12.value:
                setx = setx_jdk_12
                os.environ[java_home] = setx
            log_show(setx)
            log_show(f'Now updated to {setx}')
        else:
            if new_output[0] == JavaVersion.JAVA_8.value:
                setx = setx_jdk_8
                os.environ[java_home] = setx
            elif new_output[0] == JavaVersion.JAVA_12.value:
                setx = setx_jdk_12
                os.environ[java_home] = setx
            time.sleep(1)
            log_show(setx)
    else:
        exception_heading(f'Invalid environ {setx_enum} type')
        pass


def unzip_file(file_name):
    try:
        zip_file = zipfile.ZipFile(file_name, 'r')
        zip_file.extractall(path=temp)
        zip_file.close()
    except Exception as err:
        exception_heading(f'Error: {err}')


def back_heading():
    print(f'{Fore.LIGHTCYAN_EX}    [01] BACK TO MAIN{Style.RESET_ALL}')


def eixt_heading(num):
    print(f'{Fore.LIGHTRED_EX}    [{num}] EXIT{Style.RESET_ALL}')


def exception_heading(string):
    print(f'\n{Fore.LIGHTRED_EX}    {string}{Style.RESET_ALL}')


def exception_range_heading(num1, num2):
    print(
        f'\n{Fore.LIGHTRED_EX}    Value is not between {num1} to {num2}! '
        f'Please try again with valid options{Style.RESET_ALL}')


def input_heading():
    return int(input(f'\n{Fore.LIGHTWHITE_EX}  Please enter your choice: {Style.RESET_ALL}'))


def log_show(string, end=None):
    print(f'\n{Fore.LIGHTYELLOW_EX}    {string}{Style.RESET_ALL}', end=end)


def main_heading():
    print('\n')
    center_text(Fore.CYAN + Style.BRIGHT + const.heading_main_title.center(
        shutil.get_terminal_size().columns) + Style.RESET_ALL)
    print('\n')


def main_heading_softwares(num, string):
    print(f'{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Installing{Style.RESET_ALL} '
          f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Softwares{Style.RESET_ALL}')


def sub_heading(string):
    center_text(f'{Fore.LIGHTGREEN_EX}Categorized List of {string} Softwares{Style.RESET_ALL}')
    print('\n')


def sub_heading_portable(num, string):
    print(f'{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Program{Style.RESET_ALL} '
          f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}(Portable){Style.RESET_ALL}')


def sub_heading_softwares(num, string):
    print(f'{Fore.LIGHTGREEN_EX}    [{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Install{Style.RESET_ALL} '
          f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL}')


def under_progress_heading(string):
    print(f'\n{Fore.CYAN}  {string}{Style.RESET_ALL}')
