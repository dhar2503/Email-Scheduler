import subprocess, sys
p = subprocess.Popen(["powershell.exe","./scripts/powershell.ps1"], stdout=sys.stdout)
p.communicate()

