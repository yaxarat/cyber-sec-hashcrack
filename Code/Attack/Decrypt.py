from pyDes import *

read_path = '../Defend/Output/encrypted.txt'
write_path = 'Output/encrypted.txt'
leaked_password = 'YMeSt0njrWizp4IAxzBI7iWQ'


# def read_passwords():
#     with open(read_path, 'rb') as f:
#         lines = [x.strip() for x in f]
#     decrypt(lines)
#
#
# def decrypt(lines):
#     write_file = open(write_path, 'w')
#     for password in lines:
#         print(password)
#         deciphered = triple_des(leaked_password).decrypt(b'B\xd5\x85*\xc0\n\xf8I', padmode=2)
#         print(deciphered)
#         #write_file.write(deciphered + '\n')
#
#
# read_passwords()
this = b'\x81\nq;\x94\xe3#\x94\xc4\x85\xe9\xb6\xb6\x0eM\xb6'
deciphered = triple_des(leaked_password).decrypt(this, padmode=2)
print(deciphered)