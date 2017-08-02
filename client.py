
import socket
import threading
import time
import hashlib

tLock = threading.Lock()
shutdown = False
res = [False,0]
def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                global res 
                res = [True,data]
        except:
            pass
        finally:
            tLock.release()
         
       
            
            

host = '127.0.0.1'
port = 0

server = ('127.0.0.1',5001)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = input("Name: ")
message = ''
while message=='':
    message = input(alias + "-> ")
t = message
mt = ''
key = ''
while key == '':
    s.sendto(alias + ": " + message, server)
    print( res)
    if res[0]:
        data = res[1]
        if len(data.split(':')) == 2:
            st = int(data.split(':')[0])
            e = int(data.split(':')[1])
            for k in range(st,e+1):
                m = hashlib.md5()
                m.update(str(t)+str(k))
                if str(m.hexdigest()) == mt:
                    print( '-----------------------------------')
                    print( 'Key: ' + str(k))
                    print( '-----------------------------------')
                    key = str(k)
                    break
            if key !='': break
        elif len(data.split(':')) == 4: 
            d = data.split(':')
            mt = d[1]
            st = int(d[2])
            e = int(d[3])
            print((mt))
            for k in range(st,e+1):
                m = hashlib.md5()
                m.update(str(t)+str(k))
                if str(m.hexdigest()) == mt:
                    print( '-----------------------------------')
                    print( 'Key: ' + str(k))
                    print( '-----------------------------------')
                    key = str(k)
                    break
            if key !='': break
            
        print( 'not found in range - ' + res[1])
        print( 'resend')
    message = 'resend'
    time.sleep(0.1)

shudown = True
rT.join()
s.close()