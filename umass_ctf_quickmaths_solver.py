#!/usr/bin/python3

from pwn import *
import time

def calculate(l=list):
     if "//" == l[1]:
         return (int(l[0]) // int(l[2]))
     if "+" == l[1]:
         return (int(l[0]) + int(l[2]))
     if "-" == l[1]:
         return (int(l[0]) - int(l[2]))
     if "*" == l[1]:
         return (int(l[0]) * int(l[2]))


if __name__ == "__main__":
    r = remote('34.148.103.218', 1228)
    response = r.recv().decode()
    solve = response[response.find('\n\n')+2:]
    solve = solve.strip()
    print(solve)
    solve = solve.split(' ') 
    r.sendline(str(calculate(solve)).encode())
    print(r.recvline().decode())

    for i in range(999):
        print(f"[+] Attempts: {i + 1}")
        try:
            response = r.recvline(timeout=20)
        except EOFError:
            time.sleep(3)
            try:
                response = r.recvline()
            except:
                time.sleep(3)
                response = r.recvline()
        print(response.decode())
        solve = response.decode()
        solve = solve.strip()
        solve = solve.split(' ') 
        r.sendline(str(calculate(solve)).encode())
        time.sleep(0.2)
        print(r.recvline(timeout=20).decode())
    
    print(r.recv(timeout=10).decode())
