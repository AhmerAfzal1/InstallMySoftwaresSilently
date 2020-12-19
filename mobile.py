import sys

from colorama import init

import constant as const
import functions as func
import main


def i_tunes():
    func.InstallSoftware(file_name=const.i_tunes, setup='Setup.exe', args=r'/qn /norestart')


def samsung_usb():
    func.InstallSoftware(file_name=const.samsung_usb, setup='Setup.exe', args=r'/S')


def smart_switch():
    func.InstallSoftware(file_name=const.smart_switch, setup='Setup.exe', args=r'/S')


def main_program():
    func.set_console_title(const.heading_mobile)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_mobile)
            func.back_heading()
            func.sub_heading_softwares('02', const.samsung_usb)
            func.sub_heading_softwares('03', const.smart_switch)
            func.sub_heading_softwares('04', const.i_tunes)
            exit_code = func.exit_heading('05')

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
                samsung_usb()
                func.clear()
                continue

            elif choice == 3:
                smart_switch()
                func.clear()
                continue

            elif choice == 4:
                i_tunes()
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
            func.exception_heading(f'Please input a number')
            func.exception_heading(f'Error: {err}')
            input()
            func.clear()
