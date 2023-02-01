import subprocess, os, shutil
from lib.git import git


home = os.path.expanduser( '~' )
plasmoidPath=f"{home}/.local/share/plasma/plasmoids"


def simpleLauncher(self):
    
    pathDir="tmp/simpleLauncher"
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    if os.path.exists(f"{plasmoidPath}/stupidsimplelauncher") == True:
        shutil.rmtree(f"{plasmoidPath}/stupidsimplelauncher", ignore_errors=False, onerror=None)
    git(f"https://www.github.com/heqro/stupid-simple-launcher {pathDir}")
    os.chdir('tmp')
    subprocess.run("kpackagetool5 -t Plasma/Applet --install simpleLauncher/v1", shell=True)
    os.chdir("..")
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    self.simpleStupidLauncher.setEnabled(True)
    self.simpleStupidLauncher.setChecked(True)


