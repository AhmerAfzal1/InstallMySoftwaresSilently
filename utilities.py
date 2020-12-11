import sys
import time

from colorama import init

import constant as const
import functions as func
import main

aomei_partition = 'AOMEI Partition Assistant 9.0'
better_rename = 'Better File Rename 6.18'
c_cleaner = 'CCleaner 5.75.8238'
cpu_z = 'CPU-Z 1.94.8'
dism_p_p = 'Dism++ 10.1.1001.10'
eng_to_urdu_dic = 'Cleantouch English to Urdu Dictionary 7.0'
fonts = 'Fonts'
hw_info = 'HWiNFO 6.40 Build 4330'
power_iso = 'PowerISO 7.8'
rufus = 'Rufus 3.13'
seven_zip = '7-Zip 19.00'
vs_redistributable = 'Microsoft Visual C++ 2015-2019 14.28.29617'
winrar = 'WinRAR 6.00'


def main_program():
    func.set_console_title(const.heading_utilities)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_utilities)
            func.back_heading()
            func.sub_heading_softwares('02', c_cleaner)
            func.sub_heading_softwares('03', power_iso)
            func.sub_heading_softwares('04', fonts)
            func.sub_heading_softwares('05', winrar)
            func.sub_heading_portable('06', dism_p_p)
            func.sub_heading_softwares('07', eng_to_urdu_dic)
            func.sub_heading_portable('08', cpu_z)
            func.sub_heading_portable('09', hw_info)
            func.sub_heading_softwares('10', aomei_partition)
            func.sub_heading_portable('11', rufus)
            func.sub_heading_softwares('12', seven_zip)
            func.sub_heading_softwares('13', vs_redistributable)
            func.sub_heading_softwares('14', better_rename)
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
                func.install_software(file_name=c_cleaner, setup='Setup.exe', args='/S /IB /TM')
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=power_iso, setup='Setup.exe', args='/S')
                func.clear()
                continue

            elif choice == 4:
                func.install_software(file_name=fonts, setup='Setup.exe')
                func.clear()
                continue

            elif choice == 5:
                func.install_software(dir_name=winrar, setup='Setup.exe', args='/S /IEN',
                                      another_task=func.AnOtherTask.WINRAR_KEY)
                func.clear()
                continue

            elif choice == 6:
                func.portable_crack_patch(file_name=dism_p_p, setup_with_arg='Dism++x64.exe')
                func.clear()
                continue

            elif choice == 7:
                func.install_software(file_name=eng_to_urdu_dic, setup='Setup.exe', args='/exenoui')
                func.clear()
                continue

            elif choice == 8:
                func.portable_crack_patch(file_name=cpu_z, setup_with_arg='cpuz_x64.exe')
                func.clear()
                continue

            elif choice == 9:
                func.portable_crack_patch(file_name=hw_info, setup_with_arg='HWiNFO64.exe')
                func.clear()
                continue

            elif choice == 10:
                func.install_software(file_name=aomei_partition, setup='Setup.exe', args='/SILENT',
                                      another_task=func.AnOtherTask.AOMEI_PRO)
                func.clear()
                continue

            elif choice == 11:
                func.portable_crack_patch(file_name=rufus, setup_with_arg='Rufus.exe')
                func.clear()
                continue

            elif choice == 12:
                func.install_software(file_name=seven_zip, setup='Setup.exe', args='/S')
                func.clear()
                continue

            elif choice == 13:
                func.install_software(file_name=vs_redistributable, setup='Setup.exe',
                                      args='/INSTALL /QUIET /NORESTART')
                func.clear()
                continue

            elif choice == 14:
                func.install_software(file_name=better_rename, setup='Setup.exe', args='/VERYSILENT /NORESTART')
                time.sleep(1)
                func.portable_crack_patch(file_name=better_rename, setup_with_arg='Serial.txt')
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
