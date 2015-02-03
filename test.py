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
            #continue program
        else:
            print "Incorrect username or/and password."
    else:
        print "Incorrect username or/and password."

def menu():
    print "Where do you want to go"
    choice=raw_input("""
1. Human Resources
2. Administrative Office
3. Marketing
4. Finance
5. Assembly Line
6. Canteen
7. Washroom
8. IT office\n""")
 
    
        
