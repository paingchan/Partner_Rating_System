import time
from data import get_questions , get_user_data

questions = get_questions()
users = get_user_data()

def dashboard(user):
    if user:
        print("Welcome Our Dashboard".format(user['email']))
        choice()
    else:
        print("Sorry")
        exit()

def choice_again():
    again = input("do u choice again? (y/n): ")
    if again == "y":
        choice()
    elif again == "n":
        print("Thank u")
        exit()
    else:
        print("Please choose again")
        
def choice():
    
    #print(questions)
    response = {}
    print("Get Started to Choose People")
    
    for q in questions:
        question_id = q['id']
        question_text = q['text']
        user_input = input(f"{question_text}: ").split()
        response[question_id] = user_input

    # Parse user inputs
    interest_gender = response.get(1, [""])[0]
    min_age, max_age = map(int, response.get(2, [0, 100]))
    min_weight, max_weight = map(int, response.get(3, [0, 200]))
    min_height, max_height = map(int, response.get(4, [0, 250]))
    
    # Find people
    matched_people = []
    for person in users:
        if (interest_gender == person['gender'] or not interest_gender) and \
           (min_age <= person['age'] <= max_age) and \
           (min_weight <= person['weight'] <= max_weight) and \
           (min_height <= person['height'] <= max_height):
            matched_people.append(person)
    
    # Display matched people
    if matched_people:
        print("\nMatched People:")
        for person in matched_people:
            print(f"{'Name:':<10} {person['name']}")
            print(f"{'Age:':<10} {person['age']}")
            print(f"{'Gender:':<10} {person['gender']}")
            print(f"{'Weight:':<10} {person['weight']} kg")
            print(f"{'Height:':<10} {person['height']} cm")
            print(f"{'Contact:':<10} {person['contact']}")
            print("-" * 30)
        
    else:
        print("No matching people found.")
    
    choice_again()
    

if __name__ == "__main__":
    print("This script can't be run directly.")