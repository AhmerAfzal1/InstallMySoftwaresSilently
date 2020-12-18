import sys
import time

from colorama import init

import constant as const
import functions as func
import main


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
            func.eixt_heading('15')

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
                func.InstallSoftware(file_name=const.c_cleaner, setup='Setup.exe', args=r'/S /IB /TM')
                func.clear()
                continue

            elif choice == 3:
                func.InstallSoftware(file_name=const.power_iso, setup='Setup.exe', args=r'/S')
                func.clear()
                continue

            elif choice == 4:
                func.InstallSoftware(file_name=const.fonts, setup='Setup.exe')
                func.clear()
                continue

            elif choice == 5:
                func.InstallSoftware(dir_name=const.winrar, setup='Setup.exe', args=r'/S /IEN',
                                     another_task=func.AnOtherTask.WINRAR_KEY)
                func.clear()
                continue

            elif choice == 6:
                func.Portable(file_name=const.dism_p_p, setup='Dism++x64.exe')
                func.clear()
                continue

            elif choice == 7:
                func.InstallSoftware(file_name=const.eng_to_urdu_dic, setup='Setup.exe', args=r'/exenoui')
                func.clear()
                continue

            elif choice == 8:
                func.Portable(file_name=const.cpu_z, setup='cpuz_x64.exe')
                func.clear()
                continue

            elif choice == 9:
                func.Portable(file_name=const.hw_info, setup='HWiNFO64.exe')
                func.clear()
                continue

            elif choice == 10:
                func.InstallSoftware(file_name=const.aomei_partition, setup='Setup.exe', args=r'/SILENT',
                                     another_task=func.AnOtherTask.AOMEI_PRO)
                func.clear()
                continue

            elif choice == 11:
                func.Portable(file_name=const.rufus, setup='Rufus.exe')
                func.clear()
                continue

            elif choice == 12:
                func.InstallSoftware(file_name=const.seven_zip, setup='Setup.exe', args=r'/S')
                func.clear()
                continue

            elif choice == 13:
                func.InstallSoftware(file_name=const.vs_redistributable, setup='Setup.exe',
                                     args=r'/INSTALL /QUIET /NORESTART')
                func.clear()
                continue

            elif choice == 14:
                func.InstallSoftware(file_name=const.better_rename, setup='Setup.exe', args=r'/VERYSILENT /NORESTART')
                time.sleep(1)
                func.Portable(file_name=const.better_rename, setup='Serial.txt')
                func.clear()
                continue

            elif choice == 15:
                func.remove_temp(is_wait=True)
                sys.exit()

            else:
                func.exception_range_heading(1, 15)
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f'Please input a number')
            func.exception_heading(f'Error: {err}')
            input()
            func.clear()
