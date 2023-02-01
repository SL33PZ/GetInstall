import os, shutil, subprocess




link = "https://github.com/Figma-Linux/figma-linux/releases/download/v0.10.0/figma-linux_0.10.0_linux_x64.pacman"
pkg="figma-linux_0.10.0_linux_x64.pacman"


def figma_linux(self):
    pathDir="tmp"
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    subprocess.run(f"wget {link} -P {pathDir}", shell=True)
    os.chdir(pathDir)
    subprocess.run(f"sudo pacman -U --needed --noconfirm {pkg}", shell=True)
    os.chdir("..")
    if os.path.exists(f"{pathDir}/{pkg}") == True:
        os.remove(f"{pathDir}/{pkg}")
        
    self.figmaLinux.setEnabled(True)
    self.figmaLinux.setChecked(True)