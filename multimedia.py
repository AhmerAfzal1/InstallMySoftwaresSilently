import sys

from colorama import init

import constant as const
import functions as func
import main

k_lite = 'K-Lite Mega Codec Pack 15.9.0'
mp3_tag = 'Mp3Tag 3.04A'


def main_program():
    func.set_console_title(const.heading_multimedia)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_multimedia)
            func.back_heading()
            func.sub_heading_softwares('02', k_lite)
            func.sub_heading_softwares('03', mp3_tag)
            func.eixt_heading('04')

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
                func.install_software(file_name=k_lite, setup='Setup.exe', args='/verysilent')
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=mp3_tag, setup='Setup.exe', args='/S')
                func.clear()
                continue

            elif choice == 4:
                func.remove_temp(is_wait=True)
                sys.exit()

            else:
                func.exception_range_heading(1, 4)
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f'Please input a number')
            func.exception_heading(f'Error: {err}')
            input()
            func.clear()
