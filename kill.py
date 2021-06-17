#!/usr/bin/python3
print("content-type: text/html")
print()

import subprocess as sp
import cgi
form =   cgi.FieldStorage()
osname = form.getvalue("x")
cmd = "sudo docker kill {}".format(osname)
output1 = sp.getstatusoutput(cmd)
status1 = output1[0]
out1 = output1[1]
if status1 == 0:
        print("OS name {} has been deleted........You can verify it by seeing docker ps command".format(osname))
else:
        print("Error occured during deletion is {}".format(out1))


