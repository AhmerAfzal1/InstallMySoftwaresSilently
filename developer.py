import re
import sys

from colorama import init

import constant as const
import functions as func
import main


def android_studio(is_wait_long=True):
    software = func.Softwares(file_name=const.android_studio, setup='Setup.exe', args=r'/S /Allusers',
                              is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('android_studio', const.android_studio)


def git(is_wait_long=True):
    # If not provide *.reg file in variable registry='reg.reg' than optionally use winreg for it
    software = func.Softwares(file_name=const.git, setup='Setup.exe',
                              args=r'/VERYSILENT /NORESTART /NOCANCEL /SP- /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS '
                                   r'/COMPONENTS="icons,icons\desktop,ext,ext\reg,ext\reg\shellhere,assoc,assoc_sh,'
                                   r'consolefont"',
                              another_task=func.AnOtherTask.REG_GIT, is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('git', const.git)


def java_jdk(file_name, is_wait_long=True):
    software = func.Softwares(file_name=file_name, setup='Setup.exe',
                              args=r'/s ADDLOCAL="ToolsFeature,SourceFeature"', another_task=func.AnOtherTask.JAVA,
                              is_wait_long=is_wait_long)
    is_installed = software.install()
    regex_compile = re.compile(r'[\d.]+', re.IGNORECASE)
    output = re.findall(regex_compile, file_name)
    if is_wait_long and is_installed and output[0] == 8:
        func.Softwares.update_record('java_jdk_08', const.java_jdk_08)


def notepad_p_p(is_wait_long=True):
    software = func.Softwares(file_name=const.notepad_p_p, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('notepad_p_p', const.notepad_p_p)


def pycharm(is_wait_long=True):
    software = func.Softwares(file_name=const.pycharm, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('pycharm', const.pycharm)


def python(is_wait_long=True):
    software = func.Softwares(file_name=const.python, setup='Setup.exe', is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('python', const.python)


def sq_lite(is_wait_long=True):
    software = func.Softwares(file_name=const.sq_lite, setup='Setup.exe', args=const.common_arg,
                              another_task=func.AnOtherTask.SQLITE, is_wait_long=is_wait_long)
    software.install()


def main_program():
    func.set_console_title(const.heading_developer)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_developer)
            func.back_heading()
            func.sub_heading_softwares('02', const.android_studio)
            func.sub_heading_softwares('03', const.java_jdk_08)
            func.sub_heading_softwares('04', const.python)
            func.sub_heading_softwares('05', const.git)
            func.sub_heading_softwares('06', const.notepad_p_p)
            func.sub_heading_softwares('07', const.pycharm)
            func.sub_heading_softwares('08', const.java_jdk_15)
            func.sub_heading_softwares('09', const.sq_lite)
            exit_code = func.exit_heading('10')

            choice = func.input_heading()

            if choice == 0:
                func.exception_heading(const.heading_zero)
                input()
                func.clear()
                continue

            elif choice == 1:
                func.clear()
                main.main()
                break

            elif choice == 2:
                android_studio()
                func.clear()
                continue

            elif choice == 3:
                java_jdk(const.java_jdk_08)
                func.clear()
                continue

            elif choice == 4:
                python()
                func.clear()
                continue

            elif choice == 5:
                git()
                func.clear()
                continue

            elif choice == 6:
                notepad_p_p()
                func.clear()
                continue

            elif choice == 7:
                pycharm()
                func.clear()
                continue

            elif choice == 8:
                java_jdk(const.java_jdk_15)
                func.clear()
                continue

            elif choice == 9:
                sq_lite()
                func.clear()
                continue

            elif choice == int(exit_code):
                func.remove_temp(is_wait=True)
                sys.exit()

            else:
                func.exception_range_heading(exit_code)
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f'Please input a number. {err}')
            input()
            func.clear()
