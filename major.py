import sys

from colorama import init

import constant as const
import functions as func
import main

adobe_acrobat_pro = 'Adobe Acrobat Pro DC 2020.009.20067'
adobe_acrobat_reader = 'Adobe Acrobat Reader DC 2020.009.20067'
adobe_photoshop = 'Adobe Photoshop 2021 22.0.0.35'
adobe_xd = 'Adobe XD 34.1.12.9'
corel_draw = 'CorelDRAW Graphics Suite 2020 (22.1.0.517)'
ms_office = 'Microsoft Office 2016-2019 (2020.10)'


def main_program():
    func.set_console_title(const.heading_major)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_major)
            func.back_heading()
            func.sub_heading_softwares('02', ms_office)
            func.sub_heading_softwares('03', adobe_acrobat_reader)
            func.sub_heading_softwares('04', adobe_acrobat_pro)
            func.sub_heading_softwares('05', adobe_photoshop)
            func.sub_heading_softwares('06', adobe_xd)
            func.sub_heading_softwares('07', corel_draw)
            func.eixt_heading('08')

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
                func.install_software(file_name=ms_office, setup_with_arg='AUTORUN.exe')
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=adobe_acrobat_reader, setup_with_arg='Setup.exe /S')
                func.clear()
                continue

            elif choice == 4:
                func.install_software(file_name=adobe_acrobat_pro, setup_with_arg='Setup.exe /S')
                func.clear()
                continue

            elif choice == 5:
                func.install_software(file_name=adobe_photoshop, setup_with_arg='Setup.exe /S')
                func.clear()
                continue

            elif choice == 6:
                func.install_software(file_name=adobe_xd, setup_with_arg='Setup.exe /S')
                func.clear()
                continue

            elif choice == 7:
                func.install_software(file_name=corel_draw, setup_with_arg='Setup.exe /S')
                func.clear()
                continue

            elif choice == 8:
                func.remove_temp()
                sys.exit()

            else:
                func.exception_range_heading('1', '8')
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f'Please input a number')
            func.exception_heading(f'Error: {err}')
            input()
            func.clear()
