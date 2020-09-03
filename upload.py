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
    resp = json.loads(r.text)
    if resp['status']:
        urlshort = resp['data']['file']['url']['short']
        urllong = resp['data']['file']['url']['full']
        print(f'[SUCCESS] Your file has been succesfully uploaded:\nFull URL: {urllong}\nShort URL: {urlshort}')
    else:
        message = resp['error']['message']
        errtype = resp['error']['type']
        print(f'[ERROR] {message}\n{errtype}')
