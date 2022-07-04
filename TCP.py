from http import client
from pstats import SortKey
import socket
from urllib import response

target_host = "www.google.com"
target_port = 80

# membuat sebuah objek soket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# menghubungi client
client.connect((target_host,target_port))

# mengirim data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode(encoding='utf-8'))

# menerima data
response = client.recv(4096)

print(response)