from pwn import *
import struct

def pack32(number):
    # little endian 32 bit version of passed number
    # this is the hardcoded address for the 'win' function in main.c
    # the address was copied from the objdump
    return struct.pack(">I", number)

def conn():
    conn = remote('vuln.stacksmash.io', '1112')
    # print(conn.recvall())
    return conn

def exploit(conn):
    conn.recvline()
    conn.recvline()
    conn.recvline()
    conn.interactive()
    # conn.recvline()
    # conn.recvuntil(b'>')
    conn.sendline(b'123')
    result = conn.recvline()
    return result

def main():
    process = None
    process = conn()
    # print(exploit(process))
    process.close()

if __name__ == "__main__":
    main()
