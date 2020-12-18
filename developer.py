import sys

from colorama import init

import constant as const
import functions as func
import main


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
            func.eixt_heading('09')

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
                func.InstallSoftware(file_name=const.android_studio, setup='Setup.exe', args=r'/S /Allusers')
                func.clear()
                continue

            elif choice == 3:
                func.InstallSoftware(file_name=const.java_jdk_08, setup='Setup.exe',
                                     args=r'/s ADDLOCAL="ToolsFeature,SourceFeature"',
                                     another_task=func.AnOtherTask.JAVA)
                func.clear()
                continue

            elif choice == 4:
                func.InstallSoftware(file_name=const.python, setup='Setup.exe')
                func.clear()
                continue

            elif choice == 5:
                # If not provide *.reg file in variable registry='reg.reg' than optionally use winreg for it
                func.InstallSoftware(file_name=const.git, setup='Setup.exe',
                                     args=r'/VERYSILENT /NORESTART /NOCANCEL /SP- /CLOSEAPPLICATIONS '
                                          r'/RESTARTAPPLICATIONS /COMPONENTS="icons,icons\desktop,ext,ext\reg,'
                                          r'ext\reg\shellhere,assoc,assoc_sh,consolefont"',
                                     another_task=func.AnOtherTask.REG_GIT)
                func.clear()
                continue

            elif choice == 6:
                func.InstallSoftware(file_name=const.notepad_p_p, setup='Setup.exe', args=r'/S')
                func.clear()
                continue

            elif choice == 7:
                func.InstallSoftware(file_name=const.pycharm, setup='Setup.exe', args=r'/S')
                func.clear()
                continue

            elif choice == 8:
                func.InstallSoftware(file_name=const.java_jdk_15, setup='Setup.exe',
                                     args=r'/s ADDLOCAL="ToolsFeature,SourceFeature"',
                                     another_task=func.AnOtherTask.JAVA)
                func.clear()
                continue

            elif choice == 9:
                func.remove_temp(is_wait=True)
                sys.exit()

            else:
                func.exception_range_heading(1, 8)
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f'Please input a number')
            func.exception_heading(f'Error: {err}')
            input()
            func.clear()
