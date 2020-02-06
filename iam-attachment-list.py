#!/usr/bin/env python3

"""
Simple script to list all entities a list o policies is attached to
"""

import sys
import boto3
import colorama
from colorama import Fore, Style

#declare variables

profile = 'default'
policy_list_file = 'sqs_policies.txt'

#read role file

policies_file_FH = open(policy_list_file, "r")
if policies_file_FH.mode == 'r':
    policies = policies_file_FH.readlines()

#create boto session and client
session = boto3.Session(profile_name = profile)
iam_client = session.client('iam', region_name='us-east-1')

for i in policies:
    policyarn = "arn:aws:iam::600690756780:policy/{}".format(i).rstrip('\r|\n')
    try:
        response = iam_client.list_entities_for_policy(PolicyArn = policyarn)
    except Exception as e:
        print(e)
    else:
        print("\n", Fore.GREEN, i, Style.RESET_ALL)

        #print groups
        for j in response['PolicyGroups']:
            try:
                print('Group:', j['GroupName'])
            except:
                pass
        
        #print roles
        for x in response['PolicyRoles']:
            try:
                print('Role:', x['RoleName'])
            except:
                pass

        #print users
        for y in response['PolicyUsers']:
            try:
                print('User:', y['UserName'])
            except:
                pass

