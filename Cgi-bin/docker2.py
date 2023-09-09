#!/usr/bin/python3
 
import subprocess

print("content-type: text/html")
print()

output=subprocess.getoutput("sudo docker ps")
#print(output.split("\n")[1:])
"""print("<pre>")
for i in output.split("\n")[1:]:
    print(i)
print("</pre>")
"""
print("<pre>")
alldocker=output.split("\n")[1:]
for i in alldocker:
   ik =i.split()[1]
   st =i.split()[6]
   ss=i.split()[-1]
   print("Image name: " + ik +"Docker status:  " + "<span style= ' color : green'>" +  st+ "</span>" + " Container name:  " + ss)
print("</pre>")
print()
print()
#print("<form action= http://15.206.173.164/menu.html>")
#print("<input type='submit' value='Back to Main menu'></form>")