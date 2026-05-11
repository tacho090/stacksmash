from pwn import *

context.log_level = 'debug'

def connect():
    conn = remote('ftp.ubuntu.com', 21)
    conn = recvline()

def connect_to_process():
    io = process('sh')
    io.sendline('echo Hello, world')
    io.recvline()

def export_env():
    io = process(['sh', '-c', 'echo $MYENV'], env={'MYENV': 'MYVAL'})
    io.recvline()

if __name__ == "__main__":
    # export_env()
    connect_to_process()

