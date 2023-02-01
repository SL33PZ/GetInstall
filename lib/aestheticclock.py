import subprocess, os, shutil
from lib.git import git



home = os.path.expanduser( '~' )
plasmoidPath=f"{home}/.local/share/plasma/plasmoids"

def aestclockProcess(self):
    
    pathDir="tmp/aestheticClock"
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)
    if os.path.exists(f"{plasmoidPath}/com.github.prayag2.aestheticclock") == True:
        shutil.rmtree(f"{plasmoidPath}/com.github.prayag2.aestheticclock", ignore_errors=False, onerror=None)
    git(f"https://github.com/prayag2/kde_aestheticclock {pathDir}")
    os.chdir(pathDir)
    subprocess.run("kpackagetool5 -i package", shell=True)
    os.chdir("../..")
    if os.path.exists(pathDir) == True:
        shutil.rmtree(pathDir, ignore_errors=False, onerror=None)

    self.aestheticClock.setEnabled(True)
    self.aestheticClock.setChecked(True)
