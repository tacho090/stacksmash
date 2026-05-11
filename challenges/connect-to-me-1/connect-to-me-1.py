from pwn import *
import ipdb
import struct
import sys

context.log_level = 'debug'

def conn():
    conn = remote('vuln.stacksmash.io', '1112')
    return conn

def exploit(conn):
    conn.recvline()
    conn.recvline()
    result = conn.recvline()

    counter = 1
    while True:
        print(f"Operation {counter}: {result}")
        if counter == 101: 
            break
        result = calculate(conn, result)
        counter += 1
        print(f"counter: {counter}")

    print(result)
    sys.exit()


def calculate(conn, result):
    expression = result.decode().strip()
    answer = int(eval(expression))
    print(f"answer: {answer}")
    conn.sendline(str(answer).encode())
    response = conn.recvline()
    conn.recvline()
    result = conn.recvline()
    return result

def main():
    process = None
    process = conn()
    exploit(process)
    process.close()

if __name__ == "__main__":
    main()
