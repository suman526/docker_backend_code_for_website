#!/usr/bin/python3
import subprocess
print("content-type: text/html")
print()
start = subprocess.getoutput("sudo systemctl start docker")
enable = subprocess.getoutput("sudo systemctl enable docker")
status = subprocess.getoutput("sudo systemctl status docker")
print(status)

