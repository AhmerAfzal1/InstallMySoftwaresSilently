import os

import functions as func
from main import main

if __name__ == '__main__':
    if not len(os.listdir(func.temp)) == 0:
        func.log_show('Please wait...')
        func.remove_temp(is_wait=False)
        func.clear()
    main()
