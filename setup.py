import sys
from distutils.core import setup

import constant as conts

try:
    # This will create an exe that needs Microsoft Visual C++ 2008
    # Redistributable Package
    import py2exe
except ImportError:
    if len(sys.argv) >= 2 and sys.argv[1] == 'py2exe':
        print('Cannot import py2exe', file=sys.stderr)
        exit(1)

# python setup.py install
# python setup.py py2exe

sys.argv.append('py2exe')

py2exe_console = [{
    'comments': conts.heading_main_title,
    'copyright': conts.copyright_,
    'description': conts.desription,
    'dest_base': conts.product,
    'icon_resources': [(0, 'setup.ico')],
    'product_name': conts.product,
    'product_version': conts.version,
    'script': '__main__.py',
    'uac_info': 'requireAdministrator',
    'version': conts.version,
}]

py2exe_options = {
    'bundle_files': 3,
    'compressed': True,
    'dist_dir': 'dist',
    'dll_excludes': [],
    'excludes': ['tkinter'],
    'includes': ['dbm.dumb'],
    'optimize': 2,
    'unbuffered': True,
    'xref': True,
}

setup(
    author_email=conts.email,
    author=conts.author,
    console=py2exe_console,
    description=conts.desription,
    license='Unlicense',
    long_description=conts.heading_main_title,
    maintainer_email=conts.email,
    maintainer=conts.author,
    name=conts.product,
    options={'py2exe': py2exe_options},  # Optionally 'py2exe' can replaced to 'build_exe'
    platforms='Windows',
    data_files=[('', ['InstallMySofts.bak', 'InstallMySofts.dat', 'InstallMySofts.dir'])],
    version=conts.version,
    zipfile=None,

    classifiers=[
        'Topic :: Desktop Environment :: File Managers',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
