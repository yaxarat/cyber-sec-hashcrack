read_path = '../Defend/Output/hashed_sha1.txt'
table = '../Resource/raw_passwords.txt'

rainbow = []


def read_passwords(hashcode):
    global rainbow

    with open(table, 'r') as f:
        rainbow = [x.strip() for x in f]

    with open(read_path, 'r') as f:
        lines = [x.strip() for x in f]
    lookup(lines, hashcode)


def lookup(dictionary, hashcode):
    i = 1

    for line in dictionary:
        if hashcode == line:
            print('SHA1: Result')
            print(rainbow[i+1])
        else:
            i += 1


read_passwords('d30afd521506d7d66c4a0954cc3948f16791eb05')
