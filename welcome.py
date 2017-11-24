import pyttsx
from spy_details import spy
from datetime import datetime
from steganography.steganography import Steganography
from datetime import datetime

engine = pyttsx.init()

STATUS_MESSAGES = ['My name is Peter, Petty Peter', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

engine.say("WELCOME TO SPY CHAT....")
print'\t\t******************SPY CHAT******************'
print' \t\t =================WELCOME================='

friends = []

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

    return updated_status_message


def add_friend():
    new_friend = {'name': '', 'age': 0, 'rating': 0.0, 'is_online': False}
    new_friend['name'] = raw_input("Please add your friend's name:")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        # Add Friend
        friends.append(new_friend)
        print 'FRIEND ADDED'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)


def select_friend():
    friend_selected = None
    item_number = 0
    if len(friends) == 0:
        print'Sorry! No friends in the list....\nPlease add a friend.'
        return add_friend()
    else:
        for friend in friends:
            print '%s. %s aged %d with spy rating %f is online' % (
            item_number + 1, friend['name'].upper(), friend['age'], friend['rating'])
            item_number += 1
        choice = input("\nChoose friend from above list")
        if len(friends) >= choice:
            friend_selected = friends[choice - 1]
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
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[friend_choice]['chats'].append(new_chat)
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
    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend \n 3. Send secret message \n 4. Read secret message \n 5. Read Chats from a user \n 6. Exit \n Your choice please : "
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
            # Exit Application
            show_menu = False
        else:
            print 'INVALID CHOICE'


engine.say("WOULD YOU LIKE TO CONTINUE AS " + spy['name'] + " OR TO START AS A NEW USER?")
engine.runAndWait()
existing_spy = raw_input("WOULD YOU LIKE TO CONTINUE AS " + spy['salutation'] + ". " + spy['name'] + "? (Y/N)")

if existing_spy.upper() == 'Y':
    engine.say("You can proceed")
    engine.runAndWait()
    print'You can proceed'
    start_chat(spy['name'], spy['age'], spy['rating'])
elif existing_spy.upper() == 'N':
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
    engine.say("WHAT SHOULD I CALL YOU Ms. OR Mr.? ")
    engine.runAndWait()
    spy_salutation = raw_input("WHAT SHOULD I CALL YOU Ms. OR Mr.?")
    spy_salutation.capitalize()
    engine.say("MAY I KNOW YOUR GOOD NAME: ")
    engine.runAndWait()
    spy_name = raw_input("MAY I KNOW YOUR GOOD NAME: ")
    if (len(spy_name) > 0) and (spy_name.isalnum()):
        spy_name.capitalize()
        engine.say("Alright," + spy_name + "! May I know more about you")
        engine.runAndWait()
        spy_response = raw_input("Alright, " + spy_salutation + " " + spy_name + "! May I know more about you (Y/N): ")
        if spy_response.upper() == 'Y':
            engine.say('Please tell me your age')
            engine.runAndWait()
            spy_age = input('Please tell me your age : ')
            if (spy_age > 12) and (spy_age < 50):
                engine.say('What is your spy rating?')
                engine.runAndWait()
                spy_rating = input("What is your spy rating (0 to 5)?")
                if (spy_rating > 4.5):
                    engine.say('Great ace!')
                    print 'Great ace!'
                elif (spy_rating > 3.5) and (spy_rating <= 4.5):
                    engine.say('You are one of the good ones.')
                    print 'You are one of the good ones.'
                elif (2.5 <= spy_rating <= 3.5):
                    engine.say('You can always do better')
                    print 'You can always do better'
                else:
                    engine.say('We can always use somebody to help in the office.')
                    print 'We can always use somebody to help in the office.'
                engine.runAndWait()
            else:
                engine.say("Sorry! you are not of appropriate age to be a spy.")
                engine.runAndWait()
                print("Sorry! you are not of appropriate age to be a Spy.")
            spy_is_online = True
            print("Authentication is complete.\nSpy " + spy_salutation + " " + spy_name + " \nSpy Age:{}".format(
                spy_age) + "\nSpy Rating:" + format(spy_rating) + " \n We are proud to have you on board!")
        elif spy_response.upper() == 'N':
            engine.say("You can proceed.")
            engine.runAndWait()
            print("You can proceed.")
        else:
            engine.say("Invalid choice!")
            engine.runAndWait()
            print("Invalid choice!")
    else:
        engine.say("Sorry! Invalid name")
        engine.runAndWait()
        print("Sorry! Invalid name")
    start_chat(spy_name, spy_age, spy_rating)
else:
    engine.say('SORRY! INVALID CHOICE...PLEASE RETRY')
    engine.runAndWait()
    print('SORRY! INVALID CHOICE...PLEASE RETRY')
