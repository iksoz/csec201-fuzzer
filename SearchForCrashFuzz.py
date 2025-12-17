import socket,time

ip ='10.0.2.15' #vm ip
port = 2223
def attack(payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#connects to the server
        s.connect((ip, port))
        response = s.recv(1024)    # <-- wait for reply
        print(str(response)+'\n')
        time.sleep(0.3)
        s.sendall(payload)
        time.sleep(0.3)
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
    for i in range(1,100):
        
        garbage = b'INC ' +b'1'*i+b'ZIFE'+b'3\n'#repeatedly sents bytes by increments of 10
        try:
            attack(garbage)
            print(str(i+5)+" characters sent")
        except:
            print("Crash at " + str(i+5) + " bytes")#identifies when the program crashes
            break
        

def main(): 
    fuzzer()
    #connect()

if __name__ == '__main__':
    main()