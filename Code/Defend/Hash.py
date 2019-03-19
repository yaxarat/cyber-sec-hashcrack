import hashlib

read_path = '../Resource/raw_passwords.txt'
write_path = 'Output/hashed_sha1.txt'


file = open(read_path, "r")
hashed_file = open(write_path, "w")
for line in file:
    eachpwd = line.strip().encode('utf-8')

    sha_1 = hashlib.sha1()
    sha_1.update(eachpwd)
    hashed_file.write(sha_1.hexdigest() + '\n')
