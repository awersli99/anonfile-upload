#!/usr/bin/env python3

import requests
import sys
import json

url = 'https://api.anonfiles.com/upload'

if len(sys.argv) == 1:
    print("[ERROR] You need to specify one or more files!")

for filename in sys.argv[1:]:
    try:
        files = {'file': (open(filename, 'rb'))}
    except FileNotFoundError:
        print(f'[ERROR] The file "{filename}" doesn\'t exist!')
        continue
    except IsADirectoryError:
        print('[ERROR] You cannot upload a directory!')
        continue
    r = requests.post(url, files=files)
    print("[UPLOADING]", filename)
    request_dict = json.loads(r.text)
    if request_dict['status']:
        urlshort = request_dict['data']['file']['url']['short']
        urllong = request_dict['data']['file']['url']['full']
        print(f'[SUCCESS] Your file has been succesfully uploaded:\nFull URL: {urllong}\nShort URL: {urlshort}')
    else:
        message = request_dict['error']['message']
        errtype = request_dict['error']['type']
        print(f'[ERROR] {message}\n{errtype}')
