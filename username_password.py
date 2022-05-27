import time 
usernames = ("test","test01", "test02")
passwords = ("test", "test01", "test02")
max_attemp = 3

def validator(username, password):
    isValid = False
    if username in usernames and password in passwords:
        if (list(usernames).index(username) == list(passwords).index(password)):
            isValid = True
    return isValid



attemps = 0
while True:
    username = input("Your username:")
    password = input("Your password:")
    if validator(username, password):
        print("Access Granted")
        break
    else:
        attemps+=1
        if attemps >= max_attemp:
            print("Exceed max attemps.")
            break
        
        print("Try Again (10 sec)")
        time.sleep(2)