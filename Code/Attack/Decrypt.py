from pyDes import *

read_path = '../Defend/Output/encrypted.txt'
write_path = '../Attack/Output/decrypted.txt'
leaked_password = b'YMeSt0njrWizp4IAxzBI7iWQ'


def read_passwords():
	with open(read_path, 'rb') as f:
		decrypt(f)
	f.close()


def decrypt(lines):
	write_file = open(write_path, 'w')
	cipher = triple_des(leaked_password, padmode=PAD_PKCS5)
	line = lines.read()
	deciphered = cipher.decrypt(line, padmode=PAD_PKCS5)
	deciphered = deciphered.decode('utf-8')
	password = ''
	for c in deciphered:
		if c.isprintable():
			password = password + c
			password = password.strip()
		else:
			if password.strip() != '':
				write_file.write(password.strip() + '\n')
			password = ''
	write_file.close()


read_passwords()
