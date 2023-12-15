import boto3
import json

"""Launching an EC2 instance into our web-app-B Subnet
"""

# VPC and subnet IDs
vpc_id = 'vpc-05704411be30ec044'
subnet_id = 'subnet-0a32b064754eaf45a'

# Security group
SG = ['Hwtechnet-SG']
# AMI ID (Amazon Machine Image)
ami_id = 'ami-0759f51a90924c166'

# instance type and key pair name
instance_type = 't2.micro'
key_name = 'hwtechnet'
# Create an EC2 client
ec2_client = boto3.client('ec2')

# Create an EC2 instance
response = ec2_client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName= key_name,
    MinCount = 1,
    MaxCount = 1,
    SubnetId = subnet_id
)

print(response)

