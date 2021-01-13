import sys
import time

from colorama import init

import constant as const
import functions as func
import main


def android_iphone(is_wait_long=True):
    func.InstallSoftware(file_name=const.android_iphone, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)


def i_mobie(is_wait_long=True):
    func.InstallSoftware(file_name=const.i_mobie, setup='Setup.exe', args=const.common_arg, is_wait_long=is_wait_long)


def i_tunes(is_wait_long=True):
    func.InstallSoftware(file_name=const.i_tunes, setup='Setup.exe', args=r'/qn /norestart', is_wait_long=is_wait_long)


def samsung_usb(is_wait_long=True):
    func.InstallSoftware(file_name=const.samsung_usb, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)


def smart_switch(is_wait_long=True):
    func.InstallSoftware(file_name=const.smart_switch, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)


def sms_contacts_recover(is_wait_long=True):
    func.InstallSoftware(file_name=const.sms_contacts_recover, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    time.sleep(const.wait_short)
    func.Portable(file_name=const.sms_contacts_recover, setup='Patch.exe')


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
            func.sub_heading_softwares('05', const.sms_contacts_recover)
            func.sub_heading_softwares('06', const.i_mobie)
            exit_code = func.exit_heading('07')

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

            elif choice == 5:
                sms_contacts_recover()
                func.clear()
                continue

            elif choice == 6:
                i_mobie()
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
