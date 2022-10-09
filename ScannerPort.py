import sys
import socket

obj = socket.gethostbyname(input("Inserte la IP: "))

print("Escaneando objetivo. . ." + obj)

try: 
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        res = s.connect_ex((obj, port))
        if res == 0:
            print("El puerto {} esta abierto".format(port))
            s.close()
except:
    print("\n saliendo. . .")
    sys.exit(0)

    
