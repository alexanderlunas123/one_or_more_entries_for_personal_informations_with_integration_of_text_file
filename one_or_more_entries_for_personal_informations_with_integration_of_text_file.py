allowed_special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
marital_status_generator = []

while True:
    while True:
        user_name = input("Name (can be username or real name): ").strip()
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
            print("")
            break
        else:
            print("Invalid input, 'Male' or 'Female' only.")
            print("Please try again.\n")

    while True:
        print("Marital Status")
        print("Choose one from the following below (type its corresponding letter):\n")
        print("A. Single")
        print("B. Married")
        print("C. Divorced")
        print("D. Widowed")
        print("E. Separated\n") 

        user_marital_status = input("").strip().capitalize()
        if user_marital_status == "A":
            marital_status_generator = ["Single"]
            break
        elif user_marital_status == "B":
            marital_status_generator = ["Married"]
            break
        elif user_marital_status == "C":
            marital_status_generator = ["Divorced"]    
            break
        elif user_marital_status == "D":
            marital_status_generator = ["Widowed"]
            break
        elif user_marital_status == "E":
            marital_status_generator = ["Separated"]
            break 
        else:
            print("Invalid input.")
            print("Please read the instruction again. Thank you.") 

    with open("user(s)_informations.txt", "a") as database:
        database.write(f"Name: {user_name}\n")
        database.write(f"Age: {user_age}\n")
        database.write(f"Address: {user_address}\n")
        database.write(f"Gender: {user_gender}\n")
        database.write("Marital Status: " + " ".join(marital_status_generator) + "\n\n")            

    while True:
        another_entry = input("Would you like to submit another entry? (Yes/No): ").strip().capitalize() 
        if another_entry == "No" or another_entry == "Yes":    
            break
        else:
            print("Invalid input, 'Yes' or 'No' only.")
            print("Please try again.")     

    if another_entry == "No":
        break
