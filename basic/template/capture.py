# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: capture one TCP connection
# Created: 2024.01.01
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/01    basic build success
# -----------------------------

import socket
import subprocess
import atexit

import re


class Monitor():
    def __init__(self, PID: int):
        self.on_init(PID)

    def on_init(self, PID: int):
        self.____PID____ = PID
        self.____port____ = None
        
        netstat = subprocess.run(f"netstat -ano | findstr {self.____PID____}", 
                                capture_output=True, text=True, check=True, shell=True)
        self.____host_ip____ = socket.gethostbyname(socket.gethostname())
        pattern = re.compile(f'{re.escape(self.____host_ip____)}:(\d+)')
        if match:= pattern.search(netstat.stdout):
            self.____port____ = int(match.group(1))

        atexit.register(self.on_exit)

    def on_exit(self):
        if hasattr(self, 'socket_server'):
            self.socket_server.close()

    def on_start(self):
        if not self.____port____:
            return

        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        self.socket_server.bind((self.____host_ip____, self.____port____))        
        
        self.socket_server.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        print(f"Capturing packets on port {self.____port____}...")

        try:
            while True:
                data, addr = self.socket_server.recvfrom(65535)
                print(f"Received packet from {addr}: {data}")
        except KeyboardInterrupt:
            print("Capture stopped.")
        

if __name__ == "__main__":
    ins = Monitor()  # it needs a PID
    
    try:
        ins.on_start()
    except KeyboardInterrupt:
        import sys
        sys.exit()
