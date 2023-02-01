from lib.git import git
import os
import subprocess
import shutil


home = os.path.expanduser( '~' )
plasmoidPath=f"{home}/.local/share/plasma/plasmoids"


def SystemMonitor(self):
    print(os.getcwd())
    pathDir="tmp/simpleMonitor"
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    if os.path.exists(f"{plasmoidPath}/org.kde.simpleMonitor") == True:
        shutil.rmtree(f"{plasmoidPath}/org.kde.simpleMonitor", ignore_errors=False, onerror=None)
    git(f"https://github.com/dhabyx/plasma-simpleMonitor {pathDir}")
    os.chdir('tmp/simpleMonitor')
    subprocess.run("plasmapkg2 -t plasmoid -i ./plasmoid", shell=True)
    os.chdir("../..")
    if os.path.exists(pathDir) == True:
            shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    print(os.getcwd())
    self.simpleStupidLauncher.setEnabled(True)
    self.simpleStupidLauncher.setChecked(True)
    
