#!/usr/bin/python3
import subprocess
print("content-type: text/html")
print()
status = subprocess.getoutput("sudo docker ps")
print(status)
