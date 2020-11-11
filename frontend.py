# Ticket Manager Front end, this is the part of the code that the user directly interacts with (presumably) Here the
# user can signup, login, and manage all of their tickets. Users can also buy tickets, add points, and view their
# tickets. Please make sure you view the README either in the provided documentation or view our github repo
# https://github.com/SeamusRW/CYBR3108-Project-TicketManager-Group4
# Authors: Roydon D'souza, John Walker
# V 3.0
# Date : 11/11/2020

try:
    import gloves as glove
    import time as t
    import socket
except:
    print("Unable to import required modules")
    print("Please refer to the README and ensure that all requirements are met")
    exit(0)

try:
    import colorama
    from colorama import init
    from colorama import Fore, Back, Style

    init()
except:
    print("Unable to import colorama")
    print("Entering boring mode")


# Main function
def main():
    intro()
    ui = ""

    # Initial Login Screen
    print("\n____________________")
    while ui != "quit" or ui != "3":
        print("\n1: Login\n2: Signup\n3: Quit")
        print("____________________\n")

        t.sleep(0.2)

        ui = input(": ")

        # Login option
        if ui == "1" or ui == "login":
            print("\n<<Login>>")
            print("____________________")
            t.sleep(0.2)
            try:
                username = input("\nPlease enter Username: ")
                password = input("Please enter Password: ")
            except TypeError:
                print("Invalid Credentials")
            else:
                if glove.login(username, password):  # calls login function, if user is not logged in, and username
                    # and password are valid, then user gains access
                    application(username, password)  # passes username and password to application, runs application
                else:
                    print("Unable to login, Please check login information")

        # Signup option
        if ui == "2" or ui == "signup":
            print("\n<<Signup>>")
            print("____________________")
            t.sleep(0.2)
            while True:
                # password requirements
                print("\n<<Password Requirements:")
                print("* Must be at least 8 characters long"
                      "\n* Must have one number \n* Must have one lowercase letter"
                      "\n* Must have one uppercase letter  \n* Must have one special character(@$_)")
                t.sleep(0.2)
                try:
                    username = input("\nPlease enter Username: ").strip()
                except TypeError:
                    print("Invalid type")
                else:
                    if glove.checkUser(username):  # checks to see if username is taken
                        print("Username Taken, please try again")
                    else:
                        try:
                            password = input("Please enter Password: ")
                        except TypeError:
                            print("Invalid Type")
                        else:
                            if glove.valPass(password):  # checks to see if password is valid
                                verify = input("Please verify Password: ")
                                if verify == password:  # verify entered password
                                    fname = input("Please enter first name: ")
                                    lname = input("Please enter last name: ")

                                    glove.signup(username, password, fname, lname)  # signup user with provided
                                    # information
                                    break
                                else:
                                    print("\nPasswords do not match, please try again")
                            else:
                                print("Password does not meet requirements please try again")

        if ui == "3" or ui == "quit":
            print("Goodbye")
            exit(1)


# once user is validated and, they are able to log in
def application(username, password):
    ui = ""
    tickets = [["Metallica", 250], ["Lady Gaga", 250], ["Keith Urban", 250]]  # available tickets
    if glove.loggedIN:
        print('''
        | Welcome to Ticket Manager ''' + username + ''' |
        ''')

        # main loop
        while ui != "4" or "signout":
            print("1: Buy Tickets \n2: View Owned Tickets \n3: Add Points \n4: Signout")
            points = glove.getpointamnt(username)  # gets points from sql
            print("points: ", points)
            ui = input(": ")

            if ui == "1":  # buy tickets
                while ui != "b" or "B":
                    print("<<Buy Tickets>>")
                    print("Points: ", points)
                    print("NOTE: Users may only have one of each ticket due to current COVID guidelines\n NO REFUNDS!!")
                    print("Available tickets: \n")
                    for ticket in tickets:
                        print("{}".format(ticket).translate({ord(i): None for i in "(')[]"}))
                    print("\nPlease press 1,2 or 3 to select ticket. Or press b to go back")
                    ui = input(": ")

                    if ui == "1":  # purchase ticket1
                        print(tickets.__getitem__(0), " selected, purchase this ticket? Cost: 250 (y/n)")
                        ui = input(": ")
                        if ui == "y":
                            print("purchasing: ", tickets.__getitem__(0))
                            if glove.get_tickets(username, 1) == "None":
                                # if the metallica cell has not been filled,
                                # then the user is able to purchase the ticket
                                glove.update_tickets(username, 1)

                                # this chunk updates points
                                current = glove.getpointamnt(username)
                                print("here" + current)
                                current = int(current)
                                new = current - 250
                                glove.update_points(username, str(new))

                                print("Metallica Ticket Purchased")
                            else:
                                print("You have already purchased a Metallica Ticket, due to current COVID guidelines, "
                                      "you are only allowed one ticket for each event.")
                        else:
                            print("purchase cancelled")

                    if ui == "2":
                        print(tickets.__getitem__(1), " selected, purchase this ticket? Cost: 250 (y/n)")
                        ui = input(": ")
                        if ui == "y":
                            print("purchasing: ", tickets.__getitem__(1))
                            if glove.get_tickets(username, 2) == "None":
                                # if the lady gaga cell has not been filled,
                                # then the user is able to purchase the ticket
                                glove.update_tickets(username, 2)

                                # this chunk updates points
                                current = glove.getpointamnt(username)
                                current = int(current)
                                new = current - 250
                                glove.update_points(username, str(new))

                                print("Lady Gaga Ticket Purchased")
                            else:
                                print("You have already purchased a Lady Gaga Ticket, due to current COVID guidelines, "
                                      "you are only allowed one ticket for each event.")
                        else:
                            print("purchase cancelled")

                    if ui == "3":
                        print(tickets.__getitem__(2), " selected, purchase this ticket? Cost: 250 (y/n)")
                        ui = input(": ")
                        if ui == "y":
                            print("purchasing: ", tickets.__getitem__(2))
                            if glove.get_tickets(username, 3) == "None":
                                # if the Keith Urban cell has not been filled,
                                # then the user is able to purchase the ticket
                                glove.update_tickets(username, 3)

                                # this chunk updates points
                                current = glove.getpointamnt(username)
                                current = int(current)
                                new = current - 250
                                glove.update_points(username, str(new))

                                print("Keith Urban Ticket Purchased")
                            else:
                                print(
                                    "You have already purchased a Keith Urban Ticket, due to current COVID guidelines, "
                                    "you are only allowed one ticket for each event.")
                        else:
                            print("purchase cancelled")

                    if ui == "b" or "B":
                        break

                    else:
                        print("Invalid input, please try again.")

            # Displays owned tickets
            if ui == "2":
                # retrieves ticket codes from sql
                print("\n<<Owned Tickets>>")
                if glove.get_tickets(username, 1) == "1":
                    print("Metallica")
                if glove.get_tickets(username, 2) == "1":
                    print("Lady Gaga")
                if glove.get_tickets(username, 3) == "1":
                    print("Keith Urban")

                t.sleep(5)

            # Add points
            if ui == "3":
                print("\n<<Add points>>")
                print("Please enter how many points you would like(5,000 at a time): ")
                ui = int(input())
                if ui <= 5000:
                    try:
                        # updates points
                        current = int(points) + int(ui)
                        new = str(current)
                        glove.addpoints(username, new)
                    except:
                        print("Error in adding tickets")
                    else:
                        print("Successfully added points.")
                        print("New balance: ", points)

            # signout option
            if ui == "4":
                print("\n<<Signout>>")
                print("Are you sure you want to signout?(y/n): ")
                ui = input(": ")
                if ui == 'y' or ui == "yes":
                    glove.signOut(username, password)  # sets loggedin to false
                    if not glove.loggedIN:
                        print("\nSignout successful")
                        main()
                        break
                else:
                    print("Signout cancelled")


# super dope intro
def intro():
    try:
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + ''' 
     ____________________      ___              ___
    |____________________|    |___|            |___|
          |       |           || | |          | | ||
          |       |           ||  | |        | |  ||
          |       |           ||   | |      | |   ||
          |       |           ||    | |    | |    ||
          |       |           ||     | |  | |     ||
          |       |           ||      | || |      ||                                
          |_______|icket      ||       |__|       ||anager
            ''')
    except:
        print('Boring mode detected, unable to print header\n')
        pass
    else:

        t.sleep(0.2)
        i = 0
        while i < 5:  # this has no functionality other than displaying connecting to the server
            print("\r      Connecting to Server    ", end="")
            t.sleep(0.25)
            print("\r     <Connecting to Server>    ", end="")
            t.sleep(0.25)
            print("\r    <<Connecting to Server>>    ", end="")
            t.sleep(0.25)
            print("\r   <<<Connecting to Server>>>   ", end="")
            t.sleep(0.25)
            print("\r  <<<<Connecting to Server>>>> ", end="")
            t.sleep(0.25)
            print("\r <<<<<Connecting to Server>>>>> ", end="")
            t.sleep(0.25)
            print("\r <<<<<   Connected   >>>>> ", end="")
            i += 1

        while True:  # this has no functionality other than displaying Welcome to Ticket Manager
            try:
                print("\rW    ", end="")
                t.sleep(0.21)
                print("\rWe   ", end="")
                t.sleep(0.21)
                print("\rWel  ", end="")
                t.sleep(0.21)
                print("\rWelc ", end="")
                t.sleep(0.21)
                print("\rWelco", end="")
                t.sleep(0.21)
                print("\rWelcom", end="")
                t.sleep(0.21)
                print("\rWelcome ", end="")
                t.sleep(0.21)
                print("\rWelcome t", end="")
                t.sleep(0.21)
                print("\rWelcome to", end="")
                t.sleep(0.21)
                print("\rWelcome to T", end="")
                t.sleep(0.21)
                print("\rWelcome to Ti", end="")
                t.sleep(0.21)
                print("\rWelcome to Tic", end="")
                t.sleep(0.21)
                print("\rWelcome to Tick", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticke", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket M", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket Ma", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket Man", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket Mana", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket Manag", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket Manage", end="")
                t.sleep(0.21)
                print("\rWelcome to Ticket Manager", end="")
                break
            except:
                print("\nError printing welcome message..")
                print("Welcome anyway..")


if __name__ == '__main__':
    main()
