#!/usr/bin/python3
print("content-type: text/html")
print()

import subprocess as sp
import cgi
form =   cgi.FieldStorage()
osname = form.getvalue("x")
osimage = form.getvalue("i")
print(osname)
print("OS Launched named {}".format(osname))
cmd = "sudo docker run -d -i -t --name {0} {1}".format(osname,osimage)
output = sp.getstatusoutput(cmd)
print(output)

#status = output[0]
#out = output[1]
#if status == 0:
#	print("OS Launched named {}".format(osname))
#else:
#	print("some error: {}".format(out))
