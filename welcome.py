# to use csv
import csv

# to check image extension
import imghdr

# to implement text to speech
import pyttsx

# to encode and decode password
from passlib.hash import pbkdf2_sha256

# to implement hiding text in image
from steganography.steganography import Steganography

# to import elements of other class
from spy_details import spy, ChatMessage, Spy

# for live chat
import socket

# activate voice engine
engine = pyttsx.init ()

# list holding friends details
friends = []

# pre stored status message list
STATUS_MESSAGES = ['My name is Peter, Petty Peter', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

# assigning text to voice engine to covert it to speech
engine.say ("WELCOME TO SPY CHAT....")

print'\t\t******************SPY CHAT******************'
print' \t\t =================WELCOME================='

engine.say ("WOULD YOU LIKE TO CONTINUE AS " + Spy.name + " OR TO START AS A NEW USER?")
# executing text to speech engine
engine.runAndWait ()
existing_spy = raw_input ("WOULD YOU LIKE TO CONTINUE AS " + Spy.name + "? (Y/N)")


# function to add status
def add_status(current_status_message):
    updated_status_message = None
    if current_status_message is not None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input ("Do you want to select from the existing status (y/n)? ")

    if default.lower () == "n":  # setting your own status not pre stored , lower will convert 'N' to 'n'
        new_status_message = raw_input ("What status message do you want to set?")
        if len (new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append (updated_status_message)
    elif default.upper () == "Y":  # setting any status from pre stored
        item_position = 1
        for message in STATUS_MESSAGES:
            print str (item_position) + ". " + message
            item_position = item_position + 1
        message_selection = input ("\nChoose from the above messages ")
        if len (STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    else:
        print'invalid choice'
    return updated_status_message


# function to load friend list of a spy
def friend_list(sname):
    with open ('friend.csv', 'rb') as friend_data:
        read = csv.reader (friend_data)
        x = 1
        for row in read:
            if row[1] == sname:
                s = spy (row[0], row[2], row[3])
                friends.append (s)
                print str (x) + '. ' + row[0]
                x += 1
        if x == 0:
            print 'No Friends'


# function to add friends
def add_friend(sname):
    salutation = raw_input ("Are they Mr. or Ms.?: ")
    name = raw_input ("Please add your friend's name:")
    name = salutation.capitalize () + ' ' + name.capitalize ()
    age = input ("Age?")
    rating = input ("Spy rating?")
    x = 0
    # Add Friend here we don't need any constraints as they are already applied while adding a user
    try:
        with open ('spy_list.csv', 'rb') as s1:
            read = csv.reader (s1)
            for r in read:
                if r[0] == name and r[1] == str (age):
                    x += 1
                    new_friend = spy (name, age, rating)
                    friends.append (new_friend)
                    with open ('friend.csv', 'ab') as friend_data:
                        write = csv.writer (friend_data)
                        write.writerow ([name, sname, str (age), str (rating), True])
                        print 'FRIEND ADDED \n Friend List'
                        friend_list (sname)
                        engine.say ('Friend Added')
                        engine.runAndWait ()
            if x == 0:
                print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
                return add_friend (sname)
                engine.say ('Sorry! Invalid entry. We can\'t add spy with the details you provided')
                engine.runAndWait ()
            return len (friends)
    except Exception as e:
        print e
        print 'exception in add friend'


# function to search friend
def search_friend():
    f = True
    x = 0
    while f:
        try:
            c = input ('Search friend by\n 1. Name \n 2. Age \nEnter your choice: ')
            if c == 1:
                f = False
                s = raw_input ('Are they Mr. or Ms.?:  ')
                n = raw_input ('Enter your friend\'s name: ')
                n = s.capitalize () + " " + n.capitalize ()
                with open ('spy_list.csv', 'rb') as spy:
                    r = csv.reader (spy)
                    for rr in r:
                        if rr[0] == n:
                            x += 1
                            print str (x) + '. Spy "' + rr[0] + '" Aged: ' + rr[1] + ' with spy rating ' + rr[2]
                    if x == 0:
                        print 'NO spy ' + n + ' is there!'
            elif c == 2:
                f = False
                a = raw_input ('Enter Age: ')
                with open ('spy_list.csv', 'rb') as spy:
                    r = csv.reader (spy)
                    for rr in r:
                        if rr[1] == a:
                            x += 1
                            print str (x) + '. Spy "' + rr[0] + '" Aged: ' + rr[1] + ' with spy rating ' + rr[2]
                    if x == 0:
                        print 'NO spy aged ' + a + ' is there!'
            else:
                print 'Invalid choice!!!'
        except Exception as e:
            print 'Exception in search_friend'
            print e


# function of friend selection
def select_friend(sname):
    friend_selected = None
    item_number = 0
    friend_list (sname)
    f = True
    if len (friends) == 0:
        print'Sorry! No friends in the list....\nPlease add a friend.'
        engine.say ('Sorry! No friends in the list. Please add a friend.')
        engine.runAndWait ()
        return add_friend ()
    else:
        while f:
            try:
                engine.say ('choose friend from above list')
                engine.runAndWait ()
                choice = input ("\nChoose friend from above list")
                if len (friends) >= choice:
                    friend_selected = choice - 1
                    return friend_selected
                else:
                    print'Sorry! Invalid Choice. Please retry'
                    engine.say ('Sorry! Invalid Choice. Please retry')
                    engine.runAndWait ()
                return select_friend (sname)
            except Exception as e:
                print e
                print'exception in select friend'


# function to send message by encoding it word by word to different images
def send_message(sname):  # sending message hidden in image
    flag = True
    friend_choice = select_friend (sname)
    while flag:
        try:
            text = raw_input ("What do you want to say?")
            text = text.strip (' ')
            text = text.split (' ')  # splitting text in word
            x = 1
            if len (text) > 0:
                # encoding text word by word in image
                for word in text:
                    # path of image
                    original_image = raw_input ("What is the name of the image?")
                    # checking image format
                    image_format = imghdr.what (original_image)
                    if image_format == 'png' or image_format == 'gif' or image_format == 'bmp' or image_format == 'xbm'\
                            or image_format == 'pgm' or image_format == 'jpeg':
                        output_path = 'output' + str (x) + '.' + image_format
                        Steganography.encode (original_image, output_path, word)
                        x += 1
                        chat_obj = ChatMessage (word, True)
                        # writing message to csv
                        try:
                            with open ('chats.csv', 'ab') as chat_data:
                                write = csv.writer (chat_data)
                                write.writerow ([sname, friends[friend_choice].name, word, chat_obj.time, True])
                                print "Your secret message is ready!"
                                flag = False
                                friends[friend_choice].chats.append (chat_obj)
                        except Exception as e:
                            print e
                            print 'exception in writing text to file'
                    else:
                        print 'Wrong file format'
        except Exception as e:
            print e
            print 'exception in sending message'


# function to read messages by particular friend
def read_message(sname):
    sender = select_friend (sname)
    message = ''
    n = input('Enter the Number of images')
    try:
        for x in range (n):
            output_path = raw_input ("What is the name of the file?")
            secret_text = Steganography.decode (output_path)  # decoding text hidden in image
            message += secret_text + ' '
        chat_obj = ChatMessage (message, False)
        friends[sender].chats.append (chat_obj)
        print message
    except Exception as e:
        print e
        print 'exception in decoding message'


# function to read complete chat from a particular friend
def chat(spy_name):
    sender = select_friend (spy_name)
    x = 0
    with open ('chats.csv', 'rb') as chatting:  # opening chats to to read chat
        read = csv.reader (chatting)
        for row in read:
            # comparing sender and receiver name to view message from friend
            if row[0] == friends[sender].name and row[1] == spy_name:
                print ' Message by "' + friends[sender].name + '"\n"' + row[2] + '" \tsent on "' + row[3] + '"'
                x += 1
            # checking your own message
            elif row[0] == spy_name and row[1] == friends[sender].name:
                print ' Message by YOU \n"' + row[2] + '" \tsent on "' + row[3] + '"'
                x += 1
        if x == 0:
            print 'No CHATS'


# function to implement live chat with online users using socket programming
def live_chat(sname):
    try:
        s = socket.socket ()
        port = 12222
        ip = '127.0.0.1'
        c = input ('PRESS \n 1. SERVER\n 2. CLIENT')
        if c == 1:
            s.bind ((ip, port))
            s.listen (5)
            cname = raw_input ('Enter friend name: ')
            c = None
            while True:
                if c is None:
                    print'waiting for friends...'
                    c, addr = s.accept ()
                else:
                    print 'Response...'
                    print c.recv (1025)
                    q = raw_input ('type msg here: ')
                    c.send (q)
                    chat_obj = ChatMessage (q, True)
                    try:
                        with open ('chats.csv', 'ab') as chat_data:
                            write = csv.writer (chat_data)
                            write.writerow ([sname, cname, q, chat_obj.time, True])
                            print "Your secret message is ready!"
                    except Exception as e:
                        print e
                        print 'exception in writing text to file'
            c.close ()
        if c == 2:
            s.connect ((ip, port))
            cname = raw_input ('Enter friend name: ')
            while True:
                z = raw_input ('Send Message :')
                s.send (z)
                chat_obj = ChatMessage (z, True)
                try:
                    with open ('chats.csv', 'ab') as chat_data:
                        write = csv.writer (chat_data)
                        write.writerow ([sname, cname, z, chat_obj.time, True])
                        print "Your secret message is ready!"
                except Exception as e:
                    print e
                    print 'exception in writing text to file'
                print('Response...')
                print s.recv (1025)
            s.close ()
    except Exception as e:
        print e


# function for login
def login(name, password):  # parameters taken are spy name and password
    c = 0
    try:
        # reading data from csv to check if user name and password is correct
        with open ("spy_list.csv", "rb") as spy_data:
            read = csv.reader (spy_data)
            for row in read:
                if row[0] == name and pbkdf2_sha256.verify (password, row[4]):  # verification of password
                    c += 1
                    print 'Login Successful'
                    engine.say ('Login Successful')
                    engine.runAndWait ()
                    # defining parameters for calling spy chat
                    name = row[0]
                    age = row[1]
                    rating = row[2]
                    spy_login = spy (name, age, rating)  # defining class object
                    start_chat (spy_login.name, spy_login.age, spy_login.rating)  # calling spy_chat
                    break
            if c == 0:
                print'invalid name or password'
    except Exception as e:
        print e
        print 'Exception in login'


# function for adding a new user to application
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
    if len (name) > 0 and name.isalnum ():  # constraints on name
        name = salutation + ' ' + name.capitalize ()  # combining name and salutation
        engine.say ('How old are you?')
        engine.runAndWait ()
        try:
            age = input ('age: ')
            if (age > 12) and (age < 50):  # constraints on age
                engine.say ('Please, rate spy!')
                engine.runAndWait ()
                rating = input ("What is your spy rating (0 to 5)?")

                # complementing spy according to rating
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
                spy_is_online = True

                engine.say ('Enter password please!')
                engine.runAndWait ()
                password = raw_input ('enter password')  # taking password
                confirm_password = raw_input ('confirm password')  # confirming password
                # constraints on password
                if (password == confirm_password) and password.isalnum () and len (password) < 10:
                    password = pbkdf2_sha256.hash (password)  # encoding password
                else:
                    print'invalid password! password can only have numbers or alphabets'
                    engine.say ('invalid password! password can only have numbers or alphabets')
                    engine.runAndWait ()
                while f:
                    engine.say ('Email id please!')
                    engine.runAndWait ()
                    # taken for confirming user identity if it already exists in the file
                    try:
                        email = raw_input ("enter the email: ")
                        with open ('spy_list.csv', 'rb') as fd:  # opening csv file in read mode
                            read = csv.reader (fd)
                            for row in read:
                                if email == row[5]:  # comparing email
                                    print'Email Id already exist!!! Try new one'
                                else:
                                    f = False
                    except Exception as e:
                        print e  # printing exception
                        print 'exception in email comparison'

                print("Authentication is complete.\nSpy " + name + " \nSpy Age:" +
                      str (age) + "\nSpy Rating:" + str (rating) + " \n We are proud to have you on board!")
                engine.say ("Authentication is complete.Spy " + name + " Spy Age:" +
                            str (age) + " Spy Rating:" + str (rating) + " We are proud to have you on board!")
                engine.runAndWait ()
                print("You can proceed.")
                spy_new = spy (name, age, rating)  # defining class object
                start_chat (spy_new.name, spy_new.age, spy_new.rating)
            else:
                print("Sorry! you are not of appropriate age to be a Spy.")
                engine.say ("Sorry! you are not of appropriate age to be a Spy.")
                engine.runAndWait ()
        except Exception as e:
            print e
            print "Invalid age entry"
    else:
        print("Sorry! Invalid name")
        engine.say ("Sorry! Invalid name")
        engine.runAndWait ()
    try:
        with open ("spy_list.csv", "ab") as spy_data:
            write = csv.writer (spy_data)
            write.writerow ([name, str (age), str (rating), True, password, email])
    except Exception as e:
        print e
        print 'exception in adding new spy'

    # function for selection of login or new user


# function for the selection of new user or login
def entry():
    flag = True
    while flag:  # setting flag for executing the body again and again
        try:  # exception handling: try block where exception can occur
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
                # logging in the existing spy
                login (name, password)

            elif choice == 2:
                flag = False
                # calling new user to add one more spy to application
                new_user ()

            elif choice == 3:
                # exit
                flag = False

            else:
                # choice other than required
                print'Invalid Choice'
                engine.say ('Invalid choice')
                engine.runAndWait ()

        except Exception as e:
            print 'exception in user selection module'
            print e


# function gives menu\ main operations of chat application
def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = 0
        try:
            print "What do you want to do? \n 1. Add a status update\n 2. Add a friend \n 3. Send secret message " \
                  "\n 4. Read secret message \n 5. Read chats from a user \n 6. Live chat \n 7. Friend list " \
                  "\n 8. Search People \n 9. Logout \n 10. Exit \n Your choice please : "
            menu_choice = input ()

            if menu_choice == 1:
                # Add Status Update
                print'Add a status update'
                engine.say ('Add a status update')
                engine.runAndWait ()
                current_status_message = add_status (current_status_message)

            elif menu_choice == 2:
                # Add Friend
                print'Add friend'
                engine.say ('Add friend')
                engine.runAndWait ()
                add_friend (spy_name)

            elif menu_choice == 3:
                # Send Message
                print'Send secret message'
                engine.say ('Send secret message')
                engine.runAndWait ()
                send_message (spy_name)

            elif menu_choice == 4:
                # Read message
                print'Read secret message'
                engine.say ('Read secret message')
                engine.runAndWait ()
                read_message (spy_name)

            elif menu_choice == 5:
                # Read chat
                print'Read chats from a friend'
                engine.say ('Read chat from a friend')
                engine.runAndWait ()
                chat (spy_name)

            elif menu_choice == 6:
                # Live chat
                print 'Live Chat'
                engine.say ('Live Chat')
                engine.runAndWait ()
                live_chat (spy_name)

            elif menu_choice == 7:
                # Knowing your friends
                print'Friend list'
                engine.say ('know your friends')
                engine.runAndWait ()
                friend_list (spy_name)
            elif menu_choice == 8:
                # Searching people
                print 'Search people'
                engine.say ('SEARCH PEOPLE')
                engine.runAndWait ()
                search_friend ()

            elif menu_choice == 9:
                # logout
                print 'You are logged out'
                show_menu = False
                entry ()

            elif menu_choice == 10:
                # Exit Application
                show_menu = False

            else:
                # any other entry than required
                print 'INVALID CHOICE'
                engine.say ('invalid choice')
                engine.runAndWait ()

        except Exception as e:
            print 'exception in start chat'
            print e


if existing_spy.upper () == 'Y':  # upper will convert even 'y' to 'Y'
    engine.say ("You can proceed")
    engine.runAndWait ()
    print'You can proceed'
    start_chat (Spy.name, Spy.age, Spy.rating)  # calling spy for peter

elif existing_spy.upper () == 'N':
    entry ()  # selection for login or new user

else:
    print 'Invalid Choice'
    engine.say ('Invalid choice')
    engine.runAndWait ()


