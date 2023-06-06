import os
from cryptography.fernet import Fernet

my_list = []

def decrypt():
	global my_list
	
	for file in os.listdir():
		if file =="randomware.py" or file =="my_key.key" or file == "decrypt.py":
			continue
			
		if os.path.isfile(file):
			my_list.append(file)
	
	key = Fernet.generate_key()
	
	with open("my_key.key","rb") as read_encrypt:
		my_hash = read_encrypt.read()
		
	for file in my_list:
		with open(file,"rb") as readfile:
			content = readfile.read()
			content_decrypt = Fernet(my_hash).decrypt(content)
			with open(file,"wb") as writefile:
				writefile.write(content_decrypt)
		
decrypt()
