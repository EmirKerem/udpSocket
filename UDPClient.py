import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Ask about...('History' or 'Weather in Istanbul') Press Q for Quit" )
    if msg == 'Q':
        break
    client.sendto(msg.encode(),("127.0.0.1",2424))
    ans ,addr = client.recvfrom(1024)
    print("Answer is : ",ans.decode())

client.close()