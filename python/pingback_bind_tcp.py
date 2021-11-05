import binascii as b
import socket as s
o=s.socket(s.AF_INET,s.SOCK_STREAM)
try:
 o.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
 o.bind(('0.0.0.0', 4444))
 o.listen(1)
 o,addr=o.accept()
 o.send(b.a2b_base64('rIVjTxgXS+qYCF41ttKDvg=='))
 o.close()
except:
 pass
