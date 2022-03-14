#from Developers import*
import datetime
import unittest

#This is the main class
class Krankodesigns:
    # initializing the unique code
    unique_code = 400
    # Setting instance Attributes
    def __init__(self, fname, lname, password, dob, doj,phone_no, acc):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.dob = dob
        self.unique_code = Krankodesigns.unique_code+1
        self.doj = doj
        self.phone_no = phone_no
        self.acc = acc
        # Adding one to the code to ensure instances created don't have the same unique IDs
        Krankodesigns.unique_code = Krankodesigns.unique_code+1

    #Defining methods of the class

    def hiring_developer(self,other,other1,other2,other3):
        # other1 = list available developers
        # other - dev dict
        # other2 - professionals dic
        #Other 3 - krankodesigns account
        print("Developers available")
        for i, j in enumerate(other1):#Loop through the list of developer's, printing only their unique codes and specialty
            print(f"Unique code:{j.unique_code},Programming language:{j.speciality}")
        #ask user for their choice of developer. Exception handling to handle value error
        while True:
            try:
                hired_developer = int(input("Enter the unique code of the developer you want to hire"))
                break
            except ValueError:
                print("Please enter the corresponding integer")

        if hired_developer in other.keys():#Checks if the developer is in the developer's dictionary
            if hired_developer in other2.keys():#Checks if the developer is in the general professional's dictionary
                #Prints out developer's names, rate
                print(f"You have decided to hire {other2[hired_developer].fname} {other2[hired_developer].lname}"
                      f"\nphone no: {other2[hired_developer].phone_no}\nrates:{other[hired_developer].rates}")
                #Calculuation of amount's to be charged to the client, to be added to krankodesigns and to developer's account

                if self.acc >= other2[hired_developer].rates:#If  user's account balance is greater than the rate of the developer
                    self.acc = self.acc-other2[hired_developer].rates#Subtract this amount from the client
                    other3 = other3+(0.2*other2[hired_developer].rates)#Add 20% of the rate to Krankodesigns account
                    other2[hired_developer].acc=other2[hired_developer].acc+(0.8*other2[hired_developer].rates)#Add 80% of the amount to the hired developer
                    print(f"You have spent $ {other2[hired_developer].rates} to hire the developer")#Tell the user how much they have spent

                    print("He will reach out to you shortly")
                    del other[hired_developer]#Remove developer to avoid having the developer get hired twice
                    for i, j in enumerate(other1):#Remove hired developer from the list of availailable developers
                        if (j.unique_code == hired_developer):
                            del other1[i]


                else:#Else if the user doesn't have sufficient funds
                    print("You have insufficient amount\nKindly refill your account")
            else:#If the developer is in the developer’s dictionary and not in professional’
                print("The developer is currently busy")
        else:#if the developer is not in any of the professionals and the developers dictionary
            print("The developer does not exist.")
        return True

    def hiring_accountant(self, other, other1, other2, other3):
        # other1 = list available accountant
        # other - accountant dict
        # other2 - professionals dic
        # Other 3 - krankodesigns account

        print("accountants available")
        for i, j in enumerate(other1):#Loop through the list of accountants, printing only their unique codes and specialty
            print(f"Unique code:{j.unique_code},Speciality:{j.speciality}")
        # ask user for their choice of developer. Exception handling to handle value error
        while True:
            try:
                hired_accountant = int(input("Enter the unique code of the accountant you want to hire"))
                break
            except ValueError:
                print("Please enter the corresponding integer")

        if hired_accountant in other.keys():#Checks if the accountant is in the developer's dictionary
            if hired_accountant in other2.keys():#Checks if the accountant is in the general professional's dictionary

                print(f"You have decided to hire {other2[hired_accountant].fname} {other2[hired_accountant].lname}"
                      f"\nphone no: {other2[hired_accountant].phone_no}\nrates:{other2[hired_accountant].rates}")
                # Calculuation of amount's to be charged to the client, to be added to krankodesigns and to developer's account
                if self.acc >= other2[hired_accountant].rates:#If  user's account balance is greater than the rate of the developer
                    self.acc = self.acc - other2[hired_accountant].rates
                    other3 = other3 + (0.2 * other2[hired_accountant].rates)#Add 20% of the rate to Krankodesigns account
                    other2[hired_accountant].acc = other2[hired_accountant].acc + (0.8 * other2[hired_accountant].rates)#Add 80% of the rate to hired accountant
                    print(f"You have spent $ {other2[hired_accountant].rates} to hire the accountant")#Tell the user how much they have spent
                    print("they will reach out to you shortly")
                    del other[hired_accountant]#Remove developer to avoid having the accountant get hired twice
                    for i, j in enumerate(other1):#Remove hired accountant from the list of availailable accountant
                        if (j.unique_code == hired_accountant):
                            del other1[i]

                else:#Else if the user doesn't have sufficient funds
                    print("You have insufficient amount\nKindly refill your account")
            else:#If the accountant is in the account's dictionary and not in professional’
                print("The accountant is currently busy")
        else:#if the accountant is not in any of the professionals and the accountants dictionary
            print("The accountant does not exist.")
        return True

    def hiring_architect(self, other, other1, other2, other3):
        # other1 = list available architect
        # other - arch dict
        # other2 - professionals dic
        # Other 3 - krankodesigns account
        print("Architects available")
        for i, j in enumerate(other1):#Loop through the list of architect, printing only their unique codes and specialty
            print(f"Unique code:{j.unique_code},speciality:{j.speciality}")
        # ask user for their choice of architect. Exception handling to handle value error
        while True:
            try:
                hired_architect = int(input("Enter the unique code of the architect you want to hire"))
                break
            except ValueError:
                print("Please enter the corresponding integer")

        if hired_architect in other.keys():#Checks if the architects is in the architect's dictionary
            if hired_architect in other2.keys():#Checks if the architects is in the general professional's dictionary
                # Prints out architect's names, rate
                print(f"You have decided to hire {other2[hired_architect].fname} {other2[hired_architect].lname}"
                      f"\nphone no: {other2[hired_architect].phone_no}\nrates:{other2[hired_architect].rates}")
                # Calculuation of amount's to be charged to the client, to be added to krankodesigns and to architect's account
                if self.acc >= other2[hired_architect].rates:#If  user's account balance is greater than the rate of the architect
                    self.acc = self.acc - other2[hired_architect].rates#Subtract this amount from the client
                    other3 = other3 + (0.2 * other2[hired_architect].rates)#Add 20% of the amount to Krankodesigns account
                    other2[hired_architect].acc = other2[hired_architect].acc + (0.8 * other2[hired_architect].rates)# Add 80% of the amount to the architects's account
                    print(f"You have spent $ {other2[hired_architect].rates} to hire the architect")
                    print("He will reach out to you shortly")
                    del other[hired_architect]#Remove architects to avoid having the architect get hired twice
                    for i, j in enumerate(other1):#Remove hired architect from the list of availailable architect
                        if (j.unique_code == hired_architect):#Delete from the list of available architects
                            del other1[i]

                else:#Else if the user doesn't have sufficient funds
                    print("You have insufficient amount\nKindly refill your account")
            else:#If the architect is in the account's dictionary and not in professional’
                print("The architect is currently busy")
        else:#if the architect is not in any of the professionals and the accountants dictionary
            print("The architect does not exist.")
        return True

    def hiring_designer(self, other, other1, other2, other3):
        # other1 = list available designers
        # other - des dict
        # other2 - professionals dic
        # Other 3 - krankodesigns account

        print("Designers available")#Print the available designers
        for i, j in enumerate(other1):#Loop through the list of designers, printing only their unique codes and specialty
            print(f"Unique code:{j.unique_code},speciality:{j.speciality}")
        # ask user for their choice of designer. Exception handling to handle value error
        while True:
            try:
                hired_designer = input("Enter the unique code of the designer you want to hire")
                break
            except ValueError:
                print("Please enter the corresponding integer")

        if hired_designer in other.keys():#Checks if the designers is in the designers' dictionary
            if hired_designer in other2.keys():#Checks if the designers is in the general professional's dictionary
                # Prints out architect's names, rate
                print(f"You have decided to hire {other2[hired_designer].fname} {other2[hired_designer].lname}"
                        f"\nphone no: {other2[hired_designer].phone_no}\nrates:{other2[hired_designer].rates}")
                # Calculuation of amount's to be charged to the client, to be added to krankodesigns and to designer's account
                if self.acc >= other2[hired_designer].rates:#If  user's account balance is greater than the rate of the designers
                    self.acc = self.acc - other2[hired_designer].rates#Subtract this amount from the client
                    other3 = other3 + (0.2 * other2[hired_designer].rates)#Add 20% of the amount to Krankodesigns account
                    other2[hired_designer].acc = other2[hired_designer].acc + (
                                0.8 * other2[hired_designer].rates)# Add 80% of the amount to the designer's account
                    print(f"You have spent $ {other2[hired_designer].rates} to hire the designer")
                    print("He will reach out to you shortly")
                    del other[hired_designer]#Remove designer to avoid having the designer get hired twice
                    for i, j in enumerate(other1):#Remove hired designer from the list of availailable designers
                        if (j.unique_code == hired_designer):
                            del other1[i]

                else:#Else if the user doesn't have sufficient funds
                    print("You have insufficient amount\nKindly refill your account")
            else:#If the designer is in the account's dictionary and not in professional
                print("The architect is currently busy,try another one")
        else:#if the designer is not in any of the professionals and the designers dictionary
            print("The designer does not exist.")
        return True

    def buying_software(self, other, other3):
        #Other3 = Kranko Designs
        #other = Dictionary with lists of the available softwares
        print("Softwares available")
        for key,value in other.items():#Loops through the dictionary of software and print the unique key of the software,the software and its cost
            print(f"Unique code:{key},software:{other[key][0]},cost:{other[key][1]}")
        software = input("Enter the unique code of the software you want to buy")
        if software in other.keys():#Checks if the selected software is in the list
            print(f"You have decided to buy {other[software][0]},cost:{other[software][1]}")#if yes print the software the userr has bought
            if self.acc >= other[software][1]:#If the user's account balance is greater than the cost of the software
                self.acc = self.acc - other[software][1]#Subtract the cost of the software from the user's balance
                other3 = other3 + other[software][1]#add the cost of the software to krankodesigns account
                print(f"You have spent $ {other[software][1]} to buy the software")#Print to the user how much they have spent
                print("Our staff will soon direct how on how you will obtain it")

            else:
             print("You have insufficient amount\nKindly refill your account")#If user doesn't have sufficient funds
        else:
            print("The software does not exist.")#If use enters code for software that's is not among the ones displayed
        return True




    def calculate_tax(self):
        print("Welcome to Krankodesigns tax calculator")
        print("<--------------------------------------->")
        response1 = input("What type of tax do you want to calculate?\nEnter 1 for Individual monthly tax\n"
                          "Enter 2 for company tax")#Ask user which calculation they want
        if response1 == "1":
            while True:#To handle the exceptions that may be raised as a result of entering values that are not integers
                try:
                    amount1 = int(input("Enter basic salary in Ksh:"))
                    amount2 = int(input("Enter PAYE paid in Ksh:"))
                    amount3 = int(input("Enter the sum total of all benefits enjoyed such as car benefit etc"))
                    break
                except ValueError:
                    print("Please enter integers only")
            amount4 = amount1 + amount3#Adds basic salary and benefits
            monthly_relief = 1204#Fixed relief offered by the government
            if amount4 > 0 and amount4 <= 12298: #for
                tax = 0.1 * amount4
                tax_payable = tax - monthly_relief - amount2
                print("Tax payable: Ksh", tax_payable)
            elif amount4 > 12298 and amount4 <= 23885:
                tax1 = 0.1 * 12298
                tax2 = 0.15 * (23885 - amount4)
                tax = tax1 + tax2
                tax_payable = tax - monthly_relief - amount2

            elif amount4 > 23885 and amount4 <= 35472:
                tax1 = 0.1 * 12298
                tax2 = 0.15 * 11587
                tax3 = 0.20 * (23885 - amount4)
                tax = tax1 + tax2 + tax3
                tax_payable = tax - monthly_relief - amount2
                print("Tax payable: Ksh", tax_payable)
            elif amount4 > 35472 and amount4 <= 47059:
                tax1 = 0.1 * 12298
                tax2 = 0.35 * 11587
                tax3 = 0.25 * (47059 - amount4)
                tax = tax1 + tax2 + tax3
                tax_payable = tax - monthly_relief - amount2
                print("Tax payable: Ksh", tax_payable)
            elif amount4 > 47059:
                tax1 = 0.1 * 12298
                tax2 = 0.60 * 11587
                tax3 = 0.3 * (amount4 - 47059)
                tax = tax1 + tax2 + tax3
                tax_payable = tax - monthly_relief - amount2
                print("Tax payable: Ksh", tax_payable)
        elif response1 == "2":
            gross_income = int(input("Enter your companies gross income"))
            allowable_expenses = int(input("Enter the value of allowable expenses"))
            taxable_income = gross_income - allowable_expenses
            corporate_tax_rate = 0.3
            tax = corporate_tax_rate * taxable_income
            print("Company Tax Value: Ksh", tax)
        else:
            print("Invalid entry")
        return True

if __name__=="__main__":
    samuel = Krankodesigns("samuel", "wanza", "1997", "12/12/2001", "12 / 12 / 2010", 45678897654, 10000000)






