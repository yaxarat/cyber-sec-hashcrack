# Plain text password breach

# Storing password (and possibly its hint) as a plain text in a database. This is bad
# since in case of a data breach, all passwords along with their user info will be read easily
# by the attackers.

raw_path = '../Resource/raw_passwords.txt'


def read_passwords():
    with open(raw_path) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        return lines


print read_passwords()
