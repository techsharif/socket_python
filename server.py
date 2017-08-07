
import socket
import time
import random
import hashlib
host = '127.0.0.1'
port = 5001

# clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False
print "Server Started."
while not quitting:
    try:
        data, client = s.recvfrom(1024)

        
        if "Quit" in str(data):
            quitting = True


        tdata = data
        data = data.split(': ')[1]
        if data!='resend':
            print 'request: '+data
            print time.ctime(time.time()) + str(client) + ": :" + str(tdata)

        

        a = 0
        b = 99999999
        key = random.randint(a, b)
        range_start = random.randint(a, b)
        range_end = random.randint(range_start, b)
        
        if data=='resend0':
            # print str(range_start)+':'+str(range_end)
            s.sendto(str(int(a))+':'+str(int(b/4)+1), client)
        elif data=='resend1':
            # print str(range_start)+':'+str(range_end)
            s.sendto(str(int(b/4)-1)+':'+str(int(b/2)+1), client)
        elif data=='resend2':
            # print str(range_start)+':'+str(range_end)
            s.sendto(str(int(b/2)-1)+':'+str(int(b*3/4)+1), client)
        elif data=='resend3':
            # print str(range_start)+':'+str(range_end)
            s.sendto(str(int(b*3/4)-1)+':'+str(int(b)), client)
        elif data=='resend4':
            # print str(range_start)+':'+str(range_end)
            s.sendto(str(a)+':'+str(b), client)
        else: 
            m = hashlib.md5()
            m.update(str(data)+str(key))
            # print(str(m.hexdigest()))
            t = data
            mt = str(m.hexdigest())
            rng = str(range_start)+':'+str(range_end)
            message = t+':'+mt+':'+rng
            print message
            print 'Key: ' + str(key)
            s.sendto(message, client)
    except:
        pass
s.close()