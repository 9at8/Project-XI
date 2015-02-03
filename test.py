import db

username=""
password=""

class db():
    username=["aditya","arsh","swapnil"]
    password=["thakral","rampal","satpute"]
    name=["Aditya Thakral","Arsh Rampal","Swapnil Satpute"]
    email=["","",""]
    phone=["","",""]
    dep=["admin","admin","admin"]
    lastlogin=["","",""]
    lastloc=["","",""]
    
def wait():
    print "Press enter to continue..."
    x=raw_input()
    return None

def login():
    print "Please login to continue."
    global username
    global password
    username=raw_input("Username: ")
    password=raw_input("Password: ")
    if username in db.username:
        for i in range (0,len(db.username)):
            if username==db.username[i]:
                break
            else:
                i+=1
        if password==db.password[i]:
            wait()
        else:
            print "Incorrect username or/and password."
    else:
        print "Incorrect username or/and password."
