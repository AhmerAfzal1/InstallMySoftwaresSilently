import sys
from distutils.core import setup

import constant as conts

try:
    # This will create an exe that needs Microsoft Visual C++ 2008
    # Redistributable Package
    import py2exe
except ImportError:
    if len(sys.argv) >= 2 and sys.argv[1] == "py2exe":
        print("Cannot import py2exe", file=sys.stderr)
        exit(1)

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

py2exe_console = [{
    "comments": conts.heading_main_title,
    "copyright": conts.__copyright__,
    "description": conts.__desription__,
    "dest_base": conts.__product__,
    "icon_resources": [(0, "setup.ico")],
    "product_name": conts.__product__,
    "product_version": conts.__version__,
    "script": "main.py",
    "version": conts.__version__,
}]

py2exe_options = {
    "bundle_files": 3,
    "compressed": True,
    "dist_dir": "dist",
    "dll_excludes": [],
    "excludes": ["tkinter"],
    "optimize": 2,
}

setup(
    options={"py2exe": py2exe_options},
    zipfile=None,
    console=py2exe_console,
    name=conts.__product__,
    version=conts.__version__,
    description=conts.__desription__,
    long_description=conts.heading_main_title,
    author=conts.__author__,
    author_email=conts.__email__,
    maintainer=conts.__author__,
    maintainer_email=conts.__email__,
    license="Unlicense",

    classifiers=[
        "Topic :: Desktop Environment :: File Managers",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: Public Domain",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
