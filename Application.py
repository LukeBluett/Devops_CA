import pymongo
from pymongo import MongoClient
import pprint

def check_username(username):
    if username == 'Luke':
        return True
    else:
        return False

def check_password(password):
    if password == 'password1234':
        return True
    else:
        return False

def connect_to_mongo(ip_address, port_number):
    return MongoClient(ip_address, port_number)

def list_db():
    print("List")
    posts = db.posts
    for post in posts.find():
        pprint.pprint(post)


def add_db():
    print("Add")
    account = raw_input("Account? ")
    password = raw_input("Password? ")
    post = {"Account": account, "Password": password}
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id

def remove_db():
    print("remove")
    account = raw_input("Enter account: ")
    password = raw_input("Enter password: ")
    result = db.posts.delete_many({"Account": account, "Password": password})

if __name__ == '__main__':
    print("\n***Welcome to the password manager***\n\n")

    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    ip_address = raw_input("Enter your ip address for Mongo: ")
    port_number = raw_input("Enter your port for Mongo: ")

    client = ''
    if check_username(username):
        if check_password(password):
            client = connect_to_mongo(ip_address, int(port_number))
        else:
            print("Error")
            quit()
    else:
        print("Error")
        quit()

    db = client.password_database
    collection = db.password_collection


    message = "\nSelect an option: \n\t1:list \n\t2:add \n\t3:remove \n\t4:quit \n"

    print(message)

    choice = int(raw_input("Choice? (1,2,3,4) "))

    while choice != 4:
        if choice == 1:
            list_db()
        elif choice == 2:
            add_db()
        elif choice == 3:
            remove_db()
        else:
            print("Invalid choice")

        choice = int(raw_input("Choice? (1,2,3,4) "))

    print("Exiting... Goodbye")
