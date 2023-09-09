#!/usr/bin/env python3
import cgi
import boto3

print("Content-type: text/html")
print()

# Get the form data
form = cgi.FieldStorage()

# Specify your AWS region here
aws_region = 'ap-south-1'

# Create an EC2 client with the specified region
ec2_client = boto3.client('ec2', region_name=aws_region)

# Get the values of the form fields
image_id = form.getvalue('image_id')
instance_type = form.getvalue('instance_type')
max_count = int(form.getvalue('max_count', 1))
min_count = int(form.getvalue('min_count', 1))

# Launch EC2 instances
response = ec2_client.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    MaxCount=max_count,
    MinCount=min_count
)

# Print the response

print("<h1>EC2 Instances Launched Successfully!</h1>")
print("<p>ImageId: {}</p>".format(image_id))
print("<p>InstanceType: {}</p>".format(instance_type))
print("<p>MaxCount: {}</p>".format(max_count))
print("<p>MinCount: {}</p>".format(min_count))
print("<p>Instance IDs:</p>")
print("<ul>")
for instance in response['Instances']:
    print("<li>{}</li>".format(instance['InstanceId']))
print("</ul>")