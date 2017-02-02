# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import os
import sys
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

if not os.geteuid() == 0:
    sys.exit('Insanity must be run as root')
os.system('apt-get install sudo')
os.system('sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install wine')
os.system('clear')
print '\n'
print ' ################################################################## '
print '\n'
print '\n'
print '             *{0} SELECT WINDOWS 7 ON winecfg {1}* '.format(GREEN, END)
print '                 [PRESS ENTER TO DO THIS]'
print '\n'
print '\n'
print ' ################################################################## '
raw_input('                            ')
os.system('winecfg')
os.system('clear')
print '\n'
print ' ################################################################## '
print '\n'
print '\n'
print '             *{0} DOWNLOADING PYTHON2.7.msi {1}* '.format(GREEN, END)
print '                          - PLEASE WAIT -'
print '\n'
print '\n'
print ' ################################################################## '
os.system('wget https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi')
os.system('wine msiexec /i python-2.7.13.msi /L*v log.txt')
os.system('clear')
print '\n'
print ' ################################################################## '
print '\n'
print '\n'
print '             *{0} DOWNLOADING WIN32-OY2.7.exe {1}* '.format(GREEN, END)
print '                          - PLEASE WAIT -'
print '\n'
print '\n'
print ' ################################################################## '
os.system('wget https://ufpr.dl.sourceforge.net/project/pywin32/pywin32/Build%20220/pywin32-220.win32-py2.7.exe')
os.system('sudo wine win32-py2.7.exe')
os.system('sudo wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller')
os.system('sudo wine /root/.wine/drive_c/Python27/python.exe -m pip uninstall Crypto')
os.system('sudo wine /root/.wine/drive_c/Python27/python.exe -m pip uninstall pycrypto')
os.system('clear')
print '\n'
print ' ################################################################## '
print '\n'
print '\n'
print '             *{0} DOWNLOADING VCFORPYTHON2.7.msi {1}* '.format(GREEN, END)
print '                          - PLEASE WAIT -'
print '\n'
print '\n'
print ' ################################################################## '
os.system('wget https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi')
one()
os.system('sudo wine msiexec /i VCForPython27.msi /L*v log2.txt')
os.system('sudo wine /root/.wine/drive_c/Python27/python.exe -m pip install pycrypto')
os.system('mkdir .OK')
