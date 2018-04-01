import sys
from steganography.steganography import Steganography
from spy_details import SPY, ChatMessage
import csv

friends = []

def add_friend():
    friend_name = raw_input("What is Your friend's name?: ")
    friend_salutation = raw_input("salutation? (Mr. or Mrs.): ")
    friend_age = int(raw_input("Age?: "))
    friend_rating = float(raw_input("Rating (0-5)?: "))
    friend_is_online=True



    #validating the Name
    if friend_name.isalpha() == False:
        print "Name is Invalid"
        print "Name should be only in alphabets (A-Z) or (a-z)"
        sys.exit(0)

    #validating the age
    if friend_age <= 12 or friend_age >= 50:
        print "Age is Invalid"
        sys.exit(0)

    #validating the rating
    if friend_rating>=5.1:
        print "Invalid Rating"
        sys.exit(0)
    new_friend=SPY(friend_name, friend_salutation, friend_age, friend_rating, friend_is_online)
    friends.append(new_friend)

    print "Here is the updated list of friends"
    counter = 0
    for f in friends:
        counter +=1
        print "%d. %s"  %(counter, f.name)

def select_friend():

    #Printing all the friends of a User
    counter = 0
    for f in friends:
        counter +=1
        print "%d. %s"  %(counter, f.name)

    friend_choice = raw_input("Choose from your friend: ")
    friend_choice = int(friend_choice)
    friend_choice -=1
    #returning the index
    return friend_choice

def send_message():
    print "Choose the friend to whom you want to send the message"
    friend_choice = select_friend()

    original_image = raw_input("Enter the name of the image:")
    output_path = 'output.jpg'
    text = raw_input("Enter the message to be concealed")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)
    print "Your message has been sent to %s" %friends[friend_choice].name

def read_message():
    print "Choose the friend to whose message you want to read"
    sender = select_friend()

    if len(friends[sender].chats) == 0:
        print "You have no conversation with %s" %friends[sender].chats

    else:
        for i in range(len(friends[sender].chats)):
            print friends[sender].chats[i].message
    output_path = raw_input("What is the name of the file?")
    Secret_text =Steganography.decode(output_path)

    new_chat = ChatMessage(Secret_text, False)

    friends[sender].chats.append(new_chat)
    print "Your secret  message has been saved\n"
    print "Your message is '%s'" % Secret_text


def load_friend():
    read_object = open("friend.csv",'r')
    reader = csv.reader(read_object)
    for row in reader:
        # Order will be (name,salutation,age,rating)
        name = row[0]
        salutation = row[1]
        age =(row[2])
        rating = (row[3])
        is_online= (row[4])
        new_friend=SPY(name,salutation,age,rating,is_online)
        friends.append(new_friend)

    read_object.close()

def save_friend():
    write_object = open('friend.csv','w')
    writer = csv.writer(write_object)
    for i in range(len(friends)) :
        name = friends[i].name
        salutation = friends[i].salutation
        age = friends[i].age
        rating = friends[i].rating
        is_online = friends[i].is_online
        writer.writerow([name,salutation,age,rating,is_online])
    write_object.close()
