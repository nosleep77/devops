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

  local_filename = "/root/mount_file/week13-fjamsh.csv"

  AWS_ACCESS = os.getenv('AWS_ACCESS').strip("\n")
  AWS_SECRET = os.getenv('AWS_SECRET').strip("\n")
  print(f"AWS_ACCESS is {AWS_ACCESS}")
  print(f"AWS_SECRET is {AWS_SECRET}")

  s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS, aws_secret_access_key=AWS_SECRET)
  s3_file = "/root/mount_file/week13-fjamsh.csv"
  s3.upload_file(s3_file, 'UML', 'week13-fjamsh.csv')

