import sys
import spy_friend
import spy_status
from spy_details import SPY

print "Welcome to SpyChat program"

#Module 1:
# Creating User Profile
print "Let's First Create Your Profile\n"
profile_choice = raw_input("Do You want to Continue with the current setting? (y/n)")

if profile_choice.upper() == 'Y':
    spy = SPY("Abhishek", "Mr.", 21, 4.8,True)
else:
     #validating the Name of the spy
     name = raw_input("Enter Your Name:")
     if spy['name'].isalpha()==False:
          print "Name is Invalid"
          print "Name should be only in alphabets (A-Z) or (a-z)"
          sys.exit(0)

     salutation = raw_input("Enter Your Salutation (Mr. or Mrs.):")

    #validating the age of the spy
     age=int(raw_input("Enter Your age:"))
     if spy['age'] <= 12 or spy['age'] >= 50:
            print "Age is Invalid"
            sys.exit(0)


    #validating the Rating of the spy
     rating = float(raw_input("Enter Your rating (0-5): "))
     if  spy['rating']>=5.1:
          print "Invalid Rating"
          sys.exit(0)

     SPY = SPY(name, salutation, age, rating)


print "Hello %s %s" %( spy.salutation, spy.name)
print "We have SUCCESSFULLY Create Your Account"

# Module 2:
# Creating a Menu
def start_chat()   :
        
        show_menu=True

        while show_menu:
            print "1.Add Status  \n 2.Add Friend\n 3. Send Secret Message\n 4. Read Secret Message\n 5.Close Application.\n"
            menu_choice=raw_input("What do You want to do: ")

            if menu_choice=='1':
                # update the status
                print "You have chosen to update a status"
                spy.current_status_message = spy_status.add_status(spy.current_status_message)
            elif menu_choice =='2':
                # Add Friend
                print "You have chosen to add a Friend"
                spy_friend.add_friend()
            elif menu_choice == '3':
                # Send a secret message
                print "\n You Have Chosen to send a secret message to a friend"
                spy_friend.send_message()
            elif menu_choice == '4':
                # Read a secret message
                print "\n You Have Chosen to read a secret message of a friend"
                spy_friend.read_message()
            elif menu_choice=='5':
                show_menu=False
            else:
                print "\nIncorrect Choice"
spy_friend.load_friend()
start_chat()
spy_friend.save_friend()
spy.current_status_message= spy_status.load_status()
spy_status.save_status()
