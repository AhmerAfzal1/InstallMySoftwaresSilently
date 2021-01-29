import ctypes
import os
import sys

from colorama import init

import constant as const
import converter
import developer
import functions as func
import internet
import major
import mobile
import multimedia
import pdf
import utilities


def make_font_bigger():
    lf_facesize = 32
    std_output_handle = -11

    class Coord(ctypes.Structure):
        _fields_ = [('X', ctypes.c_short), ('Y', ctypes.c_short)]

    class ConsoleFontInfoex(ctypes.Structure):
        _fields_ = [('cbSize', ctypes.c_ulong),
                    ('nFont', ctypes.c_ulong),
                    ('dwFontSize', Coord),
                    ('FontFamily', ctypes.c_uint),
                    ('FontWeight', ctypes.c_uint),
                    ('FaceName', ctypes.c_wchar * lf_facesize)]

    font = ConsoleFontInfoex()
    font.cbSize = ctypes.sizeof(ConsoleFontInfoex)
    font.nFont = 12
    font.dwFontSize.X = 11
    font.dwFontSize.Y = 16  # Font size value
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = 'Lucida Console'

    handle = ctypes.windll.kernel32.GetStdHandle(std_output_handle)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))


def os_build(is_wait_long=True):
    software = func.Softwares(file_name=const.os_build, setup='Setup.msu', args='/QUIET /NORESTART',
                              is_wait_long=is_wait_long)
    software.install()


def main():
    make_font_bigger()
    os.system('mode 120, 45')
    func.set_console_title(const.heading_main_title)
    init()
    while True:
        try:
            func.main_heading()
            func.main_heading_softwares('01', 'All Drivers & Recommended')
            func.main_heading_softwares('02', const.heading_converter)
            func.main_heading_softwares('03', const.heading_developer)
            func.main_heading_softwares('04', const.heading_internet)
            func.main_heading_softwares('05', const.heading_major)
            func.main_heading_softwares('06', const.heading_mobile)
            func.main_heading_softwares('07', const.heading_multimedia)
            func.main_heading_softwares('08', const.heading_pdf)
            func.main_heading_softwares('09', const.heading_utilities)
            func.main_heading_softwares('10', 'Recommended Newer Updated')
            exit_code = func.exit_heading('11')

            choice = func.input_heading()

            if choice == 0:
                func.exception_heading(const.heading_zero)
                input()
                func.clear()
                continue

            elif choice == 1:
                drivers = 'Drivers'
                func.Softwares(file_name=drivers, driver_dir='Audio', setup='Setup.exe', args=r'/S').install()
                func.Softwares(file_name=drivers, driver_dir='Chipset',
                               sub_dri_dir='Intel Active Management Technology', setup='Setup.exe',
                               args=r'-L 0409 -S').install()
                func.Softwares(file_name=drivers, driver_dir='Chipset', sub_dri_dir='Intel Chipset Device',
                               setup='Setup.exe', args=r'-L 0409 -S').install()
                func.Softwares(file_name=drivers, driver_dir='Graphics', setup='igxpin.exe',
                               args=r'-L enu -S').install()
                func.Softwares(file_name=drivers, driver_dir='Network',
                               sub_dri_dir=os.path.join(*['APPS', 'PROSETDX', 'Winx64']), setup='DxSetup.exe',
                               args=r'/QUIET /NORESTART').install()
                developer.git()
                developer.java_jdk(const.java_jdk_08)
                developer.notepad_p_p()
                developer.android_studio()
                internet.firefox()
                mobile.samsung_usb()
                multimedia.k_lite()
                utilities.c_cleaner()
                utilities.fonts()
                utilities.winrar()
                developer.python()
                developer.pycharm()
                func.clear()
                continue

            elif choice == 2:
                func.clear()
                converter.main_program()
                break

            elif choice == 3:
                func.clear()
                developer.main_program()
                break

            elif choice == 4:
                func.clear()
                internet.main_program()
                break

            elif choice == 5:
                func.clear()
                major.main_program()
                continue

            elif choice == 6:
                func.clear()
                mobile.main_program()
                continue

            elif choice == 7:
                func.clear()
                multimedia.main_program()
                continue

            elif choice == 8:
                func.clear()
                pdf.main_program()
                continue

            elif choice == 9:
                func.clear()
                utilities.main_program()
                continue

            elif choice == 10:
                func.Softwares().update_install()
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
