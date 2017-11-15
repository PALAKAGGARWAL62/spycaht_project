import pyttsx
import sys
from spy_details import spy_name,spy_age,spy_rating,spy_salutation

engine = pyttsx.init()

engine.say("WELCOME TO SPY CHAT....")
print'\t\t******************SPY CHAT******************'
print' \t\t =================WELCOME================='

def start_chat(spy_name,spy_age, spy_rating):
    menu_choices = "What do you want to do? \n 1. Add a status update\n 2. \n 3. \n 4. \n 5. \n 6. Exit \n Your choice please : "
    menu_choice = input(menu_choices)
    if (menu_choice == 1):
        # Add Status Update
        print'UPDATE STATUS'
    elif(menu_choice == 6):
        # Exit Application
        sys.exit()
    else:
        print 'INVALID CHOICE'
    while(menu_choice!=6):
        start_chat(spy_name,spy_age,spy_rating)

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

