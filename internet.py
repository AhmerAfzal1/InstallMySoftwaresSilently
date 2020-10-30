from colorama import init, Fore, Style
import constant as const
import functions as func
import main

chrome = "Google Chrome 84.0.4147.89"
firefox = "Firefox 82.0"
idm = "Internet Download Manager 6.37.14"
net_balancer = "NetBalancer 9.12.9"
net_limiter = "NetLimiter 4.0.67"


def main_developer():
    func.set_console_title(const.heading_internet)
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

            choice = int(input("\nPlease enter your choice: "))

            if choice == 0:
                print("\nValue must be greater than zero")
                input()
                func.clear_screen()
                continue

            elif choice == 1:
                func.clear_screen()
                main.main()
                break

            elif choice == 2:
                func.install_software(firefox, "Setup.exe")
                break

            elif choice == 7:
                exit()
                break

            else:
                print("\nThat is not between 1 To 7! Try Again\n")
                input()
                func.clear_screen()
                continue

        except ValueError:
            print("\nPlease input a number")
            input()
            func.clear_screen()


if __name__ == "__main__":
    init()
    main_developer()
