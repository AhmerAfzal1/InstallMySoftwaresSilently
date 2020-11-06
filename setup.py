from distutils.core import setup
from distutils.sysconfig import get_python_lib
import constant as conts
import os
import sys

try:
    # This will create an exe that needs Microsoft Visual C++ 2008
    # Redistributable Package
    import py2exe
except ImportError:
    if len(sys.argv) >= 2 and sys.argv[1] == 'py2exe':
        print('Cannot import py2exe', file=sys.stderr)
        exit(1)

mfc_dir = get_python_lib() + '\\pythonwin\\'
mfc_files = [os.path.join(mfc_dir, i) for i in
             ["mfc90.dll", "mfc90u.dll", "mfcm90.dll", "mfcm90u.dll", "Microsoft.VC90.MFC.manifest"]]
data_files = [("Microsoft.VC90.MFC", mfc_files), ]

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")


class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = conts.my_version
        self.company_name = conts.my_company
        self.copyright = conts.my_copyright
        self.name = conts.my_product


py2exe_options = {
    'bundle_files': 1,
    'compressed': 1,
    'optimize': 2,
    'dist_dir': '.',
    'dll_excludes': ['w9xpopen.exe', 'crypt32.dll'],
}

target = Target(
    description=conts.heading_main_title,
    script="main.py",
    dest_base=conts.my_product)

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    zipfile=None,
    console=[target],
    data_files=data_files
)
