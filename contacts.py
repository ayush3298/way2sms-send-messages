#!/usr/bin/env python
import os
import sys
import getpass

Contact_file = "contact.txt"

def get_number():
    number = input("Enter Contact Mobile Number: ")
    if len(number) == 10:
        #print(len(number))
        return number
        
    else:
        print('digits in phone number is less then 10')
        get_number()


def add_contact():
    with open(Contact_file, "a") as f:
        print("Enter Contact Name: ")
        f.write(str(sys.stdin.readline().strip()) + ":")
        number = get_number()
        f.write(number + "\n")


def get_contact(name=None):
    while not check_contact():
        pass
    while True:
        with open(Contact_file, "r") as f:
            lines = [line.strip().split(":", 2) for line in f.readlines()]
        if name is not None:
            for name, mobile in lines:
                if name == name.strip():
                    return name, mobile
        print("Which contact do you want to send msg? (Type number)")
        for ind, (name, mobile) in enumerate(lines):
            print("%d: %s" % (ind + 1, name))
        #print("%d: %s" % (0, "add another contact."))
        print("%d: %s" % (-1, "delete all contact."))
        try:
            ind = input().split(',')
            print(ind)
            if len(ind) == 1:
                if int(ind[0]) == -1:
                    delete_contact()
                    check_contact()
                    continue
                if int(ind[0]) - 1 in list(range(len(lines))):
                    return lines[int(ind[0]) - 1]
            else:
                contact_list = list()
                for choice in ind:
                    choice = int(choice)
                    if choice - 1 in list(range(len(lines))):
                        contact_list.append(lines[choice - 1])
                return contact_list
                    
        except Exception as e :
            print(e)
            print("Wrong input. I need the number of contact to use.")


def check_contact():
    while True:
        if os.path.exists(Contact_file):
            with open(Contact_file, "r") as f:
                try:
                    name, mobile = f.readline().strip().split(":")
                    if len(name) < 1 or len(mobile) < 10:

                        print("Data in 'contact.txt' file is invalid. "
                              "We will delete it and try again.")

                        os.remove(Contact_file)
                    else:
                        return True
                except:
                    print("Your file is broken. We will delete it "
                          "and try again.")
                    os.remove(Contact_file)
        else:
            while True:
                add_contact()
                print("Do you want to add another contact? (y/n)")
                if "y" not in sys.stdin.readline():
                    break


def delete_contact():
    if os.path.exists(Contact_file):
        os.remove(Contact_file)



