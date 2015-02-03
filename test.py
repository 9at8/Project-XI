username=""
password=""
i=0

class db():
    username=["thk98","arsh","swapnil","jatin"]
    password=["thakral","rampal","satpute","sethi"]
    name=["Aditya Thakral","Arsh Rampal","Swapnil Satpute","Jatin Sethi"]
    email=["aditya.1998thakral@gmail.com","","",""]
    phone=["9717552963","","",""]
    dep=["it","it","it","Finance"]
    pos=["Head","Head","Head"]
    lastlogin=["","",""]
    lastloc=["","",""]
    
def wait():
    print "Press enter to continue..."
    x=raw_input()
    return None

def lonely():
    print """
You are in Human Resources.
It's lonely here. We'll add someone here. Don't worry."""

def login():
    print "Please login to continue."
    global username
    global password
    global i
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
    print "Where do you want to go?"
    choice=int(raw_input("""
1. Human Resources
2. Administrative Office
3. Marketing
4. Finance
5. Assembly Line
6. Canteen
7. Washroom
8. IT Lab\nEnter a number corresponding to your choice"""))
    if choice==1:
        hr()
    elif choice==2:
        admin()
    elif choice==3:
        market()
    elif choice==4:
        finance()
    elif choice==5:
        assl()
    elif choice==6:
        cant()
    elif choice==7:
        wash()
    elif choice==8:
        it()
    else:
        print "Enter a valid choice!"
        menu()



def hr():
    lonely()
    """
recuitment
employee welfare
salary
PF
Labour Laws
admin
    """

def admin():
    lonely()
#remove admin
def market():
    lonely()
    """
product identification
market requirements
market location
category of market
    """

def finance():
    lonely()
    """
Management of cash flow
Management of expenses
Management of income
Management of Profitablity
Investments
    """
def assl():
    lonely()
    """
Components
Jig and Fixture
Testing Equipments
Assembly Lines
    """

def cant():
    lonely()

def wash():
    lonely()

def it():
    print "WIP"
    """
Server room-A/C
Database
Computers
    """
    
