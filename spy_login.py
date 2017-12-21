import csv
from passlib.hash import pbkdf2_sha256
class spy_add:
    def new_user(self):
        age = 0
        rating = 0.0
        is_online = False


        salutation = raw_input ('enter salutation: ')
        salutation = salutation.capitalize()
        name = raw_input('enter name: ')
        name = name.strip(' ')
        if len(name) > 0 and name.isalnum():
            name=salutation +' '+ name.capitalize()
            age = input('age: ')
            if (age > 12) and (age < 50):
                age=str(age)
                rating = input("What is your spy rating (0 to 5)?")
                if(rating > 4.5):
                    print 'Great ace!'
                elif(rating > 3.5) and (rating <= 4.5):
                    print 'You are one of the good ones.'
                elif(2.5 <= rating <= 3.5):
                    print 'You can always do better'
                else:
                    print 'We can always use somebody to help in the office.'
                rating=str(rating)
                spy_is_online = True
                password = raw_input ('enter password')
                confirm_password = raw_input ('confirm password')
                if (password == confirm_password) and password.isalnum () and len (password) < 10:
                    password = pbkdf2_sha256.hash (password)
                else:
                    print'invalid password! password can only have numbers or alphabets'
                email = raw_input ("enter the email: ")
                # check email already exist left
            else:
                print("Sorry! you are not of appropriate age to be a Spy.")

            print("Authentication is complete.\nSpy " + salutation + " " + name + " \nSpy Age:"+
                age + "\nSpy Rating:" + rating + " \n We are proud to have you on board!")
            print("You can proceed.")
        else:
            print("Sorry! Invalid name")
        with open("spy_list.csv", "ab") as spy_data:
            write = csv.writer(spy_data)
            write.writerow([name,age,rating,True,password,email])

    def login(self):
        salutation = raw_input('Enter Spy salutation: ')
        name=raw_input('Enter Spy name: ')
        name=salutation.capitalize()+' '+name.capitalize()
        password = raw_input('Enter password: ')
        c=0
        with open ("spy_list.csv", "rb") as spy_data:
            read = csv.reader(spy_data)
            for row in read:
                if row[0]==name and pbkdf2_sha256.verify(password,row[4]):
                    c+=1
                    print 'login successfull'
                    name=row[0]
                    age = row[1]
                    rating=row[2]
                    break;
            if c==0:
                print'invalid name or password'
def login():
    print '1. LOGIN \n2. SIGNUP AS NEW USER'
    choice = input(" ENTER YOUR CHOICE ")
    s=spy_add()
    if choice == 1:
        s.login()
    elif choice == 2:
        s.new_user()
