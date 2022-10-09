import socket

hostname = socket.gethostname()
Ip = socket.gethostbyname(hostname)

print ("El nombre de tu ordenador es: " + hostname + " y tu direccion IP es: " + Ip)
