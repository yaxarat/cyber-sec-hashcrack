# Plain text password breach

# Storing password (and possibly its hint) as a plain text in a database. This is bad
# since in case of a data breach, all passwords along with their user info will be read easily
# by the attackers.
read_path = '../Resource/raw_passwords.txt'
write_path = 'Output/plain_text.txt'


def read_passwords():
    with open(read_path) as f:
        lines = [x.strip() for x in f]
    write(lines)


def write(lines):
    write_file = open(write_path, 'w')
    for password in lines:
        write_file.write(password + '\n')


read_passwords()
