import socket

def CtxUp( CtxHost ):
  try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
  except s.error as err: 
    print "socket creation failed with error %s" %(err) 
  except s.error as err: 
    print "socket creation failed with error %s" %(err) 
    
  s.settimeout(10)  
  result = s.connect_ex((CTxHost,2598))
  if result == 0:
        print "Port is open on CTxHost"
  else:
        print "Port is closed"
  s.close()
  return

for intThrOctet in range(1,255):
  CtxUp('10.0.0.'+str(intThrOctet))
  CtxUp('10.1.0.'+str(intThrOctet))
