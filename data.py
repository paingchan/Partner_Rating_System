import json

def get_user_data():
    with open('data/users.json' , 'r') as file:
        users_data = json.load(file)
    return users_data['Users']

def save_user_data(users):
    with open('data/users.json', 'w') as file:
        json.dump({'Users' : users},file,indent=4)
    
def get_questions():
    with open('data/questions.json', 'r') as file:
        data = json.load(file)
        return data['Questions']