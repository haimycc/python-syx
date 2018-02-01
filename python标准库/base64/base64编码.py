import base64

MESSAGE = "hello,world"
file=open("out.txt","w")
file.write(MESSAGE)
file.close()

base64.encode(open("out.txt"),open("outbase64.txt","w"))


