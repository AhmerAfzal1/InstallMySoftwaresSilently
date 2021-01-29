import sqlite3
import sys
import time

from colorama import init

import constant as const
import functions as func
import main


def chrome(is_wait_long=True):
    software = func.Softwares(file_name=const.chrome, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    software.install()


def firefox(is_wait_long=True):
    software = func.Softwares(file_name=const.firefox, setup='Setup.exe', args=r'-ms', is_wait_long=is_wait_long)
    software.install()
    if is_wait_long:
        connect, cursor = func.connect_db()
        try:
            date = func.get_date_time()
            key_id = 'firefox'
            key_name = const.firefox
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


def fdm(is_wait_long=True):
    software = func.Softwares(file_name=const.fdm, setup='Setup.exe', args=const.common_arg, is_wait_long=is_wait_long)
    software.install()


def idm(is_wait_long=True):
    func.task_kill('IDMan.exe')
    time.sleep(const.wait_short)
    software = func.Softwares(file_name=const.idm, setup='Setup.exe', args=r'/skipdlgs', wait=10,
                              another_task=func.AnOtherTask.IDM, is_wait_long=is_wait_long)
    software.install()
    if is_wait_long:
        connect, cursor = func.connect_db()
        try:
            date = func.get_date_time()
            key_id = 'idm'
            key_name = const.idm
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


def net_balancer(is_wait_long=True):
    software = func.Softwares(file_name=const.net_balancer, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()


def net_limiter(is_wait_long=True):
    software = func.Softwares(file_name=const.net_limiter, setup='Setup.exe', args=r'/EXENOUI /EXENOUPDATES',
                              another_task=func.AnOtherTask.NETSETMAN, is_wait_long=is_wait_long)
    software.install()


def net_set_man(is_wait_long=True):
    software = func.Softwares(file_name=const.net_set_man, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()


def main_program():
    func.set_console_title(const.heading_internet)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_internet)
            func.back_heading()
            func.sub_heading_softwares('02', const.firefox)
            func.sub_heading_softwares('03', const.idm)
            func.sub_heading_softwares('04', const.chrome)
            func.sub_heading_softwares('05', const.fdm)
            func.sub_heading_softwares('06', const.net_balancer)
            func.sub_heading_softwares('07', const.net_limiter)
            func.sub_heading_softwares('08', const.net_set_man)
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
                firefox()
                func.clear()
                continue

            elif choice == 3:
                idm()
                func.clear()
                continue

            elif choice == 4:
                chrome()
                func.clear()
                continue

            elif choice == 5:
                fdm()
                func.clear()
                continue

            elif choice == 6:
                net_balancer()
                func.clear()
                continue

            elif choice == 7:
                net_limiter()
                func.clear()
                continue

            elif choice == 8:
                net_set_man()
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
