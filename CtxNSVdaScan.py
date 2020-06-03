import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def CtxUp( CtxHost ):
  try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "Socket successfully created"
  except socket.error as err: 
    print "socket creation failed with error %s" %(err) 
    
  result = sock.connect_ex(('10.14.10.216',1494))
  if result == 0:
        print "Port is open"
  else:
        print "Port is closed"
  sock.close()
return

for intThrOctet in range(1,255):
  CtxUp('10.14.10.'+intThrOctet)
  
