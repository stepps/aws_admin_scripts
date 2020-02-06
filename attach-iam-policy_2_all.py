#!/usr/bin/env python3

"""
Simple script to apply an IAM policy to all user matching a pattern (an @ in this case)
"""

import sys
import boto3
import colorama
from colorama import Fore, Style

#declare variables

profile = 'default'
policy_arn = 'arn:aws:iam:::policy/KMS-usage-all-keys'

#create boto session and client
session = boto3.Session(profile_name = profile)
iam_client = session.client('iam', region_name='us-east-1')

#get users list

response = iam_client.list_users(MaxItems=300)

for i in response['Users']:
    if '@' not in i['UserName']:
        try:
            iam_client.attach_user_policy(
                UserName=i['UserName'],
                PolicyArn=policy_arn
                )
        except Exception as e:
            print(Fore.RED, "It was not possible to attach the policy to user {}".format(i['UserName']), Style.RESET_ALL)
        else:
            print(Fore.GREEN, i['UserName'], Style.RESET_ALL)
