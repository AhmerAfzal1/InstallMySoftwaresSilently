import sqlite3
import sys
import time

from colorama import init

import constant as const
import functions as func
import main


def helium_music(is_wait_long=True):
    software = func.Softwares(file_name=const.helium_music, setup='Setup.exe', args=const.common_arg,
                              child_file='License.txt', sys_app='notepad.exe',
                              another_task=func.AnOtherTask.HELIUM_MUSIC,
                              is_wait_long=is_wait_long)
    software.install()


def k_lite(is_wait_long=True):
    software = func.Softwares(file_name=const.k_lite, setup='Setup.exe', args=r'/verysilent', is_wait_long=is_wait_long)
    software.install()
    if is_wait_long:
        connect, cursor = func.connect_db()
        try:
            date = func.get_date_time()
            key_id = 'k_lite'
            key_name = const.k_lite
            func.log_show(f'Updating latest version of "{key_name}" in the database...')
            cursor.execute('UPDATE softwares SET "name" = \"%s\", "datetime"= \"%s\" WHERE '
                           '"id" = \"%s\"' % (key_name, date, key_id))
            connect.commit()
        except sqlite3.Error as error:
            func.exception_heading(f'Error while working with SQLite {error}', wait_input=True)
        finally:
            time.sleep(const.wait_long / 2)
            cursor.close()
            connect.close()


def mp3_tag(is_wait_long=True):
    software = func.Softwares(file_name=const.mp3_tag, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    software.install()


def zortam_mp3(is_wait_long=True):
    software = func.Softwares(file_name=const.zortam_mp3, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.zortam_mp3, setup='Keygen.exe').portable()


def main_program():
    func.set_console_title(const.heading_multimedia)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_multimedia)
            func.back_heading()
            func.sub_heading_softwares('02', const.k_lite)
            func.sub_heading_softwares('03', const.mp3_tag)
            func.sub_heading_softwares('04', const.helium_music)
            func.sub_heading_softwares('05', const.zortam_mp3)
            exit_code = func.exit_heading('06')

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
                k_lite()
                func.clear()
                continue

            elif choice == 3:
                mp3_tag()
                func.clear()
                continue

            elif choice == 4:
                helium_music()
                func.clear()
                continue

            elif choice == 5:
                zortam_mp3()
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
