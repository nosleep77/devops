import os
import json
import pymysql
import csv
import csv
import boto3
import configparser

print("Contents of '/root/mount_file/':")
for file in os.listdir('/root/mount_file/'):
    print(file)

def my_function():
  for key, value in os.environ.items():
    print(f"{key}: {value}")

  #aws_conn = os.environ.get("AIRFLOW_CONN_AWS")
  #print(aws_conn)
  #json_dict = json.loads(aws_conn)
  #aws_access = json_dict['AWS_ACCESS']
  #aws_secret = json_dict['AWS_SECRET']
  local_filename = "/root/mount_file/week13-fjamsh.csv"

  AWS_ACCESS = os.getenv('AWS_ACCESS').strip("\n")
  AWS_SECRET = os.getenv('AWS_SECRET').strip("\n")
  print(f"AWS_ACCESS is {AWS_ACCESS}")
  print(f"AWS_SECRET is {AWS_SECRET}")

  #s3 = boto3.client('s3', aws_access_key_id=aws_access, aws_secret_access_key=aws_secret)
  #s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS, aws_secret_access_key=AWS_SECRET)
  s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_ACCESS, aws_secret_access_key=AWS_SECRET)

  s3_file = local_filename
  #s3.upload_file(local_filename, 'UML', s3_file)


  print("uploading file to s3")
  try:
    #s3.upload_file(local_filename, 'UML', s3_file)
    s3.upload_fileobj(local_filename, 'UML', s3_file)
  except Exception as e:
    print(f"Error uploading file to S3: {e}")

