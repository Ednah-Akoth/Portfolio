#For the program to work, make sure you are the reviews and the userdetails are in the same directory as the program files
#This is the main program of Krankodesigns, an application that seeks to bridge the barrier betteeen professionals and their potential clients
#In addition we seek to provide services such as tax calculation, services that are so rare yet, so important
#############----------------- MAIN PROGRAM --------------#####################
import datetime#This would help in conversion of user date of birth to datetime.
from krankodesigns1 import Krankodesigns
from Developers import Developers
from Designers import Designers
from Accountants import Accountants
from Architects import Architects


#Our data storage will consist of data dictionaries, files and lists.
# for the purposes of getting user feedback, we shall use files, that the professionals and the administartion will use in the next phase, which will be improvement and getting a user interface
#The dictionaries and lists, will store data as the user runs the program, to check whether indeed our initial goal is achieved as we prepare for the next phase.
#Starts by initialising our data storage
#Will divide account creation into that for professionals and for clients
prof_dict = {}
#Initialise a dictionary and list for customers
cust_dict = {}
#Adding the created customer to the dictionary
samuel = Krankodesigns("samuel", "wanza", "1997", "12/12/2001", "12/12/2010", 45678897654, 10000000)#"Unique_code=401"
cust_dict[Krankodesigns.unique_code] = samuel
#<----------------------------------------------------->
#store the customers’ unique codes
#Initialize a dictionary for Developers
dev_dict = {}
dev = Developers("Ednah","Akoth","123456","12/12/2001","12/12/2005","12345",13455,"Data science",5,"yes",677998,"gghffdswdf")#Unique code=601
dev1 = Developers("Ednahs","Akoth","123456", "12/12/2001","12/11/2021","0784803833",2000,"Data science",2,"yes",1000,"www.link.com")#Unique code=602
dev3 = Developers("Ednah3","Akoth","123456", "12/12/2001","12/11/2021","0784803833",2000,"Data science",2,"yes",1000,"www.link.com")#Unique code=603
dev_dict[dev.unique_code] = dev
dev_dict[dev1.unique_code] = dev1
dev_dict[dev3.unique_code] = dev3
available_Devs = [dev, dev1, dev3]
prof_dict[dev.unique_code] = dev
prof_dict[dev1.unique_code] = dev1
prof_dict[dev3.unique_code] = dev3

#<---------------------------------------------------->

#Initialize a dictionary/list for Accountants
accountants_dict = {}
accountant = Accountants("Gilbert", "Odipo", "1997", "12/12/1978", "12/12/2010", 789654325, 50000,
                             "Auditor", "yes", 7, 23455, "ghjoiuytgfredsw","KBG/345tr/ICPAK")#Unique_code=98000001
accountants_dict[accountant.unique_code]=accountant
available_accountants = [accountant]
prof_dict[accountant.unique_code]=accountant
#Initialize a dictionary/list for Architects
arch_dict = {}
Hussein = Architects("Jeremiah","Ater","1997","12/12/2001","12/12/2015",1234567,1234567,"skyscraper design","yes",8,1234567,"rtyhgfdewsag","KEG 12345/LM")#Unique_code=2345001
arch_dict[Hussein.unique_code] = Hussein
available_architects = [Hussein]
prof_dict[Hussein.unique_code] = Hussein
#Initialize a dictionary/list for Designers



des_dict = {}
des1= Designers("Ednah","Akoth","123456","12/12/2001","12/4/2010","0784803833",2000,"Murals",2,"yes",1000,"www.link.com")#Unique_code=12340001
des_dict[des1.unique_code]=des1
available_designers=[des1]
prof_dict[des1.unique_code]=des1
print(prof_dict)
#Initialize a dictionary/list for all professionals, in all category of users we have included the professionals dictionaries
# The professionals have special priviledges from other application users
#prof_ID = []

#####-------OBJECTS

#Dictionary of softwares available. This the list of softwares our team of developers has alraedy developed.The prices are quite fair
softwares_available={"1":["Drafano systems",8000000],"2":["kilemi accounting software",20000000],"3":["android python installer",23456700]}
#Initialization of the Krankodesigns money account
krankodesigns_acc =100000000000# T
#Defining the create account function
def create_account():
    #Present the user with  the options they have
    print("Thank you for choosing to open an account with us.")
    print("**************************************************")
    response = input("What type of account to you want?\n1. Customer Account\n2. Developer Account\n"
                     "3. Accountant Account\n"
                     "4. Architect Account\n"
                     "5. Designer Account\n"
                     "Enter the number that corresponds to the account you want:").replace(" ","")
    #Configure program to do what

    if response == "1":


        fname = input('Please enter your first name: ')
        lname = input('Please enter your last name: ')
        while True:#Making sure the correct length of password is input
            password = input("Please enter your password. Must be atleast 6 characters long")
            if len(password) < 6:
                print("Your password is too short")
            else:
                break
        birthday = input("Enter your date of birth in the format DD/MM/YYYY")
        dob = datetime.datetime.strptime(birthday, "%d/%m/%Y")#conversion of the date string to datetime
        phone_no = input("Enter your phone number: ")
        doj = datetime.date.today()#getting current date.
        try:
            acc_bal = int(input("How much do you want your initial deposit to be?"))
        except:
            print("value error")

        print("A Payment prompt has been set to your phone number.")
        #print("Enter a value that is a number")
        user = Krankodesigns(fname, lname, password, dob, doj, phone_no, acc_bal)
        #cust_IDs.append(user.unique_code) #Append the unique ID to the list to keep track of the unique IDs we have
        cust_dict[user.unique_code] = user #Adding the customer to the dictionary of customers
        client_info = open("Userdetails", "r")
        client_info.readlines()
        client_info.close()
        storage = open("Userdetails", "a")

        storage.write(f"first_name:{fname},lastname:{lname},password:{password},dob:{dob},doj:{doj},phone_no{phone_no},acc_bal:{acc_bal}\n")
        storage.close()

        #available_Devs.append(user)
        print("Account created successfully!")
        print(f"This is your unique ID {user.unique_code} that you will use to log in")
        #print("We will take you to the log in page")
    elif response == "2":

        fname = input('Please enter your first name: ')
        lname = input('Please enter your last name: ')
        while True:
            password = input("Please enter your password. Must be at least 6 characters long")
            if len(password) < 6:
                print("Your password is too short")
            else:
                break
        birthday = input("Enter your date of birth in the format DD/MM/YYYY")
        dob = datetime.datetime.strptime(birthday, "%d/%m/%Y")#Conversion of string to datetime
        phone_no = input("Enter your phone number: ")
        doj = datetime.date.today()
        acc_bal = int(input("How much do you want your initial deposit to be?"))#obtaining the initial deposit to our account
        print("A Payment prompt has been set to your phone number.")
        print("Enter a value that is a number")
        specialty = input("What is your specialty? frontend, fullstack etc?: ")
        years_of_experience = input("How many years of experience do you have?")

        rate = int(input("What is your baseline charge for a project? This is the minimum amount you will charge a clients($): "))
        while True:
            availability = input("Are you available to start immediately? yes or no?").replace(" ", "").lower()
            if availability == "yes" or availability == "no":
                break
            else:
                print("Your response can only be a yes or no")
        portfolio_link = input("Enter a link to your portfolio. This will be diplayed to clients: ")
        developer = Developers(fname,lname,password,dob,doj,phone_no,acc_bal,specialty,availability,years_of_experience, rate, portfolio_link )
        #We are stOring the developers details in dictionaries, lists and files. For login details, in the dictionaries.for storage purposes in files.
        dev_dict[dev.unique_code] = developer
        prof_dict[dev.unique_code] = developer
        available_Devs.append(developer)
        client_info = open("Userdetails", "r")
        client_info.readlines()
        client_info.close()

        User_info_storage = open("Userdetails", "a")

        User_info_storage.write(
            f"first_name:{fname},lastname:{lname},password:{password},dob:{dob},doj:{doj},phone_no{phone_no},acc_bal:{acc_bal}\n")
        User_info_storage.close()

        print('Account created successfully')
        print(f"This is the unique ID {dev.unique_code} that you will use to log in.")

    elif response == "3":

        fname = input('Please enter your first name: ')
        lname = input('Please enter your last name: ')
        while True:
            password = input("Please enter your password. Must be atleast 6 characters long")
            if len(password) < 6:
                print("Your password is too short")
            else:
                break
        birthday = input("Enter your date of birth in the format DD/MM/YYYY")
        dob = datetime.datetime.strptime(birthday, "%d/%m/%Y")
        phone_no = input("Enter your phone number: ")
        doj = datetime.datetime.today()
        acc_bal = int(input("How much do you want your initial deposit to be?"))
        #print("A Payment prompt has been set to your phone number.")
        print("Enter a value that is a number")
        specialty = input("What is your specialty?: ")
        years_of_experience = input("How many years of experience do you have?")
        rate = int(input("What is your baseline charge for a project? This is the minimum amount you will charge a clients($): "))
        print("Enter an integer")
        while True:
            availability = input("Are you available to start immediately? yes or no?").replace(" ", "").lower()
            if availability == "yes" or availability == "no":
                break
            else:
                print("Your response can only be a yes or no")
        licence_no = input("Enter your licence number. This will be diplayed to clients for authenitication of your accounting career: ")
        portfolio_link= input("Enter the link of your portfolio")
        accountant = Accountants(fname, lname, password, dob, doj, phone_no, acc_bal, specialty, availability,
                         years_of_experience, rate,portfolio_link, licence_no)
        #accountants_IDs.append(accountant.unique_code)
        accountants_dict[accountant.unique_code] = accountant
        prof_dict[accountant.unique_code] = accountant
        client = open("Userdetails", "r")
        client.readlines()
        client.close()
        storage = open("Userdetails", "a")

        storage.write(
            f"first_name:{fname},lastname:{lname},password:{password},dob:{dob},doj:{doj},phone_no{phone_no},acc_bal:{acc_bal}\n")
        storage.close()

        print('Account created successfully')
        print(f"This is the unique ID {accountant.unique_code} that you will use to log in.")
    elif response == "4":

        fname = input('Please enter your first name: ')
        lname = input('Please enter your last name: ')
        while True:
            password = input("Please enter your password. Must be at least 6 characters long")
            if len(password) < 6:
                print("Your password is too short")
            else:
                break
        birthday = input("Enter your date of birth in the format DD/MM/YYYY")
        dob = datetime.datetime.strptime(birthday, "%d/%m/%Y")#
        phone_no = input("Enter your phone number: ")
        doj = datetime.date.today()
        acc_bal = int(input("How much do you want your initial deposit to be?"))
        #print("A Payment prompt has been set to your phone number.")
        print("Enter a value that is a number")
        specialty = input("What is your specialty?: ")
        years_of_experience = input("How many years of experience do you have?")
        rate = int(input("What is your baseline charge for a project? This is the minimum amount you will charge a clients($): "))
        #print("Enter an integer")
        while True:
            availability = input("Are you available to start immediately? yes or no?").replace(" ", "").lower()
            if availability == "yes" or availability == "no":
                break
            else:
                print("Your response can only be a yes or no")
        portfolio_link = input("Enter a link to your portfolio. This will be displayed to clients: ")
        govt_reg_no = input("Enter your government registration number. This will be used to check the authenticity of your licence: ")
        architect = Architects(fname, lname, password, dob, doj, phone_no, acc_bal, specialty, availability,
                         years_of_experience, rate, portfolio_link,govt_reg_no)
        #arch_IDs.append(architect.unique_code)
        arch_dict[architect.unique_code] = architect
        prof_dict[architect.unique_code] = architect
        available_architects.append(architect)
        client = open("Userdetails", "r")
        client.readlines()
        client.close()
        storage = open("Userdetails", "a")

        storage.write(
            f"first_name:{fname},lastname:{lname},password:{password},dob:{dob},doj:{doj},phone_no{phone_no},acc_bal:{acc_bal}\n")
        storage.close()

        print('Account created successfully')
        print(f"This is the unique ID {architect.unique_code} that you will use to log in.")
    elif response == "5":

        fname = input('Please enter your first name: ')
        lname = input('Please enter your last name: ')
        while True:
            password = input("Please enter your password. Must be at least 6 characters long")
            if len(password) < 6:
                print("Your password is too short")
            else:
                break
        birthday = input("Enter your date of birth in the format DD/MM/YYYY")
        dob = datetime.datetime.strptime(birthday, "%d/%m/%Y")
        phone_no = input("Enter your phone number: ")
        doj = datetime.date.today()
        acc_bal = int(input("How much do you want your initial deposit to be?"))
        #print("A Payment prompt has been set to your phone number.")
        #print("Enter a value that is a number")
        specialty = input("What is your specialty?: ")
        years_of_experience = input("How many years of experience do you have?")
        rate = int(input(
                "What is your baseline charge for a project? This is the minimum amount you will charge a clients($): "))
        #print("Enter an integer")
        while True:
            availability = input("Are you available to start immediately? yes or no?").replace(" ", "").lower()
            if availability == "yes" or availability == "no":
                break
            else:
                print("Your response can only be a yes or no")
        portfolio_link = input("Enter a link to your portfolio. This will be displayed to clients: ")
        #Storage of designers details
        designer = Designers(fname, lname, password, dob, doj, phone_no, acc_bal, specialty, availability,
                         years_of_experience, rate, portfolio_link)
        des_dict[designer.unique_code] = designer
        prof_dict[designer.unique_code] = designer
        available_designers.append(designer)
        client= open("Userdetails", "r")
        client.readlines()
        client.close()
        storage = open("Userdetails", "a")

        storage.write(
            f"first_name:{fname},lastname:{lname},password:{password},dob:{dob},doj:{doj},phone_no{phone_no},acc_bal:{acc_bal}\n")
        storage.close()

        print('Account created successfully')
        print(f"This is the unique ID {designer.unique_code} that you will use to log in.")
    else:
        print("Please enter a valid response (a number)")


def kranko_designs():
    print("Hello, Welcome to KrankoDesigns!")
    print("********************************")
    while True:
        response = input("type 1 to create an account with us.\n"
                         "type 2 to log in").replace(" ",'')
        if response == "1":
            create_account()
        elif response == "2":

            try:
                unique_ID = int(input("Enter your Unique ID: "))#The user logs in if and only if they have an accountant with us. Apart from that, they
                password = input("Enter your password:")
                if unique_ID in cust_dict.keys() and cust_dict[unique_ID].password == password:
                    while True:
                        #if one is a client, he or she can only gain access to the client menu
                        ans = input("Welcome to KrankoDesigns! What would you like to do?\n"
                                    "1. Hire a developer\n"
                                    "2. Hire an accountant\n"
                                    "3. Hire an architect\n"
                                    "4. Hire a designer\n"
                                    "5. Buy Software\n"
                                    "6. Calculate tax\n"
                                    "7.log out")

                        if ans == "1":
                            cust_dict[unique_ID].hiring_developer(dev_dict,available_Devs,prof_dict,krankodesigns_acc)
                            #we have passed parameters in the calling of the methods to minimise corresponding to the particular data that requires update
                        elif ans == "2":
                            cust_dict[unique_ID].hiring_accountant(accountants_dict,available_accountants,prof_dict,krankodesigns_acc)
                        elif ans == "3":
                            cust_dict[unique_ID].hiring_architect(arch_dict,available_architects,prof_dict,krankodesigns_acc)
                        elif ans == "4":
                            cust_dict[unique_ID].hiring_designer(des_dict,available_designers,prof_dict,krankodesigns_acc)
                        elif ans == "5":
                            cust_dict[unique_ID].buying_software(softwares_available,krankodesigns_acc)
                        elif ans == "6":
                            cust_dict[unique_ID].calculate_tax()
                        elif ans =="7":
                            f = open("reviews", "r")
                            f.readlines()
                            f.close()
                            g = open("reviews","a")
                            review = input("Kindly review our services and rate our app.")
                            g.write(f"{review}\n")
                            g.close()

                            return

                        else:
                            print("Please enter a valid response (a number)")

                elif unique_ID in prof_dict.keys() and prof_dict[unique_ID].password == password:
                    while True:#This is the professionals menu, You can only gain access to it, if you have your unique codes and passwords in the professionals dictionary

                        ans = input("Welcome to KrankoDesigns! What would you like to do?\n"
                                    "1. Hire a developer\n"
                                    "2. Hire an accountant\n"
                                    "3. Hire an architect\n"
                                    "4. Hire a designer\n"
                                    "5. Buy Software\n"
                                    "6. Calculate tax\n"
                                    "7. Take a loan\n"
                                    "8. Take a leave from the app\n"
                                    "9. Resume from leave\n"
                                    "10. Terminate contract with the app\n"
                                    "11.log out")
                        if ans == "1":
                            #We are calling out the methods, each coresponding to a particular dictionary, indiviividual professional dictionary and the krankodesigns account.
                            prof_dict[unique_ID].hiring_developer(dev_dict,available_Devs,prof_dict,krankodesigns_acc)
                        elif ans == "2":
                            prof_dict[unique_ID].hiring_accountant(accountants_dict,available_accountants,prof_dict,krankodesigns_acc)
                        elif ans == "3":
                            prof_dict[unique_ID].hiring_architect(arch_dict,available_architects,prof_dict,krankodesigns_acc)
                        elif ans == "4":
                            prof_dict[unique_ID].hiring_designer(des_dict,available_designers,prof_dict,krankodesigns_acc)
                        elif ans == "5":
                            prof_dict[unique_ID].buying_software(softwares_available,krankodesigns_acc)
                        elif ans == "6":
                            prof_dict[unique_ID].calculate_tax()
                        elif ans == "7":
                            prof_dict[unique_ID].take_a_loan(krankodesigns_acc)
                        elif ans == "8":
                            prof_dict[unique_ID].take_leave()
                        elif ans == "9":
                            prof_dict[unique_ID].resume_from_leave()
                        elif ans == "10":
                            prof_dict[unique_ID].terminate_contract(prof_dict[unique_ID])

                        elif ans == "11":#The professionals can be able to view user reviews and improve where necessary
                            f =open("reviews","r")
                            g=f.read()
                            print(f"Reviews so far:\n{g}")
                            f.close()
                            exit()
                        else:
                            print("Please enter a valid response (a number)")

                else:
                    print("Invalid Unique ID or Password")
            except ValueError:
                print("Your unique ID should be numerals only. Check and try again")
        else:
            print("Invalid entry")
kranko_designs()#we are calling out Krankodesigns which is the main function and thus acts as the link to the all program
