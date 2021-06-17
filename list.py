#!/usr/bin/python3
import subprocess
print("content-type: text/html")
print()
image = subprocess.getoutput("sudo docker images")
print(image)
