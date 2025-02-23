import sys
import time

from colorama import init

import constant as const
import functions as func
import main


def doro_pdf_writer(is_wait_long=True):
    software = func.Softwares(file_name=const.doro_pdf_writer, setup='Setup.exe', args=r'/silent',
                              is_wait_long=is_wait_long)
    software.install()


def foxit_adv_pdf_editor(is_wait_long=True):
    software = func.Softwares(file_name=const.foxit_adv_pdf_editor, setup='Setup.exe', args=r'/S',
                              is_wait_long=is_wait_long)
    software.install()


def infix_pdf_editor(is_wait_long=True):
    software = func.Softwares(file_name=const.infix_pdf_editor, setup='Setup.exe', args=r'/S /EN',
                              is_wait_long=is_wait_long)
    software.install()


def pdf_creator(is_wait_long=True):
    software = func.Softwares(file_name=const.infix_pdf_editor, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()


def pdf_shaper(is_wait_long=True):
    software = func.Softwares(file_name=const.pdf_shaper, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.pdf_shaper, setup='Patch.exe').portable()


def pdf_to_jpg(is_wait_long=True):
    software = func.Softwares(file_name=const.pdf_to_jpg, setup='Setup.exe', args=r'/silent', is_wait_long=is_wait_long)
    software.install()


def pdf_to_jpg_converter(is_wait_long=True):
    software = func.Softwares(file_name=const.pdf_to_jpg_converter, setup='Setup.exe', args=r'/silent',
                              is_wait_long=is_wait_long)
    software.install()


def tri_sun_pdf_to_jpg(is_wait_long=True):
    software = func.Softwares(file_name=const.tri_sun_pdf_to_jpg, setup='Setup.exe', args=const.common_arg,
                              another_task=func.AnOtherTask.TRI_SUN_PDF, is_wait_long=is_wait_long)
    software.install()


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
            func.sub_heading_softwares('06', const.tri_sun_pdf_to_jpg)
            func.sub_heading_softwares('07', const.pdf_to_jpg)
            func.sub_heading_softwares('08', const.pdf_to_jpg_converter)
            func.sub_heading_softwares('09', const.doro_pdf_writer)
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
                foxit_adv_pdf_editor()
                func.clear()
                continue

            elif choice == 3:
                infix_pdf_editor()
                func.clear()
                continue

            elif choice == 4:
                pdf_creator()
                func.clear()
                continue

            elif choice == 5:
                pdf_shaper()
                func.clear()
                continue

            elif choice == 6:
                tri_sun_pdf_to_jpg()
                func.clear()
                continue

            elif choice == 7:
                pdf_to_jpg()
                func.clear()
                continue

            elif choice == 8:
                pdf_to_jpg_converter()
                func.clear()
                continue

            elif choice == 9:
                doro_pdf_writer()
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
