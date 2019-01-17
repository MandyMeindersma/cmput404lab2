import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

addr_info = socket.getaddrinfo("www.google.com", 80, proto=socket.SOL_TCP)
(family, socketype, proto, cannoname, sockaddr) = addr_info[0]

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1) #make socket listen
        # listen forever
        while True:
            conn, addr = s.accept() #accept incoming connections
            with conn:
                #create a socket
                with socket.socket(family, socketype) as proxy_end:
                    #connect
                    proxy_end.connect(sockaddr)
            full_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                full_data += data
            #print(full_data)
            #send data back as response
            conn.sendall(full_data)

if __name__ == "__main__":
    main()
