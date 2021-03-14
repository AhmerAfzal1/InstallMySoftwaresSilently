import datetime
import enum
import glob
import inspect
import os
import re
import shlex
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import winreg as reg
import zipfile

from colorama import init, Fore, Style

import constant as const
import developer
import internet
import main
import mobile
import multimedia
import utilities

init()
current_db_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
temp = os.path.join(tempfile.gettempdir(), const.product)
if not os.path.exists(temp):
    os.makedirs(temp)


def center_text(string):
    print(string.center(shutil.get_terminal_size().columns))


def clear():
    if os.name == 'nt':
        os.system('cls')


def connect_db(show_log=True):
    if show_log:
        log_show('Connecting to database...')
    connect = sqlite3.connect(const.db_name)
    cursor = connect.cursor()
    if show_log:
        time.sleep(const.wait_short)
        log_show('Connected to database')
    return connect, cursor


def copying_files(src, dst):
    try:
        if os.path.isfile(src) and os.path.exists(dst):
            d = shutil.copy(src=src, dst=dst)
            if os.path.isfile(d):
                return True
            else:
                return False
    except PermissionError as err:
        err_type, err_object, err_traceback = sys.exc_info()
        file_name = err_traceback.tb_frame.f_code.co_filename
        line_number = err_traceback.tb_lineno
        exception_heading(f'You haven\'t permission \n Syntax is: {err} \n Exception type: {err_type}'
                          f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)


def extract_archive(root, file_name, pwd=None):
    start_unzip = time.time()
    log_show(f'Extracting to {get_temp_path(file_name)}')
    zip_file = zipfile.ZipFile(file=os.path.join(root, file_name), mode='r')
    try:
        if pwd is not None:
            zip_file.setpassword(pwd=bytes(pwd, encoding=const.encode_utf_8))
        zip_file.extractall(path=temp)
    except zipfile.error as err_zip:
        err_type, err_object, err_traceback = sys.exc_info()
        file_name = err_traceback.tb_frame.f_code.co_filename
        line_number = err_traceback.tb_lineno
        exception_heading(f'Error while unzipping \n Syntax is: {err_zip} \n Exception type: {err_type}'
                          f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)
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
                            return True
        else:
            exception_heading(f'Extension for {file_name + file_ext} is unsupported format, please use zip archive')
    except Exception as err:
        err_type, err_object, err_traceback = sys.exc_info()
        file_name = err_traceback.tb_frame.f_code.co_filename
        line_number = err_traceback.tb_lineno
        exception_heading(f'Error while finding files \n Syntax is: {err} \n Exception type: {err_type}'
                          f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)


def get_date_time():
    return datetime.datetime.now().strftime('%d %b %Y %I:%M:%S %p')


def get_temp_drivers_path(file_name, drivers_dir, sub_drivers_dir=None):
    if sub_drivers_dir is not None:
        return os.path.join(*[get_temp_path(file_name), drivers_dir, sub_drivers_dir])
    else:
        return os.path.join(*[get_temp_path(file_name), drivers_dir])


def get_temp_path(file_name):
    return os.path.join(temp, file_name)


def get_time(start, end):
    t = end - start
    mins, secs = divmod(t, 60)
    if secs <= 1 and mins <= 0:
        return f'{secs:0.2f} Second'
    elif secs > 1 and mins <= 0:
        return f'{secs:0.2f} Seconds'
    elif mins <= 1 and secs <= 1:
        return f'{mins:0.0f} Minute and {secs:0.2f} Second'
    elif mins <= 1 and secs <= 59:
        return f'{mins:0.0f} Minute and {secs:0.2f} Seconds'
    else:
        return f'{mins:0.0f} Minutes and {secs:0.2f} Seconds'


def get_var_name(var_name):
    for name in globals():
        if eval(name) == var_name:
            return name


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


def task_kill(task):
    start = time.time()
    kill = subprocess.check_output('tasklist')
    if task in str(kill):
        log_show(f'Killing task {task}...')
        time.sleep(const.wait_short)
        subprocess.run(['taskkill', '/F', '/IM', task, '>nul'])
        end = time.time()
        log_show(f'Killed task {task} in ', get_time(start, end))
        return True
    else:
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


def main_heading_log_view(num):
    print(f'{Fore.CYAN}\t[{num}] Log View From Database{Style.RESET_ALL} ')


def sub_heading(string):
    center_text(f'{Fore.LIGHTGREEN_EX}Categorized List of {string} Softwares{Style.RESET_ALL}')
    print('\n')


def sub_heading_portable(num, string):
    print(f'{Fore.LIGHTGREEN_EX}\t[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Program{Style.RESET_ALL} '
          f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}(Portable){Style.RESET_ALL}')


def sub_heading_softwares(num, string, option_string=None):
    if option_string is None:
        print(f'{Fore.LIGHTGREEN_EX}\t[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Install{Style.RESET_ALL} '
              f'{Fore.LIGHTGREEN_EX}{string}{Style.RESET_ALL}')
    else:
        print(f'{Fore.LIGHTGREEN_EX}\t[{num}]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Install{Style.RESET_ALL} '
              f'{Fore.LIGHTGREEN_EX}{string} ({option_string}){Style.RESET_ALL}')


def under_progress_heading(string, wait_input=False):
    print(f'\n{Fore.CYAN} {string}{Style.RESET_ALL}')
    if wait_input:
        input(const.wait_msg_input)


class AnOtherTask(enum.Enum):
    ANDROID_IPHONE = 'androidiphone'
    AOMEI_PRO = 'pro'
    AOMEI_SERVER = 'server'
    AOMEI_TECHNICIAN = 'technician'
    AOMEI_UNLIMITED = 'unlimited'
    FONEPAW = 'fonepaw'
    HELIUM_MUSIC = 'helium'
    IDM = 'idm'
    JAVA = 'java'
    NETSETMAN = 'netsetman'
    REA_CONVERTER = 'rea'
    REG_GIT = 'gitbash'
    SQLITE = 'sqlite'
    TRI_SUN_PDF = 'trysun'
    WINRAR_KEY = 'rar'
    WISE_DUPLICATE = 'wiseduplicate'


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
            setx_jdk = ''
            setx_jre = ''
            java_home = 'JAVA_HOME'
            java_jre = 'JAVA_JRE'
            compile_jdk = re.compile(r'[\d.]+', re.IGNORECASE)
            output = re.findall(compile_jdk, file_name)
            new_output = re.findall(compile_jdk, output[0])
            try:
                if int(new_output[0]) == int(JavaVersion.JAVA_8.value):
                    setx_jdk_08 = os.path.join(*[os.environ['ProgramFiles'], 'Java', f'jdk1.8.0_{output[1]}'])
                    setx_jre_08 = os.path.join(*[os.environ['ProgramFiles'], 'Java', f'jre1.8.0_{output[1]}'])
                    setx_jdk = setx_jdk_08
                    setx_jre = setx_jre_08
                    os.environ[java_home] = setx_jdk
                    os.environ[java_jre] = setx_jre
                elif int(new_output[0]) == int(JavaVersion.JAVA_15.value):
                    setx_jdk_15 = os.path.join(*[os.environ['ProgramFiles'], 'Java', f'jdk-{output[0]}'])
                    setx_jre_15 = os.path.join(*[os.environ['ProgramFiles'], 'Java', f'jre-{output[0]}'])
                    setx_jdk = setx_jdk_15
                    setx_jre = setx_jre_15
                    os.environ[java_home] = setx_jdk
                    os.environ[java_jre] = setx_jre
                time.sleep(const.wait_short)
                log_show(f'Modified {java_home}: {setx_jdk}')
                log_show(f'Modified {java_jre}: {setx_jre}')
            except KeyError:
                exception_heading(f'Key {setx_jdk} or {setx_jre} does not exist')
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
            patcher_dir = os.path.join(*[os.environ['ProgramFiles(x86)'], 'Internet Download Manager'])
            subprocess.run(
                [os.path.join(get_temp_path(file_name), 'Patch.exe'), '/silent', '/overwrite', '/backup',
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
            path = os.path.join(*[get_temp_path(file_name), child_file])
            Functions.run_program(file_name=sys_app, path=path, sys_app_run=True)
            time.sleep(const.wait_short)
        elif task.value == AnOtherTask.ANDROID_IPHONE.value:
            log_show(f'Cracking {file_name}')
            for file in os.listdir(os.path.join(*[temp, file_name, 'Crack'])):
                src = os.path.join(*[temp, file_name, 'Crack', file])
                dst = os.path.join(*[os.environ['LOCALAPPDATA'], 'Backuptrans Android iPhone Line Transfer + (x64)'])
                is_copied = copying_files(src=src, dst=dst)
                if is_copied:
                    log_show(f'Copied crack file to {dst}')
            time.sleep(const.wait_short)
        elif task.value == AnOtherTask.SQLITE.value:
            log_show(f'Cracking {file_name}')
            src = os.path.join(*[temp, file_name, 'license3.key'])
            dst = os.path.join(*[os.environ['ProgramFiles'], 'SQLite Expert', 'Professional 5'])
            is_copied = copying_files(src=src, dst=dst)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied crack file to {dst}')
        elif task.value == AnOtherTask.WISE_DUPLICATE.value:
            log_show(f'Registering {file_name}')
            subprocess.run(
                [os.path.join(get_temp_path(file_name), 'Activator.exe'), '/activate', f'/name {const.author}',
                 f'/email {const.email}', '/overwrite', '/patchhosts', '/generate', '/product 3', '/verysilent'],
                shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(const.wait_short)
        elif task.value == AnOtherTask.NETSETMAN.value:
            log_show(f'Cracking {file_name}')
            for file in os.listdir(os.path.join(*[temp, file_name, 'Crack'])):
                src = os.path.join(*[temp, file_name, 'Crack', file])
                dst = os.path.join(*[os.environ['ProgramFiles(x86)'], 'NetSetMan Pro'])
                is_copied = copying_files(src=src, dst=dst)
                if is_copied:
                    log_show(f'Copied crack file to {dst}')
            time.sleep(const.wait_short)
        elif task.value == AnOtherTask.FONEPAW.value:
            log_show(f'Cracking {file_name}')
            for file in os.listdir(os.path.join(*[temp, file_name, 'Crack'])):
                src = os.path.join(*[temp, file_name, 'Crack', file])
                dst = os.path.join(*[os.environ['ProgramFiles(x86)'], 'FonePaw', 'FonePaw iPhone Data Recovery'])
                is_copied = copying_files(src=src, dst=dst)
                if is_copied:
                    log_show(f'Copied crack file to {dst}')
            time.sleep(const.wait_short)
        elif task.value == AnOtherTask.REA_CONVERTER.value:
            log_show(f'Cracking {file_name}')
            src = os.path.join(*[temp, file_name, 'reaconverter7_pro_loader.exe'])
            dst = os.path.join(*[os.environ['ProgramFiles(x86)'], 'reaConverter 7 Pro'])
            is_copied = copying_files(src=src, dst=dst)
            time.sleep(const.wait_short)
            if is_copied:
                log_show(f'Copied crack file to {dst}')
        else:
            exception_heading(f'Invalid AnOtherTask type')
            time.sleep(const.wait_short)
            pass


class Softwares(Functions):
    db_file = glob.glob(os.path.join(*[current_db_dir, const.db_name]))

    def __init__(self, another_task=None, args=None, child_file=None, dir_name=None, driver_dir=None, ext='.zip',
                 file_name=None, is_wait_long=None, pwd=None, registry=None, setup=None, sub_dri_dir=None, sys_app=None,
                 wait_input=False, wait=0):
        self.another_task = another_task
        self.args = args
        self.child_file = child_file
        self.dir_name = dir_name
        self.driver_dir = driver_dir
        self.ext = ext
        self.file_name = file_name
        self.is_wait_long = is_wait_long
        self.pwd = pwd
        self.registry = registry
        self.setup = setup
        self.sub_dri_dir = sub_dri_dir
        self.sys_app = sys_app
        self.wait = wait
        self.wait_input = wait_input

    def install(self):
        if not self.db_file:
            self.create_db()
        connection, cursor = connect_db(show_log=False)
        date_time = get_date_time()
        logs = '----------------- INSTALLATION -----------------'
        try:
            start = time.time()
            is_exist_file = None
            is_found_file = None
            is_skip_process = None
            if self.dir_name is not None:  # For find directory
                log_search_dir = f'Searching directory {self.dir_name}...'
                logs += '\n' + log_search_dir
                log_show(log_search_dir)
                found_dir = find_files(dir_name=self.dir_name, file_ext=self.ext)
                end = time.time()
                log_found_dir = f'Found directory {self.dir_name} in '
                log_found_time = f'{get_time(start, end)}'
                logs += '\n' + log_found_dir + log_found_time
                log_show(log_found_dir, log_found_time)
                time.sleep(const.wait_short)
                if len(os.listdir(found_dir)):
                    log_install_dir = f'Installing from directory {found_dir}...'
                    logs += '\n' + log_install_dir
                    log_show(log_install_dir)
                    time.sleep(const.wait_short)
                    self.run_program(file_name=os.path.join(*[found_dir, self.setup]), args=self.args,
                                     is_portable=False)
                    if self.another_task is not None:
                        self.perform_another_task(task=self.another_task, dir_name=found_dir)
                    end = time.time()
                    log_install_success = f'Installed {self.dir_name} successfully in '
                    log_install_time = f'{get_time(start, end)}'
                    logs += '\n' + log_install_success + log_install_time
                    log_show(log_install_success, log_install_time)
                    log_show(const.wait_msg)
                    logs += '\n' + const.wait_msg
                    time.sleep(const.wait_long)
                else:
                    log_empty = f'{found_dir} is empty'
                    logs += '\n' + log_empty
                    log_show(log_empty)
            else:
                if self.driver_dir is not None:
                    log_searching_driver = f'Searching {self.file_name}...'
                    logs += '\n' + log_searching_driver
                    log_show(log_searching_driver)
                    if not os.path.exists(
                            get_temp_drivers_path(self.file_name, self.driver_dir, self.sub_dri_dir)):
                        find_files(dir_name=None, file_name=self.file_name, file_ext=self.ext)
                    if self.sub_dri_dir is not None:
                        if self.sub_dri_dir == os.path.join(*['APPS', 'PROSETDX', 'Winx64']):
                            log_install_dri = f'Installing {self.driver_dir} Drivers...'
                            logs += '\n' + log_install_dri
                            log_show(log_install_dri)
                        else:
                            log_install_sub_dri = f'Installing {self.sub_dri_dir} Drivers...'
                            logs += '\n' + log_install_sub_dri
                            log_show(log_install_sub_dri)
                    else:
                        log_install_drivers = f'Installing {self.driver_dir} Drivers...'
                        logs += '\n' + log_install_drivers
                        log_show(log_install_drivers)
                    time.sleep(const.wait_short)
                    self.run_program(file_name=os.path.join(
                        get_temp_drivers_path(self.file_name, self.driver_dir, sub_drivers_dir=self.sub_dri_dir),
                        self.setup), args=self.args, is_portable=False)
                    end = time.time()
                    log_installed_dri = f'Installed {self.driver_dir} successfully in '
                    log_installed_dri_time = f'{get_time(start, end)}'
                    logs += '\n' + log_installed_dri + log_installed_dri_time
                    log_show(log_installed_dri, log_installed_dri_time)
                else:
                    if not os.path.exists(get_temp_path(self.file_name)):
                        log_searching_file = f'Searching file {self.file_name}...'
                        logs += '\n' + log_searching_file
                        log_show(log_searching_file)
                        is_found_file = find_files(dir_name=None, file_name=self.file_name, file_ext=self.ext,
                                                   pwd=self.pwd)
                    else:
                        is_exist_file = True
                    if is_found_file or is_exist_file:
                        log_installing_file = f'Installing {self.file_name}...'
                        logs += '\n' + log_installing_file
                        log_show(log_installing_file)
                        self.run_program(file_name=os.path.join(get_temp_path(self.file_name), self.setup),
                                         args=self.args, is_portable=False)
                        time.sleep(const.wait_short)
                        if self.wait >= 1:
                            time.sleep(self.wait)
                        end = time.time()
                        log_installed_file = f'Installed {self.file_name} successfully in '
                        log_installed_file_time = f'{get_time(start, end)}'
                        logs += '\n' + log_installed_file + log_installed_file_time
                        log_show(log_installed_file, log_installed_file_time)
                        if self.registry is not None:
                            if os.path.isfile(os.path.join(*[get_temp_path(self.file_name), self.registry])):
                                log_reg = f'Installing registry {self.registry}...'
                                logs += '\n' + log_reg
                                log_show(log_reg)
                                time.sleep(const.wait_short)
                                os.startfile(get_temp_path(self.file_name), self.setup)
                            else:
                                log_reg_not_found = f'File {self.registry} not found'
                                logs += '\n' + log_reg_not_found
                                exception_heading(log_reg_not_found)
                        if self.another_task is not None:
                            self.perform_another_task(task=self.another_task, file_name=self.file_name,
                                                      sys_app=self.sys_app, child_file=self.child_file)
                        return True
                    else:
                        is_skip_process = True
                        log_file_not_found = f'{self.file_name} not found'
                        logs += '\n' + log_file_not_found
                        log_show(log_file_not_found)
                if is_skip_process is None:
                    if self.is_wait_long:
                        logs += '\n' + const.wait_msg
                        log_show(const.wait_msg)
                        time.sleep(const.wait_long)
                    else:
                        time.sleep(const.wait_long / 4)
                if self.wait_input or is_skip_process:
                    input(const.wait_msg_input)
        except Exception as err:
            err_type, err_object, err_traceback = sys.exc_info()
            file_name = err_traceback.tb_frame.f_code.co_filename
            line_number = err_traceback.tb_lineno
            log_exception = f'Error while installing software \n Syntax is: {err} \n Exception type: {err_type} \n ' \
                            f'File name: {file_name} \n Line number: {line_number} '
            logs += '\n' + log_exception
            exception_heading(log_exception, wait_input=True)
        finally:
            cursor.execute('INSERT INTO Log (DateTime, Logs) VALUES (\"%s\",\"%s\")' % (date_time, logs))
            connection.commit()
            cursor.close()
            connection.close()

    def portable(self):
        if os.path.exists(get_temp_path(self.file_name)):
            if len(os.listdir(get_temp_path(self.file_name))) > 0:
                log_show(f'Opening from existing {self.file_name}')
                self.run_program(file_name=os.path.join(get_temp_path(self.file_name), self.setup), args=self.args,
                                 is_portable=True)
                log_show(const.wait_msg)
                time.sleep(const.wait_long)
            else:
                find_files(file_name=self.file_name, file_ext=self.ext)
                log_show(f'Opening {self.file_name}')
                self.run_program(file_name=os.path.join(get_temp_path(self.file_name), self.setup), args=self.args,
                                 is_portable=True)
                log_show(const.wait_msg)
                time.sleep(const.wait_long)
        else:
            find_files(file_name=self.file_name, file_ext=self.ext)
            log_show(f'Opening {self.file_name}')
            self.run_program(file_name=os.path.join(get_temp_path(self.file_name), self.setup), args=self.args,
                             is_portable=True)
            log_show(const.wait_msg)
            time.sleep(const.wait_long)

    def create_db(self):
        if not self.db_file:
            connection, cursor = connect_db(show_log=False)
            try:
                log_show('Creating a new database...')
                db_ids = []
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS softwares
                    (
                    SoftwareId TEXT PRIMARY KEY NOT NULL,
                    SoftwareName TEXT NOT NULL,
                    CreationDate timestamp NOT NULL,
                    UpdateDate timestamp NOT NULL,
                    Status TEXT NOT NULL
                    );''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Log
                    (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    DateTime timestamp NOT NULL,
                    Logs TEXT
                    );''')
                log_show('A new empty database has been created')
                time.sleep(const.wait_short)
                for ids in cursor.execute('SELECT SoftwareId FROM softwares'):
                    db_ids.append(ids[0])
                for key_id, key_name in const.softwares_list.items():
                    date = get_date_time()
                    if key_id not in db_ids:
                        log_show(f'New software "{key_name}" is being added to the database...')
                        cursor.execute('INSERT INTO softwares VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")'
                                       % (key_id, key_name, date, date, const.db_msg_newly))
                        time.sleep(const.wait_short / 4)
                connection.commit()
                return True
            except sqlite3.Error as error:
                err_type, err_object, err_traceback = sys.exc_info()
                file_name = err_traceback.tb_frame.f_code.co_filename
                line_number = err_traceback.tb_lineno
                exception_heading(
                    f'Error while working with SQLite \n Syntax is: {error} \n Exception type: {err_type}'
                    f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)
            finally:
                cursor.close()
                connection.close()

        if self.db_file:
            connection, cursor = connect_db(show_log=False)
            try:
                db_ids = []
                log_show('Gathering softwares information...')
                get_len_db = cursor.execute('SELECT COUNT(*) FROM softwares').fetchone()[0]
                if not get_len_db == 0:
                    for ids in cursor.execute('SELECT SoftwareId FROM softwares'):
                        db_ids.append(ids[0])
                for key_id, key_name in const.softwares_list.items():
                    date = get_date_time()
                    if key_id not in db_ids:
                        log_show(f'New software "{key_name}" is being added to the database...')
                        cursor.execute('INSERT INTO softwares VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")'
                                       % (key_id, key_name, date, date, const.db_msg_newly))
                        time.sleep(const.wait_short / 4)
                    if not get_len_db == 0:
                        for record in cursor.execute('SELECT * FROM softwares WHERE "SoftwareId"=\"%s\"' % key_id):
                            db_name = record[1]
                            if not db_name == key_name:
                                cursor.execute('UPDATE softwares SET "SoftwareName"=\"%s\", "Status"=\"%s\" WHERE '
                                               '"SoftwareId"=\"%s\" ' % (key_name, const.db_msg_update_avail, key_id))
                                time.sleep(const.wait_short / 4)
                connection.commit()
                return False
            except sqlite3.Error as error:
                err_type, err_object, err_traceback = sys.exc_info()
                file_name = err_traceback.tb_frame.f_code.co_filename
                line_number = err_traceback.tb_lineno
                exception_heading(f'Error while working with SQLite \n Syntax is: {error} \n Exception type: {err_type}'
                                  f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)
            finally:
                cursor.close()
                connection.close()

    def update_install(self):
        is_newly_created_db = self.create_db()
        if not is_newly_created_db:
            connection, cursor = connect_db(show_log=True)
            new_update = False
            time.sleep(const.wait_short / 4)
            try:
                log_show('Checking new update(s) for software(s)...')
                for record in cursor.execute('SELECT * FROM softwares WHERE "Status"=\"%s\"'
                                             % const.db_msg_update_avail).fetchall():
                    db_id = record[0]
                    db_name = record[1]
                    db_date = record[3]
                    new_software_name = const.softwares_list[db_id]
                    date = get_date_time()
                    new_update = True
                    log_show(f'"{db_name}" was last updated on "{db_date}"')
                    if db_id == 'android_studio':
                        developer.android_studio(is_wait_long=False)
                    elif db_id == 'c_cleaner':
                        utilities.c_cleaner(is_wait_long=False)
                    elif db_id == 'firefox':
                        internet.firefox(is_wait_long=False)
                    elif db_id == 'idm':
                        internet.idm(is_wait_long=False)
                    elif db_id == 'java_jdk_08':
                        developer.java_jdk(const.java_jdk_08, is_wait_long=False)
                    elif db_id == 'k_lite':
                        multimedia.k_lite(is_wait_long=False)
                    elif db_id == 'notepad_p_p':
                        developer.notepad_p_p(is_wait_long=False)
                    elif db_id == 'os_build':
                        main.os_build(is_wait_long=False)
                    elif db_id == 'power_iso':
                        utilities.power_iso(is_wait_long=False)
                    elif db_id == 'pycharm':
                        developer.pycharm(is_wait_long=False)
                    elif db_id == 'python':
                        developer.python(is_wait_long=False)
                    elif db_id == 'samsung_usb':
                        mobile.samsung_usb(is_wait_long=False)
                    elif db_id == 'winrar':
                        utilities.winrar(is_wait_long=False)
                    elif db_id == 'git':
                        developer.git(is_wait_long=False)
                    elif db_id == 'vc_redist':
                        utilities.vs_redistributable(is_wait_long=False)
                    cursor.execute('UPDATE softwares SET "SoftwareName"=\"%s\", "UpdateDate"=\"%s\", "Status"=\"%s\" '
                                   'WHERE "SoftwareId"=\"%s\"' % (new_software_name, date, const.db_msg_updated, db_id))
                    log_show(f'Updated latest version of "{new_software_name}" in the database...')
                    connection.commit()
            except sqlite3.Error as error:
                err_type, err_object, err_traceback = sys.exc_info()
                file_name = err_traceback.tb_frame.f_code.co_filename
                line_number = err_traceback.tb_lineno
                exception_heading(f'Error while working with SQLite \n Syntax is: {error} \n Exception type: {err_type}'
                                  f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)
            finally:
                time.sleep(const.wait_long / 1.5)
                if not new_update:
                    log_show(f'There are no new software updates')
                    time.sleep(const.wait_long)
                cursor.close()
                connection.close()

    @staticmethod
    def update_record(key_id, key_name):
        connection, cursor = connect_db(show_log=True)
        try:
            date = get_date_time()
            log_show(f'Updating latest version of "{key_name}" in the database...')
            cursor.execute('UPDATE softwares SET "SoftwareName"=\"%s\", "UpdateDate"=\"%s\", "Status"=\"%s\" WHERE '
                           '"SoftwareId"=\"%s\"' % (key_name, date, const.db_msg_updated, key_id))
            connection.commit()
        except sqlite3.Error as error:
            err_type, err_object, err_traceback = sys.exc_info()
            file_name = err_traceback.tb_frame.f_code.co_filename
            line_number = err_traceback.tb_lineno
            exception_heading(f'Error while working with SQLite \n Syntax is: {error} \n Exception type: {err_type}'
                              f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)
        finally:
            time.sleep(const.wait_long / 1.5)
            cursor.close()
            connection.close()

    def get_logs(self):
        is_newly_created_db = self.create_db()
        if not is_newly_created_db:
            connection, cursor = connect_db(show_log=True)
            try:
                _id = None
                for log in cursor.execute('SELECT * FROM Log').fetchall():
                    _id = log[0]
                    data = log[1]
                    log_show(f'\t[{_id}] {data}')
                choice = int(input_heading())
                if choice == 0:
                    exception_heading(const.heading_zero)
                    input(const.wait_msg_input)
                    clear()
                else:
                    log_string = cursor.execute('SELECT Logs FROM Log WHERE "ID"=\"%s\"' % choice).fetchone()
                    log_show(log_string[0])
                    input(const.wait_msg_input)
            except sqlite3.Error as error:
                err_type, err_object, err_traceback = sys.exc_info()
                file_name = err_traceback.tb_frame.f_code.co_filename
                line_number = err_traceback.tb_lineno
                exception_heading(f'Error while working with SQLite \n Syntax is: {error} \n Exception type: {err_type}'
                                  f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)
            finally:
                cursor.close()
                connection.close()

    def update_test(self):
        is_newly_created_db = self.create_db()
        if not is_newly_created_db:
            connection, cursor = connect_db(show_log=True)
            try:
                log_show('Testing...')
                for record in cursor.execute('SELECT * FROM softwares WHERE "Status"=\"%s\"'
                                             % const.db_msg_update_avail).fetchall():
                    log_show(record[0] + ', ' + record[1] + ', ' + record[4])
                input(const.wait_msg_input)
            except sqlite3.Error as error:
                err_type, err_object, err_traceback = sys.exc_info()
                file_name = err_traceback.tb_frame.f_code.co_filename
                line_number = err_traceback.tb_lineno
                exception_heading(f'Error while working with SQLite \n Syntax is: {error} \n Exception type: {err_type}'
                                  f'\n File name: {file_name} \n Line number: {line_number}', wait_input=True)
            finally:
                cursor.close()
                connection.close()
