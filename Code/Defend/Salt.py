import hashlib
import os

read_path = '../Resource/raw_passwords.txt'
write_path = 'Output/salted_hashes.txt'


file = open(read_path, "r")
hashed_file = open(write_path, "w")
for line in file:
	salt = os.urandom(16)
	eachpwd = line.strip().encode('utf-8')
	eachpwd = salt + eachpwd
	sha_1 = hashlib.sha1()
	sha_1.update(eachpwd)
	hashed_file.write(sha_1.hexdigest() + ' , ' + str(salt) + '\n')
