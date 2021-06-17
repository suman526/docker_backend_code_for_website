#!/usr/bin/python3
print("content-type: text/html")
print()

import subprocess as sp
import cgi
form =   cgi.FieldStorage()
osimage = form.getvalue("x")
cmd = "sudo docker image inspect {}".format(osimage)
output = sp.getstatusoutput(cmd)
print(output)

