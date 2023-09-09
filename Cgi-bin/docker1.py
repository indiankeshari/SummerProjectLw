#!/usr/bin/python3

import cgi
import subprocess
print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data1=form.getvalue("d")
output1=subprocess.getoutput("sudo docker run -dit {}".format(data1))        
output=subprocess.getoutput("sudo docker ps")

print(output1)
print("<pre>")
alldocker=output.split("\n")[1]
ik =alldocker.split()[1]
st =alldocker.split()[6]
ss=alldocker.split()[-1]
print("Image name: " + ik +"Docker status:  " + "<span style= ' color : green'>" +  st+ "</span>" + " Container name:  " + ss)
print("</pre>")