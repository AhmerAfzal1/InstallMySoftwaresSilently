import enum
import inspect
import os
import re
import shlex
import shutil
import subprocess
import tempfile
import time
import winreg as reg
import zipfile

from colorama import init, Fore, Style

import constant as const

init()
temp = os.path.join(tempfile.gettempdir(), const.product)
if not os.path.exists(temp):
    os.makedirs(temp)


def center_text(string):
    print(string.center(shutil.get_terminal_size().columns))


def clear():
    if os.name == 'nt':
        os.system('cls')


def copying_files(src, dst):
    try:
        if os.path.isfile(src) and os.path.exists(dst):
            d = shutil.copy(src=src, dst=dst)
            if os.path.isfile(d):
                return True
            else:
                return False
    except PermissionError as err:
        exception_heading(f'You haven\'t permission: {err}')


def extract_archive(root, file_name, pwd=None):
    start_unzip = time.time()
    log_show(f'Extracting to {get_temp_path_by_file(file_name)}')
    zip_file = zipfile.ZipFile(file=os.path.join(root, file_name), mode='r')
    try:
        if pwd is not None:
            zip_file.setpassword(pwd=bytes(pwd, encoding=const.encode_utf_8))
        zip_file.extractall(path=temp)
    except zipfile.error as err_zip:
        exception_heading(f'Error while unzipping: {err_zip}')
    finally:
        zip_file.close()
        end_unzip = time.time()
        log_show(f'Extracted {file_name} in ', f'{get_time(start_unzip, end_unzip)}')


def find_files(dir_name=None, file_name=None, file_ext=None, pwd=None):
    try:
        start = time.time()
        get_file_path = inspect.stack()[1].filename
        get_file_name = os.path.splitext(os.path.basename(get_file_path))[0]
        if get_file_name.lower() == 'Developer'.lower():
            drives = ['D:\\', 'F:\\']
        else:
            drives = ['F:\\', 'D:\\']
        if file_ext.endswith('.zip'):
            for drive in drives:
                for root, dirs, files in os.walk(drive):
                    if dir_name is not None:
                        if dir_name in dirs:
                            return os.path.join(root, dir_name)
                    else:
                        file_with_ext = file_name.replace(file_name, file_name + file_ext)
                        if file_with_ext in files:
                            end = time.time()
                            log_show(f'Found file {file_with_ext} in ', f'{get_time(start, end)}')
                            time.sleep(const.wait_short)
                            extract_archive(root=root, file_name=file_with_ext, pwd=pwd)
                            time.sleep(const.wait_short)
        else:
            exception_heading(f'Extension for {file_name + file_ext} is unsupported format, please use zip archive')
    except Exception as err:
        exception_heading(err)


def get_temp_drivers_path_by_file(file_name, drivers_dir, sub_drivers_dir=None):
    if sub_drivers_dir is not None:
        return os.path.join(*[get_temp_path_by_file(file_name), drivers_dir, sub_drivers_dir])
    else:
        return os.path.join(*[get_temp_path_by_file(file_name), drivers_dir])


def get_temp_path_by_file(file_name):
    return os.path.join(temp, file_name)


def get_time(start, end):
    t = end - start
    mins, secs = divmod(t, 60)
    if secs <= 1 and mins <= 0:
        return f'{secs:0.2f} Second'
    elif secs >= 2 and mins <= 0:
        return f'{secs:0.2f} Seconds'
    elif mins <= 1 and secs <= 1:
        return f'{mins:0.0f} Minute and {secs:0.2f} Second'
    elif mins <= 1 and secs <= 59:
        return f'{mins:0.0f} Minute and {secs:0.2f} Seconds'
    else:
        return f'{mins:0.0f} Minutes and {secs:0.2f} Seconds'


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


def remove_temp(is_wait):
    if os.path.exists(temp):
        if os.path.isfile(temp) or os.path.isdir(temp):
            if is_wait:
                log_show(f'Wait for {const.wait_long - 2} seconds deleting {temp}')
                time.sleep(const.wait_long - 2)
                shutil.rmtree(temp, ignore_errors=True)
                time.sleep(const.wait_short)
            else:
                shutil.rmtree(temp, ignore_errors=True)
                time.sleep(const.wait_short)
        else:
            pass


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


def back_heading():
    print(f'{Fore.LIGHTCYAN_EX}\t[01] BACK TO MAIN{Style.RESET_ALL}')


def exit_heading(num):
    print(f'{Fore.LIGHTRED_EX}\t[{num}] EXIT{Style.RESET_ALL}')
    return num


def exception_heading(string, wait_input=False):
    print(f'\n{Fore.LIGHTRED_EX} {string}{Style.RESET_ALL}')
    if wait_input:
        input(const.wait_msg_input)


def exception_range_heading(num):
    print(
        f'\n{Fore.LIGHTRED_EX} Value is not between {1} to {int(num)}! '
        f'Please try again with valid option{Style.RESET_ALL}')


def input_heading():
    return int(input(f'\n{Fore.LIGHTWHITE_EX}  Please enter your choice: {Style.RESET_ALL}'))


def log_show(string, string_time=''):
    print(f'\n{Fore.LIGHTYELLOW_EX} {string}{Style.RESET_ALL}' +
          f'{Fore.LIGHTRED_EX}{string_time}{Style.RESET_ALL}')


def main_heading():
    print('\n')
    center_text(Fore.CYAN + Style.BRIGHT + const.heading_main_title.center(
        shutil.get_terminal_size().columns) + Style.RESET_ALL)
    print('\n')


def main_heading_softwares(num, string):
    print(f'{Fore.LIGHTGREEN_EX}\t[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Installing{Style.RESET_ALL} '
          f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Softwares{Style.RESET_ALL}')


def sub_heading(string):
    center_text(f'{Fore.LIGHTGREEN_EX}Categorized List of {string} Softwares{Style.RESET_ALL}')
    print('\n')


def sub_heading_portable(num, string):
    print(f'{Fore.LIGHTGREEN_EX}\t[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Program{Style.RESET_ALL} '
          f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}(Portable){Style.RESET_ALL}')


def sub_heading_softwares(num, string):
    print(f'{Fore.LIGHTGREEN_EX}\t[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Install{Style.RESET_ALL} '
          f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL}')


def under_progress_heading(string):
    print(f'\n{Fore.CYAN} {string}{Style.RESET_ALL}')


class AnOtherTask(enum.Enum):
    AOMEI_PRO = 'pro'
    AOMEI_SERVER = 'server'
    AOMEI_TECHNICIAN = 'technician'
    AOMEI_UNLIMITED = 'unlimited'
    HELIUM_MUSIC = 'helium'
    IDM = 'idm'
    REG_GIT = 'gitbash'
    JAVA = 'java'
    TRI_SUN_PDF = 'trysun'
    WINRAR_KEY = 'rar'


class JavaVersion(enum.IntEnum):
    JAVA_8 = 8
    JAVA_15 = 15


class Functions:
    @staticmethod
    def run_program(file_name, args=None, path=None, is_portable=False, sys_app_run=False):
        if args is None:
            arguments = shlex.split('')
        else:
            arguments = shlex.split(args)

        if not is_portable and not sys_app_run:
            return subprocess.run([file_name] + arguments, shell=True, stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding=const.encode_utf_8)
        elif sys_app_run and not is_portable:
            return subprocess.Popen([file_name, path] + arguments, shell=True, stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding=const.encode_utf_8)
        elif is_portable and not sys_app_run:
            return subprocess.Popen([file_name] + arguments, shell=True, stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding=const.encode_utf_8)

    @staticmethod
    def perform_another_task(task, file_name=None, dir_name=None, sys_app=None, child_file=None):
        dst_aomei = os.path.join(*[os.environ['ProgramFiles(x86)'], 'AOMEI Partition Assistant'])
        if task.value == AnOtherTask.REG_GIT.value:
            log_show(f'Installing registry')
            root = reg.HKEY_CLASSES_ROOT
            sub_dir = r'Directory\shell\bash'  # Shell for directories
            sub_ins_dir = r'Directory\Background\shell\bash'  # Shell for inside directories
            name = 'Icon'
            value_type = reg.REG_SZ
            default = ''  # Like (Default)
            value = r'C:\Program Files\Git\git-bash.exe'
            value_key = 'Git Bash Here'

            # This will make it appear when you right click on a folder
            set_reg(root_key=root, sub_key=sub_dir, name_key=default, value_type=value_type, value_key=value_key)
            set_reg(root_key=root, sub_key=sub_dir, name_key=name, value_type=value_type, value_key=value)
            set_reg(root_key=root, sub_key=sub_dir + r'\command', value_type=value_type, name_key=default,
                    value_key=f'"{value}" "--cd=%1"')

            # This will make it appear when you right click inside a folder
            set_reg(root_key=root, sub_key=sub_ins_dir, name_key=default, value_type=value_type,
                    value_key=value_key)
            set_reg(root_key=root, sub_key=sub_ins_dir, name_key=name, value_type=value_type, value_key=value)
            set_reg(root_key=root, sub_key=sub_ins_dir + r'\command', value_type=value_type, name_key=default,
                    value_key=f'"{value}" "--cd=%v."')

            # # This will make it appear when you right click a file
            # sub_file = r'*\shell\Git Bash Here'  # Shell for files
            # set_reg(root_key=root, sub_key=sub_file, name_key=default, value_type=value_type, value_key=value_key)
            # set_reg(root_key=root, sub_key=sub_file, name_key=name, value_type=value_type, value_key=value)
            # set_reg(root_key=root, sub_key=sub_file + r'\command', value_type=value_type, name_key=default,
            #         value_key=f'"{value}" "--cd=%1"')
        elif task.value == AnOtherTask.JAVA.value:
            log_show(f'Setting up Java Environments')
            setx = ''
            java_home = 'JAVA_HOME'
            output = re.findall(r'[\d.]+', file_name)
            new_output = re.findall(r'[\d]+', output[0])
            setx_jdk_08 = os.path.join(*[os.environ['ProgramFiles'], 'Java', f'jdk1.8.0_{output[1]}'])
            setx_jdk_15 = os.path.join(*[os.environ['ProgramFiles'], 'Java', f'jdk-{output[0]}'])
            if os.environ.get(java_home) is not None:
                log_show(f'Already existed JAVA_HOME {os.environ[java_home]}')
                if new_output[0] == JavaVersion.JAVA_8.value:
                    setx = setx_jdk_08
                    os.environ[java_home] = setx
                elif new_output[0] == JavaVersion.JAVA_15.value:
                    setx = setx_jdk_15
                    os.environ[java_home] = setx
                log_show(setx)
                log_show(f'Now updated to {setx}')
            else:
                if new_output[0] == JavaVersion.JAVA_8.value:
                    setx = setx_jdk_08
                    os.environ[java_home] = setx
                elif new_output[0] == JavaVersion.JAVA_15.value:
                    setx = setx_jdk_15
                    os.environ[java_home] = setx
                time.sleep(const.wait_short)
                log_show(setx)
        elif task.value == AnOtherTask.AOMEI_PRO.value:
            log_show(f'Cracking {file_name}')
            src = os.path.join(*[temp, file_name, 'Crack', 'Pro', 'cfg.ini'])
            is_copied = copying_files(src=src, dst=dst_aomei)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied crack file to {dst_aomei}')
        elif task.value == AnOtherTask.AOMEI_SERVER.value:
            log_show(f'Cracking {file_name}')
            src = os.path.join(*[temp, file_name, 'Crack', 'Server', 'cfg.ini'])
            is_copied = copying_files(src=src, dst=dst_aomei)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied crack file to {dst_aomei}')
        elif task.value == AnOtherTask.AOMEI_TECHNICIAN.value:
            log_show(f'Cracking {file_name}')
            src = os.path.join(*[temp, file_name, 'Crack', 'Technician', 'cfg.ini'])
            is_copied = copying_files(src=src, dst=dst_aomei)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied crack file to {dst_aomei}')
        elif task.value == AnOtherTask.AOMEI_UNLIMITED.value:
            log_show(f'Cracking {file_name}')
            src = os.path.join(*[temp, file_name, 'Crack', 'Unlimited', 'cfg.ini'])
            is_copied = copying_files(src=src, dst=dst_aomei)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied crack file to {dst_aomei}')
        elif task.value == AnOtherTask.WINRAR_KEY.value:
            log_show(f'Registering {dir_name}')
            src_winrar = os.path.join(*[dir_name, 'rarreg.key'])
            dst_winrar = os.path.join(*[os.environ['ProgramFiles'], 'WinRAR'])
            is_copied = copying_files(src=src_winrar, dst=dst_winrar)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied Rarreg.key to {dst_winrar}')
        elif task.value == AnOtherTask.IDM.value:
            log_show(f'Patching {file_name}')
            patcher_dir = os.path.join(*[os.environ['ProgramFiles(x86)'], file_name])
            subprocess.run(
                [os.path.join(get_temp_path_by_file(file_name), 'Patch.exe'), '/silent', '/overwrite', '/backup',
                 f'/startupworkdir {patcher_dir}'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            time.sleep(const.wait_short)
        elif task.value == AnOtherTask.TRI_SUN_PDF.value:
            log_show(f'Cracking {file_name}')
            src = os.path.join(*[temp, file_name, 'Crack', 'PTJ.exe'])
            dst = os.path.join(*[os.environ['ProgramFiles(x86)'], 'PDF Helper', 'PDF to JPG'])
            is_copied = copying_files(src=src, dst=dst)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied crack file to {dst}')
        elif task.value == AnOtherTask.HELIUM_MUSIC.value:
            log_show(f'Opening Notepad {file_name}')
            path = os.path.join(*[get_temp_path_by_file(file_name), child_file])
            Functions.run_program(file_name=sys_app, path=path, sys_app_run=True)
            time.sleep(const.wait_short)
        else:
            exception_heading(f'Invalid AnOtherTask type')
            time.sleep(const.wait_short)
            pass


class InstallSoftware(Functions):
    def __init__(self, dir_name=None, file_name=None, setup=None, args=None, registry=None, another_task=None,
                 driver_dir=None, sub_dri_dir=None, sys_app=None, child_file=None, ext='.zip', pwd=None, wait=0,
                 wait_input=False):
        self.dir_name = dir_name
        self.file_name = file_name
        self.setup = setup
        self.args = args
        self.registry = registry
        self.another_task = another_task
        self.driver_dir = driver_dir
        self.sub_dri_dir = sub_dri_dir
        self.sys_app = sys_app
        self.child_file = child_file
        self.ext = ext
        self.pwd = pwd
        self.wait = wait
        self.wait_input = wait_input

        try:
            start = time.time()
            wait_for = int(wait)
            if dir_name is not None:  # For find directory
                log_show(f'Searching directory {dir_name}...')
                found_dir = find_files(dir_name=dir_name, file_ext=ext)
                end = time.time()
                log_show(f'Found directory {dir_name} in ', f'{get_time(start, end)}')
                time.sleep(const.wait_short)
                if len(os.listdir(found_dir)):
                    log_show(f'Installing from directory {found_dir}...')
                    time.sleep(const.wait_short)
                    self.run_program(file_name=os.path.join(*[found_dir, setup]), args=args, is_portable=False)
                    if another_task is not None:
                        self.perform_another_task(task=another_task, dir_name=found_dir)
                    end = time.time()
                    log_show(f'Installed {dir_name} successfully in ', f'{get_time(start, end)}')
                    log_show(const.wait_msg)
                    time.sleep(const.wait_long)
                else:
                    log_show(f'{found_dir} is empty')
            else:
                if driver_dir is not None:
                    log_show(f'Searching {file_name}...')
                    if not os.path.exists(get_temp_drivers_path_by_file(file_name, driver_dir, sub_dri_dir)):
                        find_files(dir_name=None, file_name=file_name, file_ext=ext)
                    if sub_dri_dir is not None:
                        if sub_dri_dir == os.path.join(*['APPS', 'PROSETDX', 'Winx64']):
                            log_show(f'Installing {driver_dir} Drivers...')
                        else:
                            log_show(f'Installing {sub_dri_dir} Drivers...')
                    else:
                        log_show(f'Installing {driver_dir} Drivers...')
                    time.sleep(const.wait_short)
                    self.run_program(file_name=os.path.join(
                        get_temp_drivers_path_by_file(file_name, driver_dir, sub_drivers_dir=sub_dri_dir), setup),
                        args=args, is_portable=False)
                    end = time.time()
                    log_show(f'Installed {driver_dir} successfully in ', f'{get_time(start, end)}')
                else:
                    log_show(f'Searching file {file_name}...')
                    find_files(dir_name=None, file_name=file_name, file_ext=ext, pwd=pwd)
                    log_show(f'Installing {file_name}...')
                    self.run_program(file_name=os.path.join(get_temp_path_by_file(file_name), setup), args=args,
                                     is_portable=False)
                    time.sleep(const.wait_short)
                    if wait_for >= 1:
                        time.sleep(wait_for)
                    end = time.time()
                    log_show(f'Installed {file_name} successfully in ', f'{get_time(start, end)}')
                    if registry is not None:
                        if os.path.isfile(os.path.join(*[get_temp_path_by_file(file_name), registry])):
                            log_show(f'Installing registry {registry}...')
                            time.sleep(const.wait_short)
                            os.startfile(get_temp_path_by_file(file_name), setup)
                        else:
                            exception_heading(f'File {registry} not found')
                    if another_task is not None:
                        self.perform_another_task(task=another_task, file_name=file_name, sys_app=sys_app,
                                                  child_file=child_file)
                log_show(const.wait_msg)
                time.sleep(const.wait_long)
                if wait_input:
                    input(const.wait_msg_input)
        except Exception as err:
            exception_heading(f'Error: {err}', wait_input=True)


class Portable(Functions):
    def __init__(self, file_name, setup, args=None, file_ext='.zip'):
        self.file_name = file_name
        self.setup = setup
        self.args = args
        self.file_ext = file_ext

        if os.path.exists(get_temp_path_by_file(file_name)):
            if len(os.listdir(get_temp_path_by_file(file_name))) > 0:
                log_show(f'Opening from existing {file_name}')
                self.run_program(file_name=os.path.join(get_temp_path_by_file(file_name), setup), args=args,
                                 is_portable=True)
                log_show(const.wait_msg)
                time.sleep(const.wait_long)
            else:
                find_files(file_name=file_name, file_ext=file_ext)
                log_show(f'Opening {file_name}')
                self.run_program(file_name=os.path.join(get_temp_path_by_file(file_name), setup), args=args,
                                 is_portable=True)
                log_show(const.wait_msg)
                time.sleep(const.wait_long)
        else:
            find_files(file_name=file_name, file_ext=file_ext)
            log_show(f'Opening {file_name}')
            self.run_program(file_name=os.path.join(get_temp_path_by_file(file_name), setup), args=args,
                             is_portable=True)
            log_show(const.wait_msg)
            time.sleep(const.wait_long)
