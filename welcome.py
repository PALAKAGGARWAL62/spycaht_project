import imghdr
import pyttsx
from datetime import datetime
from steganography.steganography import Steganography
from datetime import datetime
import csv
from passlib.hash import pbkdf2_sha256
from spy_details import spy, ChatMessage, Spy

engine = pyttsx.init()

friends = []

STATUS_MESSAGES = ['My name is Peter, Petty Peter', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

engine.say("WELCOME TO SPY CHAT....")
print'\t\t******************SPY CHAT******************'
print' \t\t =================WELCOME================='


def add_status(current_status_message):
    updated_status_message = None
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the existing status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
    elif default.upper () == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print str(item_position) + ". " + message
            item_position = item_position + 1
        message_selection = input("\nChoose from the above messages ")
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    else:
        print'invalid choice'
    return updated_status_message


def friend_list(sname):
    with open('friend.csv','rb') as friend_data:
        read=csv.reader(friend_data)
        x=1
        for row in read:
            if row[1]== sname:
                s=spy(row[0],row[2],row[3])
                friends.append(s)
                print str(x)+'. '+row[0]
                x+=1
        if x==0:
            print 'No Friends'


def add_friend(sname):
    salutation = raw_input("Are they Mr. or Ms.?: ")
    name = raw_input("Please add your friend's name:")
    name=salutation.capitalize()+' '+name.capitalize()
    age = input("Age?")
    rating = input("Spy rating?")
    x=0
    if 0<len(name)<30 and 12<age<50:
        # Add Friend
        try:
            with open('spy_list.csv','rb') as s1:
                read=csv.reader(s1)
                for r in read:
                    if r[0]==name and r[1]==str(age):
                        x+=1
                        new_friend = spy(name, age, rating)
                        friends.append(new_friend)
                        with open('friend.csv','ab') as friend_data:
                            write = csv.writer(friend_data)
                            write.writerow([name,sname,str(age),str(rating),True])
                            print 'FRIEND ADDED \n Friend List'
                            friend_list(sname)
                            engine.say('Friend Added')
                            engine.runAndWait()
                if x==0:
                    print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
                    return add_friend(sname)
                    engine.say('Sorry! Invalid entry. We can\'t add spy with the details you provided')
                    engine.runAndWait()
            return len(friends)
        except Exception as e:
            print e
            print 'exception in add friend'


def search_friend():
    f=True
    x=0
    while f:
        try:
            c = input('Search friend by\n 1. Name \n 2. Age \nEnter your choice: ')
            if c==1 :
                f=False
                s=raw_input('Are they Mr. or Ms.?:  ')
                n=raw_input('Enter your friend\'s name: ')
                n=s.capitalize()+" "+n.capitalize()
                with open ('spy_list.csv', 'rb') as spy:
                    r = csv.reader (spy)
                    for rr in r:
                        if rr[0]==n:
                            x += 1
                            print str(x)+'. Spy "'+rr[0]+'" Aged: '+rr[1]+' with spy rating '+rr[2]
                    if x==0 :
                        print 'NO spy '+n+' is there!'
            elif c==2:
                f=False
                a=raw_input('Enter Age: ')
                with open ('spy_list.csv', 'rb') as spy:
                    r = csv.reader (spy)
                    for rr in r:
                        if rr[1]==a:
                            x += 1
                            print str(x)+'. Spy "'+rr[0]+'" Aged: '+rr[1]+' with spy rating '+rr[2]
                    if x==0:
                        print 'NO spy aged '+a+' is there!'
            else:
                print 'Invalid choice!!!'
        except Exception as e:
            print 'Exception in search_friend'
            print e


def select_friend(sname):
    friend_selected = None
    item_number = 0
    friend_list(sname)
    f = True
    if len(friends) == 0:
        print'Sorry! No friends in the list....\nPlease add a friend.'
        engine.say('Sorry! No friends in the list. Please add a friend.')
        engine.runAndWait()
        return add_friend()
    else:
        while f:
            try:
                engine.say ('choose friend from above list')
                engine.runAndWait ()
                choice = input("\nChoose friend from above list")
                if len(friends) >= choice:
                    friend_selected = choice-1
                    return friend_selected
                else:
                    print'Sorry! Invalid Choice. Please retry'
                    engine.say('Sorry! Invalid Choice. Please retry')
                    engine.runAndWait()
                return select_friend(sname)
            except:
                print'exception in select friend'


def send_message(sname):
    flag=True
    friend_choice = select_friend(sname)
    while flag:
        original_image = raw_input("What is the name of the image?")
        I=imghdr.what(original_image)
        #print I
        if I=='png' or I=='gif' or I=='bmp' or I =='xbm' or I=='pgm' or I=='jpeg':
            output_path = 'output.'+I
            text = raw_input("What do you want to say?")
            Steganography.encode(original_image, output_path, text)
            chatobj = ChatMessage(text,True)
            with open ('chats.csv', 'ab') as chatdata:
                write = csv.writer (chatdata)
                write.writerow ([sname, friends[friend_choice].name, text, chatobj.time, True])
            print "Your secret message is ready!"
            flag = False
            friends[friend_choice].chats.append(chatobj)
        else:
            print 'Wrong file format'


def read_message(sname):
    sender = select_friend(sname)
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    cobj=ChatMessage(secret_text,False)
    friends[sender].chats.append(cobj)
    print "Your secret message has been saved!"
    print 'SENDER: '+friends[sender].name
    print 'RECEIVER: '+sname
    with open('chats.csv','rb') as chat_data:
        read=csv.reader(chat_data)
        x=0
        for row in read:
            if row[0]==friends[sender].name and row[1]==sname:
                print ' Message: "'+row[2]+'" \tsent on "'+row[3]+'"'
                x+=1
        if x==0:
            print 'No message'


def chat(sname):
    sender = select_friend (sname)
    x=0
    with open('chats.csv','rb') as chatting:
        read=csv.reader(chatting)
        for row in read:
            if row[0]==friends[sender].name and row[1]==sname:
                print ' Message by "'+friends[sender].name+ '"\n"' +row[2]+ '" \tsent on "'+row[3]+'"'
                x+=1
            elif row[0]==sname and row[1]==friends[sender].name:
                print ' Message by YOU \n"' + row[2] + '" \tsent on "' + row[3] + '"'
                x += 1
        if x==0:
            print 'No CHATS'


def login(name, password):
    c = 0
    with open ("spy_list.csv", "rb") as spy_data:
        read = csv.reader (spy_data)
        for row in read:
            if row[0] == name and pbkdf2_sha256.verify (password, row[4]):
                c += 1
                print 'Login Successfull'
                engine.say ('Login Successful')
                engine.runAndWait ()
                name = row[0]
                age = row[1]
                rating = row[2]
                Spy1 = spy (name, age, rating)
                start_chat (Spy1.name, Spy1.age, Spy1.rating)
                break;
        if c == 0:
            print'invalid name or password'


def new_user():
    age = 0
    rating = 0.0
    is_online = False
    f = True
    engine.say ('May I know your good name !')
    engine.runAndWait ()
    salutation = raw_input ('enter salutation: ')
    salutation = salutation.strip (' ')
    salutation = salutation.capitalize ()
    name = raw_input ('enter name: ')
    name = name.strip (' ')
    if len (name) > 0 and name.isalnum ():
        name = salutation + ' ' + name.capitalize ()
        engine.say ('How old are you?')
        engine.runAndWait ()
        try:
            age = input ('age: ')
            if (age > 12) and (age < 50):
                # age = str (age)
                engine.say ('Please, rate spy!')
                engine.runAndWait ()
                rating = input ("What is your spy rating (0 to 5)?")
                if 4.5 < rating <= 5:
                    print 'Great ace!'
                    engine.say ('Great ace!')
                elif (rating > 3.5) and (rating <= 4.5):
                    print 'You are one of the good ones.'
                    engine.say ('You are one of the good ones.')
                elif 2.5 <= rating <= 3.5:
                    print 'You can always do better'
                    engine.say ('You can always do better')
                else:
                    print 'We can always use somebody to help in the office.'
                    engine.say ('We can always use somebody to help in the office.')
                engine.runAndWait ()
                # rating = str(rating)
                spy_is_online = True
                engine.say ('Enter password please!')
                engine.runAndWait ()
                password = raw_input ('enter password')
                confirm_password = raw_input ('confirm password')
                if (password == confirm_password) and password.isalnum () and len (password) < 10:
                    password = pbkdf2_sha256.hash (password)
                else:
                    print'invalid password! password can only have numbers or alphabets'
                    engine.say ('invalid password! password can only have numbers or alphabets')
                    engine.runAndWait ()
                while f:
                    engine.say ('Email id please!')
                    engine.runAndWait ()
                    email = raw_input ("enter the email: ")
                    with open ('spy_list.csv', 'rb') as fd:
                        read = csv.reader (fd)
                        for row in read:
                            if email == row[5]:
                                print'Email Id already exist!!! Try new one'
                            else:
                                f = False
                print("Authentication is complete.\nSpy " + name + " \nSpy Age:" +
                      str (age) + "\nSpy Rating:" + str (rating) + " \n We are proud to have you on board!")
                engine.say ("Authentication is complete.Spy " + name + " Spy Age:" +
                            str (age) + " Spy Rating:" + str (rating) + " We are proud to have you on board!")
                engine.runAndWait ()
                print("You can proceed.")
                Spy2 = spy (name, age, rating)
                start_chat (Spy2.name, Spy2.age, Spy2.rating)
            else:
                print("Sorry! you are not of appropriate age to be a Spy.")
                engine.say ("Sorry! you are not of appropriate age to be a Spy.")
                engine.runAndWait ()
        except:
            print"Invalid age entry"
    else:
        print("Sorry! Invalid name")
        engine.say ("Sorry! Invalid name")
        engine.runAndWait ()

    with open ("spy_list.csv", "ab") as spy_data:
        write = csv.writer (spy_data)
        write.writerow ([name, str (age), str (rating), True, password, email])


def entry():
    flag = True
    while flag:
        try:
            engine.say ('Would you like to login or create a new user?')
            engine.runAndWait ()
            print '1. LOGIN \n2. SIGNUP AS NEW USER \n3. Exit'
            choice = input (" ENTER YOUR CHOICE ")
            if choice == 1:
                flag = False
                engine.say ('Your good name please')
                engine.runAndWait ()
                salutation = raw_input ('Enter Spy salutation: ')
                name = raw_input ('Enter Spy name: ')
                name = salutation.capitalize () + ' ' + name.capitalize ()
                engine.say ('Your password please!')
                engine.runAndWait ()
                password = raw_input ('Enter password: ')
                login (name, password)
            elif choice == 2:
                flag = False
                new_user ()
            elif choice == 3:
                # exit
                flag = False
            else:
                print'Invalid Choice'
                engine.say ('Invalid choice')
                engine.runAndWait ()
        except:
            print 'exception in user selection module'


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True

    while show_menu:
        menu_choice=0
        try:
            print "What do you want to do? \n 1. Add a status update\n 2. Add a friend \n 3. Send secret message \n 4. Read secret message \n 5. Read Chats from a user \n 6. Friend List \n 7. Search People \n 8. Logout \n 9. Exit \n Your choice please : "
            menu_choice = input()

            if (menu_choice == 1):
                # Add Status Update
                print'Add a status update'
                engine.say('Add a status update')
                engine.runAndWait()
                current_status_message = add_status(current_status_message)
            elif (menu_choice == 2):
                print'Add friend'
                engine.say ('Add friend')
                engine.runAndWait ()
                add_friend(spy_name)
            elif (menu_choice == 3):
                print'Send secret message'
                engine.say ('Send secret message')
                engine.runAndWait ()
                send_message(spy_name)
            elif (menu_choice == 4):
                print'Read secret message'
                engine.say ('Read secret message')
                engine.runAndWait ()
                read_message(spy_name)
            elif (menu_choice == 5):
                print'Read chats from a user'
                engine.say ('Read chat from a user')
                engine.runAndWait ()
                chat(spy_name)
            elif (menu_choice == 6):
                print'Friend list'
                engine.say ('friend list')
                engine.runAndWait ()
                friend_list(spy_name)
            elif(menu_choice == 7):
                engine.say('SEARCH PEOPLE')
                engine.runAndWait()
                search_friend()
            elif(menu_choice == 8):
                print 'You are logged out'
                show_menu = False
                entry()
            elif(menu_choice == 9):
                # Exit Application
                show_menu = False
            else:
                print 'INVALID CHOICE'
                engine.say ('invalid choice')
                engine.runAndWait ()
        except Exception as e:
            print 'exception in start chat'
            print e


engine.say("WOULD YOU LIKE TO CONTINUE AS " + Spy.name + " OR TO START AS A NEW USER?")
engine.runAndWait()
existing_spy = raw_input("WOULD YOU LIKE TO CONTINUE AS " + Spy.name + "? (Y/N)")

if existing_spy.upper() == 'Y':
    engine.say("You can proceed")
    engine.runAndWait()
    print'You can proceed'
    start_chat(Spy.name, Spy.age, Spy.rating)

elif existing_spy.upper() == 'N':
    entry()

else:
    print 'Invalid Choice'
    engine.say('Invalid choice')
    engine.runAndWait()