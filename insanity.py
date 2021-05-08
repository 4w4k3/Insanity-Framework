#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import os
import sys
import time
import datetime
from bin.settings import exec_com
from bin.settings import RED, WHITE, END

if not os.geteuid() == 0:
    sys.exit('Insanity must be run as root')

# create def clear():
def clear():
    os.system('clear')

# create def heading():
def heading():
    os.system('clear')

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
 -- [I]ɴsᴀɴɪᴛʏ [F]ʀᴀᴍᴇᴡᴏʀᴋ  --                            Version: 1.0 Stable               
''' + END)

# create def optionBanner():
def optionBanner():
    print '! {0}[{1}1{0}]{1} Gᴇɴᴇʀᴀᴛᴇ FUD - {0}[{1}2{0}]{1} Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ !              {0}[{1}U{0}]{1} ᴜᴘᴅᴀᴛᴇ  {0}[{1}Q{0}]{1} ǫᴜɪᴛ'.format(RED, WHITE)

# create def pp():
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

# create def asker():
def asker():
    header = ('{0}InSaNiTy{1} > {2}'.format(RED, WHITE, END))
    choice = raw_input(header)
      
    if choice.upper() == 'Q' or choice.upper() == 'QUIT':
	clear()
	pp()
        raise SystemExit
    elif choice.upper() == 'E' or choice.upper() == 'EXIT':
	clear()
	pp()
        raise SystemExit
    elif choice == '1':
        exec_com('dammed.py', sudo=True)
        raise SystemExit
    elif choice == '2':
        exec_com('striker.py', sudo=True)
        raise SystemExit
    elif choice.upper() == 'U':
        exec_com('updater.py', sudo=True)
        asker()
    elif choice.upper() == 'IFCONFIG':
	os.system(str(choice)) 
        asker()
    elif choice.upper() == 'LS':
	os.system(str(choice))
        asker() 
    elif choice.upper() == 'BACK':
        main()
    elif choice.upper() == 'UPDATE':
        exec_com('updater.py', sudo=True)
        asker()
    else:             
	clear()            
	print 'Invalid Option'
        time.sleep(2)
	heading()
        optionBanner()
        asker()

 # create def disclaimer():
def disclaimer():
     clear()
     sys.stdout.write(WHITE + '''
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u''' + RED + '''  # Dɪsᴄʟᴀɪᴍᴇʀ Aʟᴇʀᴛ #''' + END + '''
       u$$$$$$"   "$$$"   "$$$$$$u                      
       "$$$$"      u$u       $$$$"  Iɴsᴀɴɪᴛʏ Fʀᴀᴍᴇᴡᴏʀᴋ
        $$$u       u$u       u$$$  Nᴏᴛ ʀᴇsᴘᴏɴsɪʙʟᴇ ꜰᴏʀ ᴍɪsᴜsᴇ 
        $$$u      u$$$u      u$$$                  ᴀɴᴅ ꜰᴏʀ ɪʟʟᴇɢᴀʟ ᴘᴜʀᴘᴏsᴇs.
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"    Usᴇ ɪᴛ ᴊᴜsᴛ ꜰᴏʀ''' + RED + ''' ᴡᴏʀᴋ''' + WHITE + ''' ᴏʀ ''' + RED + '''ᴇᴅᴜᴄᴀᴛɪᴏɴᴀʟ''' + WHITE + ''' !!!
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$        * { Tᴏ ᴍᴀɪɴᴛᴀɪɴ ᴇꜰꜰɪᴄɪᴇɴᴄʏ } *
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$         ᴅᴏɴ'ᴛ ᴜᴘʟᴏᴀᴅ ᴛᴏ VIRUS TOTAL 
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$            ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ sᴄᴀɴ,
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"       ᴜᴘʟᴏᴀᴅ ᴛᴏ NODISTRIBUTE.COM     
 """      ""$$$$$$$$$$$uu ""$"""               
           uuuu ""$$$$$$$$$$uuu 
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$         Pʀᴇss [ᴇɴᴛᴇʀ] ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ
  $$$$$$$$$$""""           ""$$$$$$$$$$$" 
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
''')
    
# create def main():
def main():
    clear()
  
    disclaimer()
    raw_input('')  
    
    clear()

    heading()

    try:

        while True:

            optionBanner()

            header = ('{0}InSaNiTy{1} > {2}'.format(RED, WHITE, END))
            choice = raw_input(header)
            
            if choice.upper() == 'Q' or choice.upper() == 'QUIT':
		clear()
		pp()
                raise SystemExit
	    elif choice.upper() == 'E' or choice.upper() == 'EXIT':
		clear()
		pp()
                raise SystemExit
            elif choice == '1':
                exec_com('dammed.py', sudo=True)
                sys.exit(0)
            elif choice == '2':
                exec_com('striker.py', sudo=True)
                raise SystemExit
            elif choice.upper == 'UPDATE':
                exec_com('updater.py', sudo=True)
                asker()
	    elif choice.upper() == 'U':
                exec_com('updater.py', sudo=True)
                asker()
            elif choice == 'ifconfig':
		os.system(str(choice)) 
                asker()
            elif choice == 'ls':
		os.system(str(choice))
                asker() 
            elif choice == 'back':
		main()
            else:             
		clear()            
		print 'Invalid Option'
                time.sleep(2)
		heading()
                optionBanner()
                asker()
 

    except KeyboardInterrupt:
	clear()
	pp()
        sys.exit(0)


if __name__ == '__main__':
    main()
