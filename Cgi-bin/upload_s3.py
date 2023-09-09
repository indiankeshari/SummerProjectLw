#!/usr/bin/env python3
import cgi
import boto3
import os

def upload_file_to_s3(bucket_name, file_field):
    s3_client = boto3.client('s3')
    
    file_item = file_field.filename
    object_name = os.path.basename(file_item)
    
    try:
        s3_client.upload_fileobj(file_field.file, bucket_name, object_name)
        return f"{object_name} uploaded successfully to {bucket_name}"
    except Exception as e:
        return f"Error uploading {object_name} to {bucket_name}: {e}"

if __name__ == "__main__":
    form = cgi.FieldStorage()
    
    bucket_name = "hacker123"  # Replace with your AWS S3 bucket name
    
    if "file" in form and form["file"].filename:
        file_field = form["file"]
        response = upload_file_to_s3(bucket_name, file_field)
        print("Content-type: text/html\n")
        print("<html>")
        print("<head>")
        print("<title>File Upload to S3</title>")
        print("</head>")
        print("<body>")
        print("<h1>File Upload to S3</h1>")
        print("<p>" + response + "</p>")
        print("</body>")
        print("</html>")
    else:
        print("Content-type: text/html\n")
        print("<html>")
        print("<head>")
        print("<title>File Upload to S3</title>")
        print("</head>")
        print("<body>")
        print("<h1>File Upload to S3</h1>")
        print("<p>No file selected for upload.</p>")
        print("</body>")
        print("</html>")