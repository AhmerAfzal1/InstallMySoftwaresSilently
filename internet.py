import sys

from colorama import init

import constant as const
import functions as func
import main


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
            func.sub_heading_softwares('05', const.net_balancer)
            func.sub_heading_softwares('06', const.net_limiter)
            func.eixt_heading('07')

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
                func.InstallSoftware(file_name=const.firefox, setup='Setup.exe', args=r'-ms')
                func.clear()
                continue

            elif choice == 3:
                func.InstallSoftware(file_name=const.idm, setup='Setup.exe', args=r'/skipdlgs', wait=10,
                                     another_task=func.AnOtherTask.IDM)
                func.clear()
                continue

            elif choice == 4:
                func.InstallSoftware(file_name=const.chrome, setup='Setup.exe', args=r'/S')
                func.clear()
                continue

            elif choice == 5:
                func.InstallSoftware(file_name=const.net_balancer, setup='Setup.exe',
                                     args=r'/SILENT /VERYSILENT /NORESTART')
                func.clear()
                continue

            elif choice == 6:
                func.InstallSoftware(file_name=const.net_limiter, setup='Setup.exe', args=r'/EXENOUI /EXENOUPDATES')
                func.clear()
                continue

            elif choice == 7:
                func.remove_temp(is_wait=True)
                sys.exit()

            else:
                func.exception_range_heading(1, 7)
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f'Please input a number')
            func.exception_heading(f'Error: {err}')
            input()
            func.clear()
