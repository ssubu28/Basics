import socket

host = raw_input("Enter the port to be scanned: ")
ip = socket.gethostbyname(host)

print ip

while True:
    port = int(raw_input("Enter port number: "))

    try:
        s = socket.socket()
        result = s.connect((ip,port))
        print "Open Ports {}: " .format(port)
        s.close()

    except:
        print "Port {} Closed" .format(port)


print "Port scanning complete."
