# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import os
import sys
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

os.system('apt-get install sudo')
os.system('sudo apt-get install wine')
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
os.system('wine msiexec /i python-2.7.13.msi /L*v log.txt')
os.system('wine pywin32.exe')
os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller')
os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install crypto')
os.system('mkdir .OK')

