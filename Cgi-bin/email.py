#!/usr/bin/python3
import cgi
import smtplib
from email.mime.text import MIMEText

# Get form data
form = cgi.FieldStorage()

# Email configuration
sender = "rit566912@gmail.com"  # Update with your actual email
password = "czxljzpiwwhrvzbv"  # Update with your actual password
subject = "Testing of e-mailing through Python"

def send_email(receiver, message):
    try:
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())

        return True

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print("Content-type: text/html\n")
    print("<html>")
    print("<head>")
    print("<title>Email Sending</title>")
    print("</head>")
    print("<body>")
    
    if "receiver" in form and "message" in form:
        receiver = form["receiver"].value
        message = form["message"].value
        result = send_email(receiver, message)
        
        if result is True:
            print("<p>Email sent successfully!</p>")
        else:
            print(f"<p>Error sending email: {result}</p>")
    else:
        print("<p>Missing form data.</p>")
    
    print("</body>")
    print("</html>")