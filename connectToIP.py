import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening


def connectto(host, port=6653):
    server_address = (host, port)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    try:

        # Send data
        message = b'\xf0\x00\x00\x14\x00'
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(40)
            amount_received += len(data)
            print('received %s' % data)
            print('numeric value of 1st byte %s' % data[0])
            print('numeric value of 2nd byte %s' % data[1])
    finally:
        print('closing socket')
        sock.close()


# while True:
#     try:
#         Host = str(input("Please Enter IP address: "))
#         Port = int(input("Please Enter Port (Optional, Default: 6653) : ") or "6653")
#         break
#
#     except ValueError:
#         print("Not valid input! Please try again ...")


Host = b'172.16.108.212'
Port = 6653
connectto(Host, Port)
