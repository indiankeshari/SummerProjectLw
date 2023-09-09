#!/usr/bin/env python3
import cgi
import boto3

def create_s3_bucket(bucket_name):
    s3_client = boto3.client('s3')
    response = s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'  # Change this to your desired region
        }
    )
    return response

def main():
    print("Content-Type: text/html\n")  # CGI header

    form = cgi.FieldStorage()  # Parse the form data

    bucket_name = form.getvalue("bucket_name")

    if bucket_name:
        response = create_s3_bucket(bucket_name)
        
        if 'Location' in response:
            print(f"S3 Bucket '{bucket_name}' created successfully in {response['Location']}.")
        else:
            print("Error creating S3 bucket.")
    else:
        print("Please provide a bucket name.")

if __name__ == "__main__":
    main()