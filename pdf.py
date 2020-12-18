import sys

from colorama import init

import constant as const
import functions as func
import main


def main_program():
    func.set_console_title(const.heading_pdf)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_pdf)
            func.back_heading()
            func.sub_heading_softwares('02', const.foxit_adv_pdf_editor)
            func.sub_heading_softwares('03', const.infix_pdf_editor)
            func.sub_heading_softwares('04', const.pdf_creator)
            func.sub_heading_softwares('05', const.pdf_shaper)
            func.sub_heading_softwares('06', const.pdf_to_jpg)
            func.sub_heading_softwares('07', const.pdf_to_jpg_converter)
            func.sub_heading_softwares('08', const.doro_pdf_writer)
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
                func.InstallSoftware(file_name=const.foxit_adv_pdf_editor, setup='Setup.exe', args=r'/S')
                func.clear()
                continue

            elif choice == 3:
                func.InstallSoftware(file_name=const.infix_pdf_editor, setup='Setup.exe', args=r'/S /EN')
                func.clear()
                continue

            elif choice == 4:
                func.InstallSoftware(file_name=const.infix_pdf_editor, setup='Setup.exe',
                                     args=r'/SILENT /NORESTART /NOCLOSEAPPLICATIONS /NORESTARTAPPLICATIONS')
                func.clear()
                continue

            elif choice == 5:
                func.InstallSoftware(file_name=const.pdf_shaper, setup='Setup.exe', args=r'/silent')
                func.clear()
                continue

            elif choice == 6:
                func.InstallSoftware(file_name=const.pdf_to_jpg, setup='Setup.exe', args=r'/silent')
                func.clear()
                continue

            elif choice == 7:
                func.InstallSoftware(file_name=const.pdf_to_jpg_converter, setup='Setup.exe', args=r'/silent')
                func.clear()
                continue

            elif choice == 8:
                func.InstallSoftware(file_name=const.doro_pdf_writer, setup='Setup.exe', args=r'/silent')
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
