import os, shutil, subprocess
from lib.git import git



link_icons = "https://github.com/sl33pz/PurpleBitch-Icons"
link_plasma = "https://github.com/sl33pz/PurpleBitch-Plasma"
link_sddm = "https://github.com/sl33pz/PurpleBitch-SDDM"

home = os.path.expanduser( '~' )

icons_path = f"{home}/.local/share/icons"
plasma_path = f"{home}/.local/share/plasma/desktoptheme"
sddm_path = f"{home}/.local/share/sddm/themes"


def purpleBitches(self):

    if os.path.exists(f"{icons_path}/PurpleBitch-Icons"):
        shutil.rmtree(f"{icons_path}/PurpleBitch-Icons")
    if os.path.exists(icons_path) == False:
        os.mkdir(icons_path)
    git(f"{link_icons} {icons_path}/PurpleBitch-Icons")
    
    if os.path.exists(f"{plasma_path}/PurpleBitch-Plasma"):
        shutil.rmtree(f"{plasma_path}/PurpleBitch-Plasma")
    if os.path.exists(icons_path) == False:
        os.mkdir(plasma_path)
    git(f"{link_plasma} {plasma_path}/PurpleBitch-Plasma")
    
    if os.path.exists(f"{sddm_path}/PurpleBitch-SDDM"):
        shutil.rmtree(f"{sddm_path}/PurpleBitch-SDDM")
    if os.path.exists(sddm_path) == False:
        os.mkdir(sddm_path)
    git(f"{link_sddm} {sddm_path}/PurpleBitch-SDDM")
    

    self.purpleBitchIcons.setEnabled(True)
    self.purpleBitchIcons.setChecked(True)
    self.purpleBitchPlasma.setEnabled(True)
    self.purpleBitchPlasma.setChecked(True)
    self.purpleBitchSddm.setEnabled(True)
    self.purpleBitchSddm.setChecked(True)
