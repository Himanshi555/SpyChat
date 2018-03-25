friends = []

def add_friend():
    new_friend = {
        'name' : "",
        'salutation' : "",
        'age' : 0,
        'rating' : 0.0,
        'is_online' : True
    }
    new_friend['name'] = input("Enter Your name: ")
    new_friend['salutation'] = input("Should we call You Mr. or Mrs.?: ")
    new_friend['salutation'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = int(input("What is Your age: "))
    new_friend['rating'] = float(input("Enter Your rating (0-5): "))


    if new_friend['name'].isalpha() == False:
        print("Name is Invalid")
        print("Name should be only in alphabets (A-Z) or (a-z)")
        sys.exit(0)

    if new_friend['age'] <= 12 or new_friend['age'] >= 50:
        print ("Age is Invalid")
        sys.exit(0)

    if new_friend['rating']>=5.1:
        print("Invalid Rating")
        sys.exit(0)

    friends.append(new_friend)
