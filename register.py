import time
import re
import bcrypt
from data import get_user_data , save_user_data
from login import login


def email_input():
    users = get_user_data()
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    while True:
        email = input("Enter your email: ").strip()
        if not email:
            print("Email cannot be empty")
            continue
        if not email_pattern.match(email):
            print("Invalid email format")
            continue
        if any(user['email'] == email for user in users):
            print("Email already in use")
        else:
            return email

def hash_password( password: str ) -> str:
    
    hashed = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    return hashed.decode('utf-8')

def password_input(prompt: str) -> str:
    while True:
        password = input(prompt).strip()
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        
        hashed_password = hash_password(password)
        return hashed_password

def gender_input():
    
    valid_genders = { "male" , "female"}
    
    while True:
        gender = input("Enter your gender (male  of female): ").strip().lower()
        
        if gender in valid_genders:
            return gender
        else:
            print("Invalid gender , Please enter male or female ")

def interger_input(prompt):
    while True:
        value = input(prompt).strip()
        if  value.isdigit():
            return int(value)
        else:
            print("Invalid Input , Please Input Number eg: 30")
    

def register():

        users = get_user_data()
        
        name = input("Enter your username: ")
        email = email_input()
        password = password_input("Enter your password: ")
        print("\033[92mYour Password Successfully Encrypted\033[0m")
        gender = gender_input()
        age = interger_input("Enter your age: ")
        weight = interger_input("Enter your weight (kg): ")
        height = interger_input("Enter your height (cm): ")
        contact = input("Enter your contact: ")

        new_id = max(user['id'] for user in users) + 1 if users else 1
        new_user = {
            "id" : new_id,
            "name" : name,
            "email" : email,
            "password" : password,
            "age" : age,
            "gender" : gender,
            "weight" : weight,
            "height" : height,
            "contact" : contact      
        }
        
        users.append(new_user)
        save_user_data(users)
        print('Processing....')
        time.sleep(2)
        print("\033[92mSuccessfully Registered\033[0m")
        login()
    
