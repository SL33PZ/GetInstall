import os, shutil, subprocess




link = "https://github.com/Schneegans/Burn-My-Windows/releases/latest/download/burn_my_windows_kwin4.tar.gz"
home = os.path.expanduser( '~' )
pkg="burn_my_windows_kwin4.tar.gz"


def burnMyWindows(self):
    pathDir="tmp"
    subprocess.run("rm -rf tmp/*", shell=True)
    if os.path.exists(f"{home}/.local/share/kwin/effects"):
        shutil.rmtree(f"{home}/.local/share/kwin/effects")
    subprocess.run(f"wget {link} -P {pathDir}", shell=True)
    os.chdir(pathDir)
    subprocess.run(f"mkdir -p {home}/.local/share/kwin/effects", shell=True)
    subprocess.run(f"tar -xf {pkg} -C {home}/.local/share/kwin/effects", shell=True)
    os.chdir("..")
    subprocess.run("rm -rf tmp/*", shell=True)

    self.burnMyWindows.setEnabled(True)
    self.burnMyWindows.setChecked(True)
    
