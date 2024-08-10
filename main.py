from register import register
from login import login
from animation import welcome_page , color

def main():
    
    welcome_page("Welcome")
    print(color('white') + "Start the appliaction" )

    while True:
        print("\nDo you have an account?")
        print("1. Yes, I have an account")
        print("2. No, I need to register")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
