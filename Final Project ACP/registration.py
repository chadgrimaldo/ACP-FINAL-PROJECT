from utils import get_valid_number

users = []

def register_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    school = input("Enter your school: ")
    phone = get_valid_number("Enter your phone number: ")
    user = {'name': name, 'email': email, 'school': school, 'phone': phone}
    users.append(user)
    print("Registration successful!")
