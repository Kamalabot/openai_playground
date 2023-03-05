#!/usr/bin/env python
import json, openai
import warnings
import os
warnings.filterwarnings('ignore')
import configparser
import datetime

readKey = configparser.ConfigParser()
readKey.read_file(open('apidata.config'))

openai_org = readKey['OPENAI']["ORG"]
openai_key = readKey['OPENAI']['KEY'] 

def extract_response(org,key,role_player,request_content):
    openai.organization = org
    openai.api_key= key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", 
             "content": f"You are a {role_player}"},
            {"role": "user", 
             "content": request_content}
            ]
        )
    return response['choices'][0]['message']['content']

get_role = input("What role you want me to play: ")
while True:
    get_prompt = input("Give the prompt here: ")
    content_output = extract_response(org=openai_org, key=openai_key, 
                 role_player=get_role, request_content=get_prompt)
    print(content_output,end='\n')

    exit_q = input("Want to Exit? y / n : ")
    if exit_q == 'y' or exit_q == 'Y':
        print("Thanks for spending time with me")
        break

