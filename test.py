import time

username=""
password=""
i=0

#for saving database
"""
ab=open("username.txt","a")
user=raw_input("Enter new username.")
ab.write(user)
"""

class db():
    with open("DATABASE/username.txt") as _1_:
        username=_1_.readlines()
    for _1 in range (len(username)-1):
        username[_1]=(username[_1])[:(len(username[_1])-1)]
        
    with open("DATABASE/password.txt") as _2_:
        password=_2_.readlines()
    for _2 in range (len(password)-1):
        password[_2]=(password[_2])[:(len(password[_2])-1)]
        
    with open("DATABASE/name.txt") as _3_:
        name=_3_.readlines()
    for _3 in range (len(name)-1):
        name[_3]=(name[_3])[:(len(name[_3])-1)]

    with open("DATABASE/email.txt") as _4_:
        email=_4_.readlines()
    for _4 in range (len(email)-1):
        email[_4]=(email[_4])[:(len(email[_4])-1)]
        
    with open("DATABASE/phone.txt") as _5_:
        phone=_5_.readlines()
    for _5 in range (len(phone)-1):
        phone[_5]=(phone[_5])[:(len(phone[_5])-1)]
        
    with open("DATABASE/dep.txt") as _6_:
        dep=_6_.readlines()
    for _6 in range (len(dep)-1):
        dep[_6]=(dep[_6])[:(len(dep[_6])-1)]
        
    with open("DATABASE/pos.txt") as _7_:
        pos=_7_.readlines()
    for _7 in range (len(pos)-1):
        pos[_7]=(pos[_7])[:(len(pos[_7])-1)]
        
    with open("DATABASE/lastlogin.txt",) as _8_:
        lastlogin=_8_.readlines()
    for _8 in range (len(lastlogin)-1):
        lastlogin[_8]=(lastlogin[_8])[:(len(lastlogin[_8])-1)]
        
    with open("DATABASE/lastloc.txt") as _9_:
        lastloc=_9_.readlines()
    for _9 in range (len(lastloc)-1):
        lastloc[_9]=(lastloc[_9])[:(len(lastloc[_9])-1)]
    
def wait():
    print "Press enter to continue..."
    x=raw_input()

def lonely():
    print """
It's lonely here. We'll add someone. Don't worry."""

def cls():
    print "\n"*100

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
            _y=str((time.localtime())[0])
            _m=str((time.localtime())[1])
            _d=str((time.localtime())[2])
            _h=str((time.localtime())[3])
            _min=str((time.localtime())[4])
            _s=str((time.localtime())[5])
            temp="\n"+_d+"/"+_m+"/"+_y+" - "+_h+":"+_min+":"+_s+"\n"
            db.lastlogin[i]=temp
            print db.lastlogin
            menu()
        else:
            print "Incorrect username or/and password."
    else:
        print "Incorrect username or/and password."

def menu():
    print "Where do you want to go?"
    choice=int(raw_input("""
1. Human Resources
2. Marketing
3. Finance
4. Assembly
5. Canteen
6. Washroom
7. IT Dept.\nEnter a number corresponding to your choice"""))
    if choice==1:
        hr()
    elif choice==2:
        market()
    elif choice==3:
        finance()
    elif choice==4:
        assl()
    elif choice==5:
        cant()
    elif choice==6:
        wash()
    elif choice==7:
        it()
    else:
        print "Enter a valid choice!"
        menu()
        
def hr():
    def recr():
        print "You have entered recuitment."
    def empl():
        print "You have entered the employee welfare."
    def sal():
        print "You have entered the salary."
    def pf():
        print "You have entered the provident fund dept."
    def lab():
        print "You have entered labour laws."
    def admin():
        print "You have entered administrative office."
    def int_menu():
        print "Hi. You have entered Human Resources."
        choice=int(raw_input("""
Where in Human Resources do you want to go?

1. Recuitment
2. Employee Welfare
3. Salary
4. Provident Fund Dept.
5. Labour Laws
6. Administrative Office
OR
7. ACCESS DATABASE
"""))
        if choice==1:
            recr()
        elif choice==2:
            empl()
        elif choice==3:
            sal()
        elif choice==4:
            pf()
        elif choice==5:
            lab()
        elif choice==6:
            admin()
        elif choice==7:
            print "This is a WIP."
        else:
            print "Please enter a valid option."
            int_menu()
    int_menu()
            
def market():
    def prod():
        print "You have entered product identification."
    def mark_req():
        print "You have entered market requirements."
    def mark_loc():
        print "You have entered market location."
    def mark_cat():
        print "You have entered category of market."
    def int_menu():
        choice=int(raw_input("""
Where in Marketing do you want to go?

1. Product Identification
2. Market Requirements
3. Category of Market
4. Category of Market
"""))
        if choice==1:
            prod()
        elif choice==2:
            mark_req()
        elif choice==3:
            mark_loc()
        elif choice==4:
            mark_cat()
        else:
            print "Please enter a valid option."
            int_menu()
    int_menu()
        
def finance():
    def cash():
        print "You have entered management of cash flow."
    def exp():
        print "You have entered management of expenses."
    def inc():
        print "You have entered management of income."
    def prof():
        print "You have entered management of profitablity."
    def int_menu():
        choice=int(raw_input("""
Where in Finance do you want to go?

1. Cash Flow
2. Expenses
3. Income
4. Profitability
"""))
        if choice==1:
            cash()
        elif choice==2:
            exp()
        elif choice==3:
            inc()
        elif choice==4:
            prof()
        else:
            print "Please enter a valid option."
            int_menu()
    int_menu()

def ass():
    def comp():
        print "You have entered management of components."
    def test():
        print "You have entered management of testing equipments."
    def assl():
        print "You have entered management of assembly lines."
    def int_menu():
        choice=int(raw_input("""
Where in Assembly do you want to go?

1. Components
2. Testing Equipments
3. Assembly Lines
"""))
        if choice==1:
            comp()
        elif choice==2:
            test()
        elif choice==3:
            assl()
        else:
            print "Please enter a valid option."
            int_menu()
    int_menu()

def cant():
    lonely()

def wash():
    lonely()

def it():
    def add():
        print "WIP 1"
    def remove():
        print "WIP 2"
    def view():
        print "WIP 3"
    def int_menu():
        choice=int(raw_input("""
What do you want to do?

1. Add a new user
2. Remove a user
3. Assembly Lines
"""))
        if choice==1:
            add()
        elif choice==2:
            remove()
        elif choice==3:
            view()
        else:
            print "Please enter a valid option."
            int_menu()
    int_menu()
