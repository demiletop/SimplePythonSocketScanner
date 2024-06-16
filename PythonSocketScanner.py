import socket

# By https://demile.top/

domain = "google.com"
ip = socket.gethostbyname(domain)
print(ip)

#Get hostname, alias, and IP addresses from an IP address
host_info = socket.gethostbyaddr(ip)
print(host_info)

# Define the list with integers
ports = [21, 22, 23, 25, 53, 80, 110, 143, 389, 443, 445, 990, 993, 995, 1433, 1434, 3389]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)  # Set a timeout of 1 second

# Sort the list in ascending order
sorted_numbers = sorted(ports)

# Print each number in the sorted list
for port in sorted_numbers:
    try:
        # connect to the IP address and port
        s.connect((ip, port))
        s.shutdown(socket.SHUT_RDWR)
        print("Port " + str(port) + " " + socket.getservbyport(port, 'tcp') + " on IP " + ip + " is open")
        
    except (socket.timeout, socket.error):
        print("Port " + str(port) + " " + socket.getservbyport(port, 'tcp') + " on IP " + ip + " is closed")
    finally:
        s.close()  # Close the socket after each attempt to connect
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Re-create socket object    

    
s.close()
