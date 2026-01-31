# defy new login
def new_login():
    email = input("Email: ")
    password = input("Password: ")
    website = input("Website: ")
    
    with open("vault.txt", "a") as file:
        file.write("Email: " + email + " | "  + "Password: " + password + " | " + " Website: " + website)

# defy check logins
def check_logins():
    with open("vault.txt", "r") as file:
        content = file.read()
        print(content)


# welcome 'screen'
print("Password vault! Save and remember your passwords for websites!")

# asks what to do
pick = input("1. Add a new login\n2. Look at existing logins ")


# picking
if pick == "1":
    new_login()  # <---- () for actually calling the def func
elif pick == "2":
    check_logins() # <---- () for actually calling the def func
else:
    print("Wrong number!")