from pyDes import *

read_path = '../Resource/raw_passwords.txt'
write_path = 'Output/encrypted.txt'


def read_passwords():
    with open(read_path) as f:
        lines = [x.strip() for x in f]
    encrypt(lines)


def encrypt(lines):
    write_file = open(write_path, 'w')
    for password in lines:
        ciphered = triple_des('YMeSt0njrWizp4IAxzBI7iWQ').encrypt(password, padmode=2)
        write_file.write(str(ciphered) + '\n')


read_passwords()
