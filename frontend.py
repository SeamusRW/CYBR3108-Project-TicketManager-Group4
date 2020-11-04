import credentials as creds
import time as t
import socket

try:
    import colorama
    from colorama import init
    from colorama import Fore, Back, Style

    init()
except:
    print("Unable to import colorama")
    print("Entering boring mode")


def main():
    intro()
    ui = ""
    print("\n____________________")
    while ui != "quit" or ui != "3":
        print("\n1: Login\n2: Signup\n3: Quit")
        t.sleep(0.2)

        ui = input(": ")

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
                if creds.login(username, password):
                    application(username, password)
                else:
                    print("Unable to login, Please check login information")

        if ui == "2" or ui == "signup":
            print("\n<<Signup>>")
            print("1"
                  "____________________")
            t.sleep(0.2)
            while True:
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
                    if creds.checkUser(username):
                        print("Username Taken, please try again")
                    else:
                        try:
                            password = input("Please enter Password: ")
                        except TypeError:
                            print("Invalid Type")
                        else:
                            if creds.valPass(password):
                                verify = input("Please verify Password: ")
                                if verify == password:
                                    fname = input("Please enter first name: ")
                                    lname = input("Please enter last name: ")

                                    creds.signup(username, password, fname, lname)
                                    # except:
                                    #   print("Error Signing up")
                                    # else:
                                    #  print("Sign up succesfully")
                                    break
                                else:
                                    print("\nPasswords do not match, please try again")
                            else:
                                print("Password does not meet requirements please try again")

        if ui == "3" or ui == "quit":
            break


def application(username, password):
    ui = ""
    tickets = [["Metallica", 20], ["Lady Gaga", 20], ["Lecrae", 20]]
    owned = []
    if creds.loggedIN:
        points = creds.getpointamnt(username)
        print("Welcome " + username + "!")

        while ui != "4" or "signout":
            print("1: Buy Tickets \n2: View Owned Tickets \n3: Add Points \n4: Signout")
            print("points: ", points)
            ui = input(": ")

            if ui == "1":  # buy tickets
                while ui != "b" or "B":
                    print("<<Buy Tickets>>")
                    print("Points: ", points)
                    print("Available tickets: \n")
                    for ticket in tickets:
                        print(ticket)
                    print("\nPlease press 1,2 or 3 to select ticket. Or press b to go back")
                    ui = input(": ")

                    if ui == "1":
                        print(tickets.__getitem__(0), " selected, purchase this ticket? Cost: 20 (y/n)")
                        ui = input(": ")
                        if ui == "y":
                            print("purchasing: ", tickets.__getitem__(0))
                            owned.append(tickets.__getitem__(0))
                            creds.update_points(username,points - 20)
                            points = creds.getpointamnt(username)
                        else:
                            print("purchase cancelled")

                    if ui == "2":
                        print(tickets.__getitem__(1), " selected, purchase this ticket? Cost: 20 (y/n)")
                        ui = input(": ")
                        if ui == "y":
                            print("purchasing: ", tickets.__getitem__(1))
                            owned.append(tickets.__getitem__(1))
                            creds.update_points(username, points - 20)
                            points = creds.getpointamnt(username)
                        else:
                            print("purchase cancelled")

                    if ui == "3":
                        print(tickets.__getitem__(2), " selected, purchase this ticket? Cost: 20 (y/n)")
                        ui = input(": ")
                        if ui == "y":
                            print("purchasing: ", tickets.__getitem__(2))
                            owned.append(tickets.__getitem__(2))
                            creds.update_points(username, points - 20)
                            points = creds.getpointamnt(username)
                        else:
                            print("purchase cancelled")

                    if ui == "b" or "B":
                        break

                    else:
                        print("Invalid input, please try again.")

            if ui == "2":
                print("\n<<Owned Tickets>>")
                for ticket in owned:
                    print(ticket)

                t.sleep(5)

            if ui == "3":
                print("\n<<Add points>>")
                print("Please enter how many points you would like(max 5,000): ")
                ui = input()
                if ui <= "5000":
                    try:
                        current = creds.getpointamnt(username)
                        new = int(current) + int(ui)
                        new = str(new)
                        creds.update_points(username,new)
                    except:
                        print("Error in adding tickets")
                    else:
                        points = creds.getpointamnt(username)
                        print("Successfully added points.")
                        print("New balance: ", points)

            if ui == "4":
                print("\n<<Signout>>")
                print("Are you sure you want to signout?(y/n): ")
                ui = input(": ")
                if ui == 'y' or "yes":
                    creds.signOut(username, password)
                    if not creds.loggedIN:
                        print("\nSignout successful")
                        main()
                else:
                    print("Signout cancelled")


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

    t.sleep(0.2)
    i = 0
    while i < 5:
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

    while True:
        print("\rW    ", end="")
        t.sleep(0.2)
        print("\rWe   ", end="")
        t.sleep(0.20)
        print("\rWel  ", end="")
        t.sleep(0.20)
        print("\rWelc ", end="")
        t.sleep(0.20)
        print("\rWelco", end="")
        t.sleep(0.20)
        print("\rWelcom", end="")
        t.sleep(0.20)
        print("\rWelcome ", end="")
        t.sleep(0.2)
        print("\rWelcome t", end="")
        t.sleep(0.20)
        print("\rWelcome to", end="")
        t.sleep(0.20)
        print("\rWelcome to T", end="")
        t.sleep(0.20)
        print("\rWelcome to Ti", end="")
        t.sleep(0.20)
        print("\rWelcome to Tic", end="")
        t.sleep(0.20)
        print("\rWelcome to Tick", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticke", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket M", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket Ma", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket Man", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket Mana", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket Manag", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket Manage", end="")
        t.sleep(0.20)
        print("\rWelcome to Ticket Manager", end="")
        break


if __name__ == '__main__':
    main()
