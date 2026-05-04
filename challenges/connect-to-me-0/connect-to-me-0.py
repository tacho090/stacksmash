from pwn import *

def conn():
    conn = remote('vuln.stacksmash.io', '1111')
    data = conn.recvline()
    conn.close()
    return data

if __name__ == "__main__":
    result = conn()
    print(result)
