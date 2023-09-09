#!/usr/bin/env python3
import cgi
from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = "ACe6c49c493f5073dbbe541e0c9e8434f4"
auth_token = "1e3112775e089e67c471a522a0091c35"

def send_twilio_message(body, from_number, to_number):
    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            body=body,
            from_=from_number,
            to=to_number
        )
        return f"Message SID: {message.sid}\nMessage sent successfully"
    except Exception as e:
        return f"Error sending message: {e}"

if __name__ == "__main__":
    form = cgi.FieldStorage()
    
    body = form.getvalue("body", "")
    from_number = "+12294045388" 
    to_number = form.getvalue("to_number", "")
    
    response = send_twilio_message(body, from_number, to_number)
    
    print("Content-type: text/html\n")
    print("<html>")
    print("<head>")
    print("<title>Twilio Message</title>")
    print("</head>")
    print("<body>")
    print("<h1>Twilio Message</h1>")
    print("<pre>")
    print(response)
    print("</pre>")
    print("</body>")
    print("</html>")