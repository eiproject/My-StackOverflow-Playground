from IPython.display import clear_output

def log_in():
    global credentials
    credentials = {'user1': '123', 'user2':'234'}
    print('----Bank Login----')
    login = False
    while not login:
        u = str(input("\nUsername: "))
        while u not in credentials:
            clear_output()
            print('---Bank Login---')
            print("Username incorrect")
        else:
            clear_output()
            print("---Bank Login---")
            print(f"Username: {u}")
            p = input("\nPassword: ")
            if p == credentials[u]:
                clear_output()
                print('---Bank Login---')
                print('\nLogin Successful')
                login = True
            else:
                print("Password Incorrect")
                continue
            
log_in()