def passwd_to_dict(file):
    users = {}
    with open(file, 'r') as f:
        for line in f:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
        return users


print(passwd_to_dict(r'C:\Users\Paul\Desktop\passwd.txt'))
