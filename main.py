import sys
import default

choice=input("Enter 1 if you want to have default setting:-")
if choice == '1':

    spy_name = default.spy_name
    spy_salutation = default.spy_salutation
    spy_age = default.spy_age
    spy_rating = default.spy_rating

else:
#validating the name of the spy
 spy_name = input("Enter Your Name:")
 if spy_name.isalpha()==False:
      print("Name is Invalid")
      print("Name should be only in alphabets (A-Z) or (a-z)")
      sys.exit(0)

 spy_salutation=input("Enter Your Salutation (Mr. or Mrs.):")

#validating the age of the spy
 spy_age=input("Enter Your age:")
 if int(spy_age)<=12:
   print ("Age below 12")
   sys.exit(0)
 elif int(spy_age)>=50:
    print("Age above 50")
    sys.exit(0)

#Rating of the spy
 spy_rating=input("Enter Your rating:")
 if spy_rating == "A":
    print("You are a 3 star spy")
 elif spy_rating == "B":
    print("You are a 2 star spy")
 elif spy_rating == "C":
    print("You are a 1 star spy")
 else:
    print("You have entered incorrect rating")
    sys.exit(0)

print("hello " + spy_salutation + spy_name)
print("Your age is :" + spy_age)
print("Your rating is :" + spy_rating)
