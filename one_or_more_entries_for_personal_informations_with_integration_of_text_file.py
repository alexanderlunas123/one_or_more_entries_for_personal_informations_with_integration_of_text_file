allowed_special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

while True:
    while True:
        user_name = input("Name: ").strip()
        replacing_spaced_names = user_name.replace(" ", "")
        if all(char.isalpha() or char in allowed_special_characters for char in replacing_spaced_names):
            break 
        elif replacing_spaced_names.isdigit():
            print("Invalid input, can't have numbers.")
        else:
            print("The inputted character(s) is/are invalid.")
            print("Please try again.")

    while True:
        user_age = input("Age: ").strip()
        if user_age.isdigit():
            integered_user_age = int(user_age)
            if integered_user_age <= 120:
                break  
            else:
                print("Invalid input, age must be less than or equal to 120.")
        else:
            print("Invalid input, must be a digit.")
            print("Please try again.")

    while True:
        user_address = input("Full Address: ").strip()
        replacing_spaced_names_2 = user_address.replace(" ", "")
        if all(char.isalnum() or char in allowed_special_characters for char in replacing_spaced_names_2):
            break 
        else:
            print("The inputted character(s) is/are invalid.")
            print("Please try again.")

    while True:
        user_gender = input("Gender (Male/Female): ").strip().capitalize()
        if user_gender == "Male" or user_gender == "Female":
            break 
        else:
            print("Invalid input, 'Male' or 'Female' only.")
            print("Please try again.")






with open("user(s)_informations.txt", "a") as database:
    database.write(user_name + "\n")
    database.write(user_age + "\n")
    database.write(user_address + "\n")
    database.write(user_gender + "\n")