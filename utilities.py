import sys
import time

from colorama import init

import constant as const
import functions as func
import main


def aomei_partition(is_wait_long=True):
    software = func.Softwares(file_name=const.aomei_partition, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    software.install()


def auslogics_duplicate(is_wait_long=True):
    software = func.Softwares(file_name=const.auslogics_duplicate, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()


def better_rename(is_wait_long=True):
    software = func.Softwares(file_name=const.better_rename, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()
    time.sleep(const.wait_short * 2)
    func.Softwares(file_name=const.better_rename, setup='Serial.txt').portable()


def c_cleaner(is_wait_long=True):
    software = func.Softwares(file_name=const.c_cleaner, setup='Setup.exe', args=r'/S /IB /TM',
                              is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('c_cleaner', const.c_cleaner)


def cpu_z():
    software = func.Softwares(file_name=const.cpu_z, setup='cpuz_x64.exe')
    software.portable()


def dism_p_p():
    software = func.Softwares(file_name=const.dism_p_p, setup='Dism++x64.exe')
    software.portable()


def eng_to_urdu_dic(is_wait_long=True):
    software = func.Softwares(file_name=const.eng_to_urdu_dic, setup='Setup.exe', args=r'/exenoui',
                              is_wait_long=is_wait_long)
    software.install()


def fonts(is_wait_long=True):
    software = func.Softwares(file_name=const.fonts, setup='Setup.exe', is_wait_long=is_wait_long)
    software.install()


def hw_info():
    software = func.Softwares(file_name=const.hw_info, setup='HWiNFO64.exe')
    software.portable()


def occt_checking_tool():
    software = func.Softwares(file_name=const.occt_checking_tool, setup='OCCT.exe')
    software.portable()


def power_iso(is_wait_long=True):
    software = func.Softwares(file_name=const.power_iso, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('power_iso', const.power_iso)


def print_conductor(is_wait_long=True):
    software = func.Softwares(file_name=const.print_conductor, setup='Setup.exe', args=const.common_arg,
                              is_wait_long=is_wait_long)
    software.install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.print_conductor, setup='Keygen.exe').portable()


def rufus():
    software = func.Softwares(file_name=const.rufus, setup='Rufus.exe')
    software.portable()


def seven_zip(is_wait_long=True):
    software = func.Softwares(file_name=const.seven_zip, setup='Setup.exe', args=r'/S', is_wait_long=is_wait_long)
    software.install()


def vs_redistributable(is_wait_long=True):
    func.Softwares(file_name=const.vs_redistributable, setup='Setup-2005.exe', args=r'/Q',
                   is_wait_long=is_wait_long).install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.vs_redistributable, setup='Setup-2008.exe', args=r'/Q',
                   is_wait_long=is_wait_long).install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.vs_redistributable, setup='Setup-2010.exe', args=r'/Q /NORESTART',
                   is_wait_long=is_wait_long).install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.vs_redistributable, setup='Setup-2012.exe', args=r'/INSTALL /QUIET /NORESTART',
                   is_wait_long=is_wait_long).install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.vs_redistributable, setup='Setup-2013.exe', args=r'/INSTALL /QUIET /NORESTART',
                   is_wait_long=is_wait_long).install()
    time.sleep(const.wait_short)
    func.Softwares(file_name=const.vs_redistributable, setup='Setup-2019.exe', args=r'/INSTALL /QUIET /NORESTART',
                   is_wait_long=is_wait_long).install()
    if is_wait_long:
        func.Softwares.update_record('vc_redist', const.vs_redistributable)


def winrar(is_wait_long=True):
    software = func.Softwares(dir_name=const.winrar, setup='Setup.exe', args=r'/S /IEN',
                              another_task=func.AnOtherTask.WINRAR_KEY, is_wait_long=is_wait_long)
    is_installed = software.install()
    if is_wait_long and is_installed:
        func.Softwares.update_record('winrar', const.winrar)


def wise_duplicate(is_wait_long=True):
    software = func.Softwares(file_name=const.wise_duplicate, setup='Setup.exe', args=const.common_arg,
                              another_task=func.AnOtherTask.WISE_DUPLICATE, is_wait_long=is_wait_long)
    software.install()


def main_program():
    func.set_console_title(const.heading_utilities)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_utilities)
            func.back_heading()
            func.sub_heading_softwares('02', const.c_cleaner)
            func.sub_heading_softwares('03', const.power_iso)
            func.sub_heading_softwares('04', const.fonts)
            func.sub_heading_softwares('05', const.winrar)
            func.sub_heading_portable('06', const.dism_p_p)
            func.sub_heading_softwares('07', const.eng_to_urdu_dic)
            func.sub_heading_portable('08', const.cpu_z)
            func.sub_heading_portable('09', const.hw_info)
            func.sub_heading_softwares('10', const.aomei_partition)
            func.sub_heading_portable('11', const.rufus)
            func.sub_heading_softwares('12', const.seven_zip)
            func.sub_heading_softwares('13', const.vs_redistributable)
            func.sub_heading_softwares('14', const.better_rename)
            func.sub_heading_softwares('15', const.auslogics_duplicate)
            func.sub_heading_softwares('16', const.print_conductor)
            func.sub_heading_softwares('17', const.wise_duplicate)
            func.sub_heading_portable('18', const.occt_checking_tool)
            exit_code = func.exit_heading('19')

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
                c_cleaner()
                func.clear()
                continue

            elif choice == 3:
                power_iso()
                func.clear()
                continue

            elif choice == 4:
                fonts()
                func.clear()
                continue

            elif choice == 5:
                winrar()
                func.clear()
                continue

            elif choice == 6:
                dism_p_p()
                func.clear()
                continue

            elif choice == 7:
                eng_to_urdu_dic()
                func.clear()
                continue

            elif choice == 8:
                cpu_z()
                func.clear()
                continue

            elif choice == 9:
                hw_info()
                func.clear()
                continue

            elif choice == 10:
                aomei_partition()
                func.clear()
                continue

            elif choice == 11:
                rufus()
                func.clear()
                continue

            elif choice == 12:
                seven_zip()
                func.clear()
                continue

            elif choice == 13:
                vs_redistributable()
                func.clear()
                continue

            elif choice == 14:
                better_rename()
                func.clear()
                continue

            elif choice == 15:
                auslogics_duplicate()
                func.clear()
                continue

            elif choice == 16:
                print_conductor()
                func.clear()
                continue

            elif choice == 17:
                wise_duplicate()
                func.clear()
                continue

            elif choice == 18:
                occt_checking_tool()
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
