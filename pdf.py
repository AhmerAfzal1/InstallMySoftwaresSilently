import sys

from colorama import init

import constant as const
import functions as func
import main

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
                func.install_software(file_name=foxit_adv_pdf_editor, setup_with_arg='Setup.exe /S')
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=infix_pdf_editor, setup_with_arg='Setup.exe /S /EN')
                func.clear()
                continue

            elif choice == 4:
                func.install_software(file_name=infix_pdf_editor,
                                      setup_with_arg='Setup.exe /SILENT /NORESTART '
                                                     '/NOCLOSEAPPLICATIONS /NORESTARTAPPLICATIONS')
                func.clear()
                continue

            elif choice == 5:
                func.install_software(file_name=pdf_shaper, setup_with_arg='Setup.exe /silent')
                func.clear()
                continue

            elif choice == 6:
                func.install_software(file_name=pdf_to_jpg, setup_with_arg='Setup.exe /silent')
                func.clear()
                continue

            elif choice == 7:
                func.install_software(file_name=pdf_to_jpg_converter, setup_with_arg='Setup.exe /silent')
                func.clear()
                continue

            elif choice == 8:
                func.remove_temp()
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
