#!/usr/bin/env python3

import requests
import sys
import json

if len(sys.argv) == 1: # If no files are specified print the error and exit.
    print("[ERROR] You need to specify one or more files!")

for filename in sys.argv[1:]: # For every file specified.
    try:
        files = {'file': (open(filename, 'rb'))} # Opens the file and creates a dictionary.
    except FileNotFoundError: # If the file doesn't exist.
        print(f'[ERROR] The file "{filename}" doesn\'t exist!')
        continue # Continues the loop for any valid files.
    except IsADirectoryError: # If the file is a directory and not a file.
        print(f'[ERROR] You cannot upload a directory!')
        continue # Continues the loop for any valid files.
    r = requests.post('https://anonfile.com/api/upload', files=files) # HTTP Request to the API.
    print("[UPLOADING]", filename)
    request_dict = json.loads(r.text)
    if request_dict['status']:
        data = request_dict['data']
        file = data['file']
        urls = file['url']
        urlshort = urls['short']
        urllong = urls['full']
        print(f'[SUCCESS] Your file has been succesfully uploaded:\nFull URL: {urllong}\nShort URL: {urlshort}')
    else: # If the GET request returns an error
        error = request_dict['error']
        message = error['message']
        errtype = error['type']
        print(f'[ERROR] {message}\n{errtype}') # Prints the error
