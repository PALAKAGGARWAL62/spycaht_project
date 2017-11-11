import pyttsx

engine = pyttsx.init()

engine.say("WELCOME TO SPY CHAT....")
print'\t\t******************SPY CHAT******************'
print' \t\t =================WELCOME================='

engine.say("WHAT SHOULD I CALL YOU Ms. OR Mr.? ")
engine.runAndWait()
spy_salutation = raw_input("WHAT SHOULD I CALL YOU Ms. OR Mr.?")
spy_salutation.capitalize()
spy_salutation = spy_salutation + "."

spy_age = 0
spy_rating = 0.0
spy_is_online = False

engine.say("MAY I KNOW YOUR GOOD NAME: ")
engine.runAndWait()
spy_name = raw_input("MAY I KNOW YOUR GOOD NAME: ")

if (len(spy_name) > 0) and (spy_name.isalnum()):
    spy_name.capitalize()
    engine.say("Alright," + spy_name + "! May I know more about you")
    engine.runAndWait()
    spy_response = raw_input("Alright, " + spy_salutation + " " + spy_name + "! May I know more about you (Y/N): ")
    if spy_response is ('y'or'Y'):
        engine.say('Please tell me your age')
        engine.runAndWait()
        spy_age=input('Please tell me your age : ')
        if (spy_age > 12) and (spy_age < 50):
            engine.say('What is your spy rating?')
            engine.runAndWait()
            spy_rating =input("What is your spy rating (0 to 5)?")
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
        print("Authentication is complete.\nSpy " + spy_salutation + " " + spy_name + " \nSpy Age:" + format(
            spy_age) + "\nSpy Rating:" + format(spy_rating))
    elif spy_response is ('n')or('N'):
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

