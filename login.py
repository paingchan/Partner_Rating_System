import json
import time
import bcrypt
from data import get_user_data
from dashboard import dashboard
from animation import animated_loading
# from register import register

def check_email():
    users = get_user_data()
    while True:
        email = input("Enter Your Email: ")
        user = next((user for user in users if user['email'] == email), None)
        if user:
            animated_loading()
            print("Your Account Found")
            return user  # Return the user data if the account is found
        else:
            print("Your Account Not Found")

def login():
    print("Login Page")
    
    user = check_email()  # Get the user data from check_email
    if user:
        password = input("Enter Your Password: ").encode('utf-8')
        if bcrypt.checkpw(password, user['password'].encode('utf-8')):
            animated_loading()
            time.sleep(2)
            print("\033[92mLogin Successfully\033[0m")
            dashboard(user)
        else:
            print("Incorrect Password")
    else:
        print("Exiting...")
        exit()


