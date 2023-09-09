#!/usr/bin/python3

import boto3
import cgi
import cgitb

cgitb.enable()  # This enables better error reporting in the browser

print("Content-Type: text/html")
print()

def delete_s3_bucket(bucket_name):
    try:
        s3 = boto3.client('s3')
        s3.delete_bucket(Bucket=bucket_name)
        return True
    except Exception as e:
        return f"An error occurred while deleting the S3 bucket: {e}"

form = cgi.FieldStorage()
bucket_name = form.getvalue("bucket_name", "")

if bucket_name:
    result = delete_s3_bucket(bucket_name)
    if result is True:
        print("S3 bucket deleted successfully.")
    else:
        print(result)
else:
    print("Please provide a valid bucket name.")