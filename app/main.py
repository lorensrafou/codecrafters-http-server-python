@@ -1,16 +1,10 @@

import socket
def main():
def main():
    
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept() # wait for client
if __name__ == "__main__":
    main()