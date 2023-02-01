from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import subprocess


def develPackages(self):
    cmd = "sudo pacman-mirrors -c Germany -m rank"
    subprocess.run(cmd, shell=True)
    
    self.baseDevel.setEnabled(True)
    self.baseDevel.setChecked(True)

