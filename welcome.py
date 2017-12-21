import pyttsx
from datetime import datetime
from steganography.steganography import Steganography
from datetime import datetime
from spy_login import login
import csv

engine = pyttsx.init()

STATUS_MESSAGES = ['My name is Peter, Petty Peter', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

class spy:
    def __init__(self,salutation,name,age,rating):
        self.salutation=salutation
        self.name=name
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status=None

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

Spy = spy('Mr','Peter',15,3.2)

friends = []

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
    elif default.upper() == 'Y':
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


def friend_list():
    with open('friend.csv','rb') as friend_data:
        read=csv.reader(friend_data)
        x=1
        for row in read:
            s=spy(row[0],row[1],row[2],row[3])
            friends.append(s)
            print str(x)+'. '+row[0]+'. '+row[1]
            x+=1

def add_friend():
    salutation = raw_input("Are they Mr. or Ms.?: ")
    salutation=salutation.capitalize()
    name = raw_input("Please add your friend's name:")
    name=name.capitalize()
    age = input("Age?")
    rating = input("Spy rating?")
    if 0<len(name)<30 and 12<age<50:
        # Add Friend
        new_friend = spy(salutation, name, age, rating)
        friends.append(new_friend)
        with open('friend.csv','ab') as friend_data:
            write = csv.writer(friend_data)
            write.writerow([salutation,name,age,rating,True])
            print 'FRIEND ADDED \n Friend List'
            friend_list()
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
        return add_friend()
    return len(friends)


def select_friend():
    friend_selected = None
    item_number = 0
    friend_list()
    if len(friends) == 0:
        print'Sorry! No friends in the list....\nPlease add a friend.'
        return add_friend()
    else:
        choice = input("\nChoose friend from above list")
        if len(friends) >= choice:
            friend_selected = choice-1
            return friend_selected
        else:
            print'Sorry! Invalid Choice. Please retry'
        return select_friend()


def send_message():
    friend_choice = select_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    chatobj = ChatMessage(text,True)
    friends[friend_choice].chats.append(chatobj)
    with open('chats.csv','ab') as chatdata:
        write = csv.writer(chatdata)
        write.writerow([Spy.name,friends[friend_choice].name,text,datetime.now(),True])
    print "Your secret message is ready!"

def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"
    print friends[sender].chats


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend \n 3. Send secret message \n 4. Read secret message \n 5. Read Chats from a user \n 6. Friend List \n 7. Exit \n Your choice please : "
        menu_choice = input(menu_choices)

        if (menu_choice == 1):
            # Add Status Update
            print'Add a status update'
            current_status_message = add_status(current_status_message)
        elif (menu_choice == 2):
            print'Add friend'
            add_friend()
        elif (menu_choice == 3):
            print'Send secret message'
            send_message()
        elif (menu_choice == 4):
            print'Read secret message'
            read_message()
        elif (menu_choice == 5):
            print'Read chats from a user'
        elif (menu_choice == 6):
            friend_list()
        elif(menu_choice == 7):
            # Exit Application
            show_menu = False
        else:
            print 'INVALID CHOICE'

engine.say("WOULD YOU LIKE TO CONTINUE AS " + Spy.name + " OR TO START AS A NEW USER?")
engine.runAndWait()
existing_spy = raw_input("WOULD YOU LIKE TO CONTINUE AS " + Spy.salutation + ". " + Spy.name + "? (Y/N)")

if existing_spy.upper() == 'Y':
    engine.say("You can proceed")
    engine.runAndWait()
    print'You can proceed'
    start_chat(Spy.name, Spy.age, Spy.rating)
else:
    login ()
    #start_chat(name,age,rating)
    #engine.say('SORRY! INVALID CHOICE...PLEASE RETRY')
    #engine.runAndWait()
    #print('SORRY! INVALID CHOICE...PLEASE RETRY')