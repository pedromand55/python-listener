import socket

# Set up the listener
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 443))
s.listen(1)

# Accept incoming connections
conn, addr = s.accept()

# Run a command loop
while True:
    cmd = input('Enter command: ')
    if cmd == 'exit':
        break
    conn.send(cmd.encode())
    result = conn.recv(10000)
    print(result.decode())

# Close the connection
conn.close()
