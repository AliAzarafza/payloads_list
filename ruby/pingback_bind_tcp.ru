require'socket';
s=TCPServer.new(4444);
c=s.accept;s.close;
c.puts'EVkqcHWWQr6Cyzb2qr0TUw=='.unpack('m0');