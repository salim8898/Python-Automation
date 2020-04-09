import json
import boto3
client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
response = client.describe_instances()

def lambda_handler(event, context):
   id = ''
   server = []
   for reservation in response["Reservations"]:
       for instance in reservation["Instances"]:
           for tag in instance["Tags"]:
               if "poc" in tag["Value"]:
                   id += instance["InstanceId"] + ' '
                   server = id.split()
                   #ec2.instances.filter(InstanceIds=server).stop()
                   print('remove above comment to stop your machine')