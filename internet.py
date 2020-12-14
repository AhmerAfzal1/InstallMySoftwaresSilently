import sys

from colorama import init

import constant as const
import functions as func
import main

chrome = 'Google Chrome 87.0.4280.88'
firefox = 'Firefox 83.0'
idm = 'Internet Download Manager 6.38 Build 15'
net_balancer = 'NetBalancer 9.12.9'
net_limiter = 'NetLimiter 4.0.67'


def main_program():
    func.set_console_title(const.heading_internet)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_internet)
            func.back_heading()
            func.sub_heading_softwares('02', firefox)
            func.sub_heading_softwares('03', idm)
            func.sub_heading_softwares('04', chrome)
            func.sub_heading_softwares('05', net_balancer)
            func.sub_heading_softwares('06', net_limiter)
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
                func.install_software(file_name=firefox, setup='Setup.exe', args='-ms')
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=idm, setup='Setup.exe', args='/skipdlgs', wait=10,
                                      another_task=func.AnOtherTask.IDM)
                func.clear()
                continue

            elif choice == 4:
                func.install_software(file_name=chrome, setup='Setup.exe', args='/S')
                func.clear()
                continue

            elif choice == 5:
                func.install_software(file_name=net_balancer, setup='Setup.exe', args='/SILENT /VERYSILENT /NORESTART')
                func.clear()
                continue

            elif choice == 6:
                func.install_software(file_name=net_limiter, setup='Setup.exe', args='/EXENOUI /EXENOUPDATES')
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
