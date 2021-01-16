import sys

from colorama import init

import constant as const
import functions as func
import main


def rea_converter(is_wait_long=True):
    func.InstallSoftware(file_name=const.rea_converter, setup='Setup.exe', args=const.common_arg,
                         another_task=func.AnOtherTask.REA_CONVERTER, is_wait_long=is_wait_long)


def main_program():
    func.set_console_title(const.heading_converter)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_converter)
            func.back_heading()
            func.sub_heading_softwares('02', const.rea_converter, option_string='Photo Converter')
            exit_code = func.exit_heading('03')

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
                rea_converter()
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
