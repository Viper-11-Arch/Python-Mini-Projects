from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)'''

def load_key():
    file = open('key.key',"rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Create Your Master Password: ")
key = load_key()
fer = Fernet(key)


def add():
    username = input("Enter UserName:")
    password = input("Enter Password:")
    with open("passwords.txt",'a') as f:
        f.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("UserName: ",user," | Password: ", fer.decrypt(passw.encode()).decode())

while True:
    mode = input("Enter the Mode(view/add) or Enter Q to quit: ").lower()

    if mode == 'q':
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Choice")

