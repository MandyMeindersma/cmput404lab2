import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=HOST)

def connect_socket(addr):
    (family, socktype, proto, cannoname, sockaddr) = addr
    print("run")
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        print("connected")
        full_data = b""
        s.sendall(payload.encode())

        s.shutdown(socket.SHUT_WR)

        while True:
            data = s.recv(BUFFER_SIZE)

            if not data:
                break
            full_data += data
        #print(full_data)
    except:
        print("failed to connect")

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    connect_socket(addr)

if __name__ == "__main__":
    main()
