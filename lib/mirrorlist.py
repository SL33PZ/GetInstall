from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import subprocess




def mirrorList(self):
    cmd = "sudo pacman-mirrors -c Germany -m rank"
    subprocess.run(cmd, shell=True)
    
    self.mirrorlist.setEnabled(True)
    self.mirrorlist.setChecked(True)
        
        

       
