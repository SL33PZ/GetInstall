from lib.git import git
import os
import subprocess
import shutil


def OneDriveGui(self):
        
    pathDir="tmp/onedrivegui"
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    git(f"https://aur.archlinux.org/onedrivegui-git {pathDir}")
    os.chdir(pathDir)
    subprocess.run("makepkg -sri --skipchecksums --nocheck --noconfirm", shell=True)
    os.chdir("../..")
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
        
    self.oneDriveGui.setEnabled(True)
    self.oneDriveGui.setChecked(True)
    
    
    
