from lib.git import git
import os
import subprocess
import shutil



def OneDrive(self):
        
    pathDir="tmp/onedrive"
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    git(f"https://aur.archlinux.org/onedrive-abraunegg {pathDir}")
    os.chdir(pathDir)
    subprocess.run("makepkg -sri --skipchecksums --nocheck --noconfirm", shell=True)
    os.chdir("../..")
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
        
    self.oneDrive.setEnabled(True)
    self.oneDrive.setChecked(True)
    
    
    
