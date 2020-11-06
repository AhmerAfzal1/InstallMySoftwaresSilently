from colorama import init
import constant as const
import functions as func
import main

chrome = "Google Chrome 84.0.4147.89"
firefox = "Firefox 82.0"
idm = "Internet Download Manager 6.37.14"
net_balancer = "NetBalancer 9.12.9"
net_limiter = "NetLimiter 4.0.67"


def main_program():
    func.set_console_title(const.heading_internet)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_internet)
            func.back_heading()
            func.sub_heading_softwares("02", firefox)
            func.sub_heading_softwares("03", idm)
            func.sub_heading_softwares("04", chrome)
            func.sub_heading_softwares("05", net_balancer)
            func.sub_heading_softwares("06", net_limiter)
            func.eixt_heading("07")

            choice = func.input_heading()

            if choice == 0:
                func.exception_heading("Value must be greater than zero")
                input()
                func.clear_screen()
                continue

            elif choice == 1:
                func.clear_screen()
                main.main()
                break

            elif choice == 2:
                func.install_software(firefox, "Setup.exe -ms")
                break

            elif choice == 3:
                func.install_software(idm, "Setup.exe /S /EN")
                break

            elif choice == 4:
                func.install_software(chrome, "Setup.exe /S")
                break

            elif choice == 5:
                func.install_software(net_balancer, "Setup.exe /SILENT /VERYSILENT /NORESTART")
                break

            elif choice == 6:
                func.install_software(net_limiter, "Setup.exe /EXENOUI /EXENOUPDATES")
                break

            elif choice == 7:
                exit()
                break

            else:
                func.exception_range_heading("1", "7")
                input()
                func.clear_screen()
                continue

        except ValueError:
            func.exception_heading("Please input a number")
            input()
            func.clear_screen()
