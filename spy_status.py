import sys
import spy_friend
from spy_details import SPY, ChatMessage
import csv

STATUS_MESSAGE = []

def add_status(current_status_message):
    if (current_status_message != None):
        print"Your Current status is:" + current_status_message
    else:
        print"You don't have any status message"

    update_choice =raw_input("Do You want to select from older status (Y/N)?:")
    if update_choice.upper() == 'N':
        new_status_message = raw_input("Enter a new status message: ")
        #print a New Status
        print 'Your New Status=',new_status_message

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGE.append(updated_status_message)

    elif update_choice.upper()=='Y':
        for i in range(len(STATUS_MESSAGE)):
            print str(i+1) + " " + STATUS_MESSAGE[i]

        message_selection = int(raw_input("choose from older message: "))
        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection-1]
            #print the Older Status
            print 'Your Current Status=', updated_status_message

        return updated_status_message

def load_status():
    read_object = open("spy_status.csv",'r')
    reader = csv.reader(read_object)
    for row in reader:
        STATUS_MESSAGE.append(row[0])
    read_object.close()
    if len(STATUS_MESSAGE) > 0:
        return STATUS_MESSAGE[-1]
    else:
        return None
    read_object.close()    

def save_status():
    write_object = open('spy_status.csv','w')
    writer = csv.writer(write_object)
    for i in range(len(STATUS_MESSAGE)) :
        writer.writerow([STATUS_MESSAGE[i]])
    write_object.close()
