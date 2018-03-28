#!/usr/bin/env python
import os
import sys
import getpass

Contact_file = "contact.txt"


def add_contact():
    with open(Contact_file, "a") as f:
        print("Enter Contact Name: ")
        f.write(str(sys.stdin.readline().strip()) + ":")
        number = input("Enter Contact Mobile Number: ")
        f.write(number + "\n")


def get_contact(name=None):
    while not check_contact():
        pass
    while True:
        with open(Contact_file, "r") as f:
            lines = [line.strip().split(":", 2) for line in f.readlines()]
        if name is not None:
            for name, mobile in lines:
                if name == username.strip():
                    return name, mobile
        print("Which contact do you want to send msg? (Type number)")
        for ind, (name, mobile) in enumerate(lines):
            print("%d: %s" % (ind + 1, name))
        print("%d: %s" % (0, "add another contact."))
        print("%d: %s" % (-1, "delete all contact."))
        try:
            ind = int(sys.stdin.readline())
            if ind == 0:
                add_contact()
                continue
            if ind == -1:
                delete_contact()
                check_contact()
                continue
            if ind - 1 in list(range(len(lines))):
                return lines[ind - 1]
        except:
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



