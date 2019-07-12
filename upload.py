#!/usr/bin/env python3

import requests
import sys
import json

if sys.argv == []:
    print(["[ERROR] You need to specify one or more files!"])

for filename in sys.argv[1:]:
    try:
        files = {'file': (open(filename, 'rb'))}
    except FileNotFoundError:
        print(f'[ERROR] The file "{filename}" doesn\'t exist!')
        exit(1)
    except IsADirectoryError:
        print(f'[ERROR] You cannot upload a directory!')
        exit(1)
    r = requests.post('https://anonfile.com/api/upload', files=files)
    print("[UPLOADING]", filename)
    request_dict = json.loads(r.text)
    if request_dict['status']:
        data = request_dict['data']
        file = data['file']
        urls = file['url']
        urlshort = urls['short']
        urllong = urls['full']
        print(
            f'[SUCCESS] Your file has been succesfully uploaded:\nFull URL: {urllong}\nShort URL: {urlshort}')
    else:
        error = request_dict['error']
        message = error['message']
        errtype = error['type']
        print(f'[ERROR] {message}\n{errtype}')
