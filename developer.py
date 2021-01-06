import sys

from colorama import init

import constant as const
import functions as func
import main


def android_studio():
    func.InstallSoftware(file_name=const.android_studio, setup='Setup.exe', args=r'/S /Allusers')


def git():
    # If not provide *.reg file in variable registry='reg.reg' than optionally use winreg for it
    func.InstallSoftware(file_name=const.git, setup='Setup.exe',
                         args=r'/VERYSILENT /NORESTART /NOCANCEL /SP- /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS '
                              r'/COMPONENTS="icons,icons\desktop,ext,ext\reg,ext\reg\shellhere,assoc,assoc_sh,'
                              r'consolefont"',
                         another_task=func.AnOtherTask.REG_GIT)


def java_jdk(file_name):
    func.InstallSoftware(file_name=file_name, setup='Setup.exe',
                         args=r'/s ADDLOCAL="ToolsFeature,SourceFeature"', another_task=func.AnOtherTask.JAVA)


def notepad_p_p():
    func.InstallSoftware(file_name=const.notepad_p_p, setup='Setup.exe', args=r'/S')


def pycharm():
    func.InstallSoftware(file_name=const.pycharm, setup='Setup.exe', args=r'/S')


def python():
    func.InstallSoftware(file_name=const.python, setup='Setup.exe')


def sq_lite():
    func.InstallSoftware(file_name=const.sq_lite, setup='Setup.exe', args=const.common_arg,
                         another_task=func.AnOtherTask.SQLITE)


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
