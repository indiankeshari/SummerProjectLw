#!/usr/bin/python3

import cgi
import os
import pywhatkit as kit

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
recipient_number = form.getvalue("recipient_number")
message = form.getvalue("message")

try:
    kit.sendwhatmsg_instantly(recipient_number, message)
    print("<h2>Message sent successfully</h2>")
except Exception as e:
    print("<h2>Error:</h2>")