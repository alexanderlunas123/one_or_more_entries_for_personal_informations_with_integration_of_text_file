

user_name = input("Name: ")
user_age = input("Age: ")
user_address = input("Full Address: ")
user_gender = input("Gender (Male/Female): ")

with open("user(s)_informations.txt", "a") as database:
    database.write(user_name + "\n")
    database.write(user_age + "\n")
    database.write(user_address + "\n")
    database.write(user_gender + "\n")