sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('10.14.10.216',1494))

for intThrOctet in range(1,255):
  CtxUp ('10.14.10.'+intThrOctet)
  
def CtxUp ( CtxHost )
  result = sock.connect_ex(('10.14.10.216',1494))
  if result == 0:
        print "Port is open"
  else:
        print "Port is closed"
  sock.close()
return
