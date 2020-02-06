#!/usr/bin/env python3

import json
import boto3
import colorama
from colorama import Fore, Style

profile='default'
region='us-east-1'

##         print("\n", Fore.GREEN, i, Style.RESET_ALL)

#create boto session and client
session = boto3.Session(profile_name = profile)
s3_client = session.client('s3', region_name=region)



buckets=s3_client.list_buckets()['Buckets']

print(s3_client.get_bucket_logging(Bucket='elecotest')['LoggingEnabled'])

for bucket in buckets:
    try:
        if s3_client.get_bucket_logging(Bucket=bucket['Name'])['LoggingEnabled']['TargetBucket'] == bucket['Name']:
            print(Fore.RED, bucket['Name'], "logs to itself.\n", Style.RESET_ALL)
        else:
            print(Fore.ORANGE, bucket['Name'], "logs to {}.\n".format(bucket['Name']['LoggingEnabled']['TargetBucket']), Style.RESET_ALL)
    except:
        print(Fore.GREEN, "{} does not have server logging enabled.\n".format(bucket['Name']), Style.RESET_ALL)
