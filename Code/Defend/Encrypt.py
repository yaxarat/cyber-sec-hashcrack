from pyDes import *

read_path = '../Resource/raw_passwords.txt'
write_path = 'Output/encrypted.txt'


def read_passwords():
    with open(read_path) as f:
        lines = [x.strip() for x in f]
    encrypt(lines)


def encrypt(lines):
    write_file = open(write_path, 'wb')
    ciphered = triple_des(b'YMeSt0njrWizp4IAxzBI7iWQ', padmode=PAD_PKCS5)
    for password in lines:
        password = password.encode('utf-8')
        encrypted = ciphered.encrypt(password, padmode=PAD_PKCS5)
        print(encrypted)
        write_file.write(encrypted)


read_passwords()
