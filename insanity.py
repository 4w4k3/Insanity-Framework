#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import os
import sys
import time

if not os.geteuid() == 0:
    sys.exit('Insanity must be run as root')
    
def clear():
    os.system('clear')

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

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
 -- [I]ɴsᴀɴɪᴛʏ [F]ʀᴀᴍᴇᴡᴏʀᴋ  --                            Version: 0.1 beta               
''' + END)

def optionBanner():
    print '! {0}[{1}1{0}]{1} Gᴇɴᴇʀᴀᴛᴇ FUD - {0}[{1}2{0}]{1} Sᴛᴀʀᴛ Lɪsᴛᴇɴᴇʀ !              {0}[{1}U{0}]{1} ᴜᴘᴅᴀᴛᴇ  {0}[{1}Q{0}]{1} ǫᴜɪᴛ'.format(RED, WHITE)


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
      
    if choice.upper() == 'Q' or choice.upper() == 'QUIT':
	clear()
	pp()
        raise SystemExit
    elif choice.upper() == 'E' or choice.upper() == 'EXIT':
	clear()
	pp()
        raise SystemExit
    elif choice == '1':
        os.system('python2.7 dammed.py')
        raise SystemExit
    elif choice == '2':
        os.system('python2.7 striker.py')
        raise SystemExit
    elif choice.upper() == 'U':
        os.system('python2.7 updater.py')
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
        os.system('python2.7 updater.py')
        asker()
    else:             
	clear()            
	print 'Invalid Option'
        time.sleep(2)
	heading()
        optionBanner()
        asker()
 
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
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$     
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""               Pʀᴇss [ᴇɴᴛᴇʀ] ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ
           uuuu ""$$$$$$$$$$uuu 
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$" 
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
''')
    

def main():
    clear()
    path = '.OK'

    if os.path.isdir(path):
        pass
    else:
        os.system('sudo python2.7 checker.py')

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
                os.system('python2.7 dammed.py')
                sys.exit(0)
            elif choice == '2':
                os.system('python2.7 striker.py')
                raise SystemExit
            elif choice.upper == 'UPDATE':
                os.system('python2.7 updater.py')
                asker()
	    elif choice.upper() == 'U':
                os.system('python2.7 updater.py')
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

