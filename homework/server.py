import os
from Crypto.Cipher import AES
from urllib.parse import *
from secret import FLAG

def pad(text):
	padding = 16 - (len(text) % 16)
	return text + bytes([padding] * padding)

def unpad(text):
	padding = text[-1]
	for char in text[-padding:]:
		assert char == padding
	return text[:-padding]

def register():
	user = input("> Username: ")
	token = urlencode({'user': user, 'admin': 'N'})
	token = aes.encrypt(pad(token.encode('utf8'))).hex()
	print(f"> Token: {token}\n")

def login():
	token = input("> Token: ")
	token = aes.decrypt(bytes.fromhex(token))
	token = parse_qs(unpad(token).decode('utf8'))
	for key, value in token.items():
		assert len(value) == 1
		if key == "admin" and value[0] == "Y":
			print(FLAG)
	print("> login finish, bye~")
	exit()

if __name__ == '__main__':
	key = os.urandom(32)
	aes = AES.new(key, AES.MODE_ECB)
	while True:
		print('> register')
		print('> login')
		print('> server.py')
		print('> exit')
		cmd = input('> Command: ')
		if cmd == 'exit': exit()
		elif cmd == 'register': register()
		elif cmd == 'login': login()
		elif cmd == 'server.py': print(open('./server.py', 'r').read())
		else: print(aes.encrypt(pad(b'Bad hacker')).hex())
