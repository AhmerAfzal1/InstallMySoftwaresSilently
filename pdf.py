import sys

from colorama import init

import constant as const
import functions as func
import main

doro_pdf_writer = 'Doro PDF Writer 2.15.0'
foxit_adv_pdf_editor = 'Foxit Advanced PDF Editor 3.10'
infix_pdf_editor = 'Infix PDF Editor Pro 7.4.0'
pdf_creator = 'PDFCreator 3.4.1'
pdf_shaper = 'PDF Shaper Pro 8.9'
pdf_to_jpg = 'PDF to JPG 2.9.10'
pdf_to_jpg_converter = 'PDF To JPG Converter 4.3.1'


def main_program():
    func.set_console_title(const.heading_pdf)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_pdf)
            func.back_heading()
            func.sub_heading_softwares('02', foxit_adv_pdf_editor)
            func.sub_heading_softwares('03', infix_pdf_editor)
            func.sub_heading_softwares('04', pdf_creator)
            func.sub_heading_softwares('05', pdf_shaper)
            func.sub_heading_softwares('06', pdf_to_jpg)
            func.sub_heading_softwares('07', pdf_to_jpg_converter)
            func.sub_heading_softwares('08', doro_pdf_writer)
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
                func.install_software(file_name=foxit_adv_pdf_editor, setup='Setup.exe', args='/S')
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=infix_pdf_editor, setup='Setup.exe', args='/S /EN')
                func.clear()
                continue

            elif choice == 4:
                func.install_software(file_name=infix_pdf_editor, setup='Setup.exe',
                                      args='/SILENT /NORESTART /NOCLOSEAPPLICATIONS /NORESTARTAPPLICATIONS')
                func.clear()
                continue

            elif choice == 5:
                func.install_software(file_name=pdf_shaper, setup='Setup.exe', args='/silent')
                func.clear()
                continue

            elif choice == 6:
                func.install_software(file_name=pdf_to_jpg, setup='Setup.exe', args='/silent')
                func.clear()
                continue

            elif choice == 7:
                func.install_software(file_name=pdf_to_jpg_converter, setup='Setup.exe', args='/silent')
                func.clear()
                continue

            elif choice == 8:
                func.install_software(file_name=doro_pdf_writer, setup='Setup.exe', args='/silent')
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
