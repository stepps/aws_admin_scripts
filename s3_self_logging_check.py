#!/usr/bin/env python3

import boto3
import colorama
from colorama import Fore, Style

profile='default'
region='us-east-1'
less_verbose=True

# create boto session and client
session = boto3.Session(profile_name = profile)
s3_client = session.client('s3', region_name=region)

# get a list of all buckets in the account
buckets=s3_client.list_buckets()['Buckets']

# check is server logging is enabled and if it the target bucket is the same as the source bucket
for bucket in buckets:
    try:
        logging_bucket=s3_client.get_bucket_logging(Bucket=bucket['Name'])['LoggingEnabled']['TargetBucket']
        if logging_bucket != bucket['Name']:
            print(Fore.CYAN, bucket['Name'], "logs to", logging_bucket,  Style.RESET_ALL)
        else:
            print(Fore.RED, bucket['Name'], "logs to itself.", Style.RESET_ALL)            
    except:
        if less_verbose:
            pass
        else:
            print(Fore.GREEN, "{} does not have server logging enabled.".format(bucket['Name']), Style.RESET_ALL)
