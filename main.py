import sys
import default
import spy_friend
import spy_status




def start_chat(spy_name,spy_age,spy_rating)   :
        current_status_message=None
        show_menu=True

        while show_menu:
            menu_choice=int(input("1.Add a Status update. \n 2.Add Friend\n 3.Close Application. \n"))
            if menu_choice==1:
                print("You have chosen to update a status")
                current_status_message=spy_status.add_status(current_status_message)
            elif menu_choice ==2:
                print("You have chosen to add a Friend")
                spy_friend.add_friend()
            elif menu_choice==3:
                show_menu=False

print("Welcome to SpyChat program")
choice=input("Do You want to proceed with default setting(y/n)?: ")

spy = {
        'name' : '',
        'salutation' : '',
        'age' : 0,
        'rating' : 0.0,
        'is_online' : True
    }
if choice.upper() == 'Y':

    spy['name'] = default.spy['name']
    spy['salutation'] = default.spy['salutation']
    spy['age'] = default.spy['age']
    spy['rating'] = default.spy['rating']
    #spy['is_online'] = default.spy['is_online']

elif choice.upper() == 'N':
#validating the name of the spy

 spy['name'] = input("Enter Your Name:")
 if spy['name'].isalpha()==False:
      print("Name is Invalid")
      print("Name should be only in alphabets (A-Z) or (a-z)")
      sys.exit(0)

 spy['salutation'] = input("Enter Your Salutation (Mr. or Mrs.):")

#validating the age of the spy
 spy['age']=int(input("Enter Your age:"))
 if spy['age'] <= 12 or spy['age'] >= 50:
        print ("Age is Invalid")
        sys.exit(0)


#Rating of the spy
 spy['rating'] = float(input("Enter Your rating (0-5): "))
 if  spy['rating']>=5.1:
      print("Invalid Rating")
      sys.exit(0)

 spy['is_online']=True

else:
    sys.exit(0)

print("hello " + spy['salutation'] + spy['name'])
print("Your age is %d:"  % (spy['age']))
print("Your rating is %f:"  % (spy['rating']))
#print("You are Online" + spy["is_online"])

start_chat(spy['name'],spy['age'],spy['rating'])
