from cryptography.fernet import Fernet
'''def write_key():
  key= Fernet.generate_key()
  with open("key.key","wb") as keyf:
    keyf.write(key)
write_key()'''
def load():
  file=open("key.key","rb")
  key=file.read()
  file.close()
  return key
main_pass=input("Enter the main password")
key= load()+main_pass.encode()
fer=Fernet(key)



def add():
    name=input("Enter username")
    pw=input("Enter password")
    with open("passwords.txt",'a') as f:
        f.write(name+"|"+fer.encrypt(pw.encode()).decode()+"\n")
def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            tx=line.rstrip()#strips \n
            user,pwd=tx.split("|")
            print("Username:",user,"Password:",(fer.decrypt(pwd.encode()).decode()))
while True:
    mode=input("add new password(a) or view(v)")
    if mode=="q":
        break
    elif mode=="v":
        view()
    elif mode=="a":
        add()