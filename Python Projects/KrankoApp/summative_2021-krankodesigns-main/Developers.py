from datetime import *
from krankodesigns1 import*
#This is a child class of the main class Krankodesigns
class Developers(Krankodesigns):
    unique_code = 600 #initializing the unique code
    #Setting instance Attributes
    def __init__(self,fname, lname, password, dob,doj, phone_no, acc, speciality, years_of_experience, availability,rates, portfolio_link):
        super().__init__(fname, lname, password, dob, doj, phone_no, acc)
        self.speciality = speciality
        self.years_of_experience = years_of_experience
        self.rates = rates
        self.portfolio_link = portfolio_link
        self.availability = availability
        self.unique_code = Developers.unique_code+1
        Developers.unique_code = Developers.unique_code+1#Adding one to the code to ensure instances created don't have the same unique IDs

    def take_a_loan(self, other3): #Taking loan method for developers
        #other3 is the Krankodesigns account that holds the money that Krankodesigns has
        from datetime import datetime
        date_today = date.today()
        days_since_joining = date_today-datetime.strptime(self.doj, "%d/%m/%Y").date() #Calculating the amount of time the user has been a Krankodesigns account owner
        if days_since_joining < timedelta(days=90):#Set minimum days needed without asking for a loan is 90 days. Checking whether user's membership period has reached this
            print("You can only borrow after being a user of KrankoDesigns for more than 90 days")
            # Takes to main menu
        else:
            while True:
                try:
                    amount = float(input("Please enter amount you want to borrow without the $"))
                    break
                except ValueError:
                    print("Please enter a float value")
            if amount > 10000:#Checks whether amount is within the borrowing max of developers = 10000
                    print("Request out of range. Can only borrow a maximum of $10000. Try the process again")
            elif amount > other3:#checks whether amount is available in the Krankodesigns account
                    print("Amount not available. Try the process again with a lower request")
            else:#If all conditions met, the amount is added to the user's account and subtracted from KrankoDesigns
                self.acc = self.acc + amount
                other3 = other3 - amount
                print(f"Operation Successful. You have borrowed {amount}. Your repayment period is 6 months")

        return True

    def take_leave(self): #method that allows the professional to take a break from the application
        print("Taking a leave will turn off your availability on the platform. You will"
              "not get any clients")
        response = input("Would you like to proceed? Yes/no")
        if response == "yes" or response== "Yes":#If user wants to continue,
            if self.availability == "no":#Check is their availability is already no
                print("Already on leave.")#if it is, then tell them so
            elif self.availability == "yes": #Else if their availability equals yes,
                self.availability = "no" #change it to no
                print("Enjoy your leave:)")
        elif response == "No" or response == "no":#Else if user doesn't want to proceed
            print("process terminated")#End process
        else:
            print("please enter a valid response, You will be taken to the main menu where you can choose the option again")
        return True


    def resume_from_leave(self):#For user to resume from their leave
            response = input("Are you sure? y or n? ").lower().replace(" ", '') #As if they are sure they would like to proceed
            if response == "y" or response == "yes": #if yes
                if self.availability == "yes":#Check if they are already available and print so
                    print("You are already working")
                    # Back to main menu
                elif self.availability == "no": #Else if they are not available
                    self.availability = "yes"#Change availability to yes
                    print("Welcome back. You are now visible to clients")
                    # Back to main menu
            elif response == "no" or response == "n": #if they don't want to continue
                print("process terminated")#Exit the process
                # Back to main menu
            else:
                print("Please enter a valid response")#If response is not yes or no, tell them to enter the right value
            return True

    def terminate_contract(self, other):#If use wants to end their contract with Krankodesigns
        #other here is prof_dict[unique_ID], the client's specific object in the dictionary
        print("Please note that terminating your contract results in the permanent deletion"
              "of your account and profile.")
        response = input("Would you like to proceed?").lower().replace(" ", '')
        if response in ["y", 'yes', 'yeah']:#If they choose to proceed, delete their account
            del other
            # exit()


        elif response in ["n", "no"]:#Else take them back to the menu
            print("process terminated")
            # back to main menu
        else:
            print("Please enter a valid response")
        return True
if __name__=="__main__":
    dev = Developers("Ednah","Akoth",123456,"12/12/2001","12/11/2021","0784803833",2000,"Data science",2,"yes",1000,"www.link.com")
    ahmed =Developers("Ahmed", "Mohamed", "1997", "12/12/2001","12/12/2012","345678965",1234567,"frontend",8,"yes",1000,"ertgghjuytf",)

