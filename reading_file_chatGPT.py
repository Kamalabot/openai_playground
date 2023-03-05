#!/usr/bin/env python
import json, openai
import warnings
import os
warnings.filterwarnings('ignore')
import configparser
import datetime
#reading in the config file with secrets
readKey = configparser.ConfigParser()
readKey.read_file(open('apidata.config'))
#attaching secrets to the python variables
openai_org = readKey['OPENAI']["ORG"]
openai_key = readKey['OPENAI']['KEY'] 

#Function that recieves the replies from chatgpt api end point
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
file_location = input("provide full path of file location: ")

with open(file_location,'r') as chat:
    data = chat.readlines()

replies = []
#ignoring the first line of the data, as it will be headers role , prompt
for ind,line in enumerate(data[1:]):
    print(f'Reading your prompt number: {ind + 1}')
    get_role = line.split(',')[0] 
    get_prompt = line.split(',')[1] 
    content_output = extract_response(org=openai_org, key=openai_key, 
                 role_player=get_role, request_content=get_prompt)
    print(f'Reply for {ind} prompt: {content_output}',end='\n')
    #making content for saving
    prompt_data = [get_role, get_prompt,f'Reply for {ind} prompt: {content_output}']
    #appending the content to list
    replies.append(prompt_data)

#checking for user request to make file
need_copy = input(f'I have {len(replies)} replies stored in memory do you want a copy (y/n): ')
#if yes then proceed to next step 
if need_copy == 'y' or need_copy == 'Y':
    #request for the file name
    destination = input('Provide me the file name to write the content')
    print('Writing it to file')
    output_loc = f'/run/media/solverbot/repoA/gitFolders/{destination}'
    with open(output_loc, 'w+') as reply:
        for ind,line in enumerate(replies):
            #have to write the string of data
            print(f'Reply for prompt {ind + 1} \n,Role is {line[0]}\n, Prompt is {line[1]}\n, and Reply is :{line[2]}')
            reply.write(f'Reply for prompt {ind + 1} \n,Role is {line[0]}\n, Prompt is {line[1]}\n, and Reply is :{line[2]}')

#ending the program
print('Written to file. Thanks for spending time with me.')
