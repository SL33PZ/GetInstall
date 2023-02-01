import subprocess



def git(link="", outputName=""):
    subprocess.run(f"git clone {link} {outputName}", shell=True)
    
