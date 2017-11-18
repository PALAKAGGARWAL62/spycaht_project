import pyttsx
from spy_details import spy_name,spy_age,spy_rating,spy_salutation

engine = pyttsx.init()

STATUS_MESSAGES = ['My name is Peter, Petty Peter', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []

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
            print item_position + ". " + message
            item_position = item_position + 1
        message_selection = input("\nChoose from the above messages ")
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    return updated_status_message

def add_friend():

    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = input("Age?")
    new_rating = input("Spy rating?")

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        # Add Friend
        print 'add friend'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)

def start_chat(spy_name,spy_age, spy_rating):

    current_status_message = None
    show_menu=True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend \n 3. Send secret message \n 4. Read secret message \n 5. Read Chats from a user \n 6. Exit \n Your choice please : "
        menu_choice = input(menu_choices)

        if (menu_choice == 1):
            # Add Status Update
            print'UPDATE STATUS'
            current_status_message=add_status(current_status_message)
        elif(menu_choice == 6):
            # Exit Application
            show_menu=False
        else:
            print 'INVALID CHOICE'

engine.say("WOULD YOU LIKE TO CONTINUE AS " + spy_name + " OR TO START AS A NEW USER?")
engine.runAndWait()
existing_spy = raw_input("WOULD YOU LIKE TO CONTINUE AS " + spy_name + " OR WANT TO START AS A NEW USER? (Y/N)")

if existing_spy.upper()=='Y':
    engine.say("You can proceed")
    engine.runAndWait()
    print'You can proceed'
    start_chat(spy_name, spy_age, spy_rating)
elif existing_spy.upper()=='N':
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
            print("Authentication is complete.\nSpy " + spy_salutation + " " + spy_name + " \nSpy Age:{}".format(spy_age) + "\nSpy Rating:" + format(spy_rating) + " \n We are proud to have you on board!")
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

