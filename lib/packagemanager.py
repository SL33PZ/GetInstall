from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import subprocess, os, shutil
from lib.git import git


def packageManager(self):
    
        pathDir="tmp/yay"
        if os.path.exists(pathDir) == True:
            shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
        git(f"https://aur.archlinux.org/yay {pathDir}")
        os.chdir(pathDir)
        subprocess.run("makepkg -sri --skipchecksums --nocheck --noconfirm", shell=True)
        os.chdir("../..")
        if os.path.exists(pathDir) == True:
            shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
        
        self.yay.setEnabled(True)
        self.yay.setChecked(True)