sudo dpkg --add-architecture i386 && sudo apt-get update && apt-get install wine32
sudo apt-get install wget -y
sudo winecfg
sudo wine msiexec /i python-2.7.12.msi /L*v log.txt
sudo wine pywin32-220.win32-py2.7.exe
sudo wine pyHook-1.5.1.win32-py2.7.exe
sudo wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller
wget https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi
sudo wine msiexec /i VCForPython27.msi /L*v log2.txt
sudo wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pip.exe install pyinstaller
sudo wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pip.exe uninstall Crypto
sudo wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pip.exe install pycrypto



