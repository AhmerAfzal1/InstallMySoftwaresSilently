import sys

from colorama import init

import constant as const
import functions as func
import main


def adobe_acrobat_pro(is_wait_long=True):
    software = func.Softwares(file_name=const.adobe_acrobat_pro, setup='Setup.exe', args=r'/S',
                              is_wait_long=is_wait_long)
    software.install()


def adobe_acrobat_reader(is_wait_long=True):
    software = func.Softwares(file_name=const.adobe_acrobat_reader, setup='Setup.exe', args=r'/S',
                              is_wait_long=is_wait_long)
    software.install()


def adobe_photoshop(is_wait_long=True):
    software = func.Softwares(file_name=const.adobe_photoshop, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    software.install()


def adobe_premiere(is_wait_long=True):
    software = func.Softwares(file_name=const.adobe_premiere, setup='Setup.exe', args=r'-S', is_wait_long=is_wait_long)
    software.install()


def adobe_xd(is_wait_long=True):
    software = func.Softwares(file_name=const.adobe_xd, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    software.install()


def corel_draw(is_wait_long=True):
    software = func.Softwares(file_name=const.corel_draw, setup='Setup.exe',
                              args=r'-y -nr -gm2 & "%SYSTEMDRIVE%\Temp\CORELDRAW\SETUP.exe" /S & RD /S /Q '
                                   r'"%SYSTEMDRIVE%\Temp\CORELDRAW"', is_wait_long=is_wait_long)
    software.install()


def ms_office(is_wait_long=True):
    software = func.Softwares(file_name=const.ms_office, setup=r'Office\helper.exe',
                              args=r'/S /INSTALL /PROX64 /WORD /EXCEL /POWERPOINT /PUBLISHER /LANG=EN-US /KMS',
                              is_wait_long=is_wait_long)
    software.install()


def main_program():
    func.set_console_title(const.heading_major)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_major)
            func.back_heading()
            func.sub_heading_softwares('02', const.ms_office)
            func.sub_heading_softwares('03', const.adobe_acrobat_reader)
            func.sub_heading_softwares('04', const.adobe_acrobat_pro)
            func.sub_heading_softwares('05', const.adobe_photoshop)
            func.sub_heading_softwares('06', const.adobe_xd)
            func.sub_heading_softwares('07', const.corel_draw)
            func.sub_heading_softwares('08', const.adobe_premiere)
            exit_code = func.exit_heading('09')

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
                ms_office()
                func.clear()
                continue

            elif choice == 3:
                adobe_acrobat_reader()
                func.clear()
                continue

            elif choice == 4:
                adobe_acrobat_pro()
                func.clear()
                continue

            elif choice == 5:
                adobe_photoshop()
                func.clear()
                continue

            elif choice == 6:
                adobe_xd()
                func.clear()
                continue

            elif choice == 7:
                corel_draw()
                func.clear()
                continue

            elif choice == 8:
                adobe_premiere()
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
