import socket

host = input("Enter target host: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("\nPort Status")
print("-" * 30)

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()