from colorama import init
import constant as const
import functions as func
import main
import sys

i_tunes = "iTunes 12.9.5.7"
samsung_usb = "Samsung USB Drivers 1.7.35.0"
smart_switch = "Smart Switch 4.2.20072.4"


def main_program():
    func.set_console_title(const.heading_mobile)
    init()
    while True:
        try:
            func.main_heading()
            func.sub_heading(const.heading_mobile)
            func.back_heading()
            func.sub_heading_softwares("02", samsung_usb)
            func.sub_heading_softwares("03", smart_switch)
            func.sub_heading_softwares("04", i_tunes)
            func.eixt_heading("05")

            choice = func.input_heading()

            if choice == 0:
                func.exception_heading("Value must be greater than zero")
                input()
                func.clear()
                continue

            elif choice == 1:
                func.clear()
                main.main()
                break

            elif choice == 2:
                func.install_software(file_name=samsung_usb, setup_with_arg="Setup.exe /S")
                func.clear()
                continue

            elif choice == 3:
                func.install_software(file_name=smart_switch, setup_with_arg="Setup.exe /S")
                func.clear()
                continue

            elif choice == 4:
                func.install_software(file_name=i_tunes, setup_with_arg="Setup.exe /qn /norestart")
                func.clear()
                continue

            elif choice == 5:
                func.remove_temp()
                sys.exit()

            else:
                func.exception_range_heading("1", "5")
                input()
                func.clear()
                continue

        except Exception as err:
            func.exception_heading(f"Please input a number")
            func.exception_heading(f"Error: {err}")
            input()
            func.clear()
