import sys

from colorama import init

import constant as const
import functions as func
import main

android_studio = 'Android Studio 4.1.0 (201.6858069)'
git = 'Git 2.29.2.2'
java_jdk = 'Java JDK 8 Update 271'
notepad_p_p = 'Notepad++ 7.9.1'
python = 'Python 3.9.0'


def main_program():
    func.set_console_title(const.heading_developer)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_developer)
            func.back_heading()
            func.sub_heading_softwares('02', android_studio)
            func.sub_heading_softwares('03', java_jdk)
            func.sub_heading_softwares('04', python)
            func.sub_heading_softwares('05', git)
            func.sub_heading_softwares('06', notepad_p_p)
            func.eixt_heading('07')

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
                func.install_software(file_name=android_studio, setup_with_arg='Setup.exe /S /Allusers')
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=java_jdk,
                                      setup_with_arg='Setup.exe /s ADDLOCAL="ToolsFeature,SourceFeature"',
                                      set_environ=func.SetX.JAVA)
                func.clear()
                continue

            elif choice == 4:
                func.install_software(file_name=python, setup_with_arg='Setup.exe')
                func.clear()
                continue

            elif choice == 5:
                # If not provide *.reg file in variable registry='reg.reg' than other option to use winreg for it
                func.install_software(file_name=git,
                                      setup_with_arg='Setup.exe /VERYSILENT /NORESTART /NOCANCEL /SP- '
                                                     '/CLOSEAPPLICATIONS /RESTARTAPPLICATIONS /COMPONENTS="icons,'
                                                     'icons\\desktop,ext,ext\\reg,ext\\reg\\shellhere,assoc,assoc_sh,'
                                                     'consolefont"',
                                      another_task=func.AnOtherTask.REG_GIT)
                func.clear()
                continue

            elif choice == 6:
                func.install_software(file_name=notepad_p_p, setup_with_arg='Setup.exe /S')
                func.clear()
                continue

            elif choice == 7:
                func.remove_temp()
                sys.exit()

            else:
                func.exception_range_heading(1, 7)
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f'Please input a number')
            func.exception_heading(f'Error: {err}')
            input()
            func.clear()
