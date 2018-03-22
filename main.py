import sys
import default

print("Welcome to SpyChat program")
STATUS_MESSAGE=[]
def add_status(current_status_message):
    if (current_status_message != None):
        print("Your Current status is:" + current_status_message)
    else:
        print("You don't have any status message")

    update_choice = input("Do You want to select from older status (Y/N)?:")
    if update_choice.upper()=='N':
        new_status_message= input("Enter a new status message: ")

        if len(new_status_message) > 0:
            updated_status_message=new_status_message
            STATUS_MESSAGE.append(updated_status_message)
    elif update_choice.upper()=='Y':

        for i in range(len(STATUS_MESSAGE)):
            print(str(i+1) + " " + STATUS_MESSAGE[i])

        message_selection = int(input("choose from older message: "))
        if len(STATUS_MESSAGE) > message_selection
        updated_status_message=STATUS_MESSAGE[message_selection-1]

    return updated_status_message

def start_chat(spy_name,spy_age,spy_rating)   :
        current_status_message=None
        show_menu=True

        while show_menu:
            print("Choose the option which you want to do")
            menu_choice=int(input("1.Add a Status update. \n 2.Close Application. \n"))
            if menu_choice==1:
                print("You have choosen to update a status")
                current_status_message=add_status(current_status_message)
            elif menu_choice==2:
                show_menu=False





choice=input("Enter 1 if you want to have default setting:-")
if choice == '1':

    spy_name = default.spy_name
    spy_salutation = default.spy_salutation
    spy_age = default.spy_age
    spy_rating = default.spy_rating

else:
#validating the name of the spy
 print("Name should be only in alphabets (A-Z) or (a-z)")
 spy_name = input("Enter Your Name:")
 if spy_name.isalpha()==False:
      print("Name is Invalid")
      print("Name should be only in alphabets (A-Z) or (a-z)")
      sys.exit(0)

 spy_salutation=input("Enter Your Salutation (Mr. or Mrs.):")

#validating the age of the spy
 spy_age=input("Enter Your age:")
 if int(spy_age) <= 12 or int(spy_age) >= 50:
   print ("Age is Invalid")
   sys.exit(0)


#Rating of the spy
 spy_rating = input("Enter Your rating (0-5): ")
 if float(spy_rating)>=6.0:
      print("Invalid Rating")
      sys.exit(0)


print("hello " + spy_salutation + spy_name)
print("Your age is :" + spy_age)
print("Your rating is :" + spy_rating)

start_chat(spy_name,spy_age,spy_rating)
