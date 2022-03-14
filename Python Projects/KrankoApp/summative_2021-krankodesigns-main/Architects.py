from datetime import*
from Developers import *
#This is a child class of the developers class
class Architects(Developers):
    unique_code = 2345000#initializing the unique code
    #Setting instance Attributes
    def __init__(self, fname, lname, password, dob, doj, phone_no, acc, specialty, availability,
                 years_of_experience, rates, portfolio_link, govt_reg_no):
        #Super to inherit the instance attributes of the parent class
        super().__init__(fname, lname, password, dob, doj, phone_no, acc, specialty, availability,
                         years_of_experience, rates, portfolio_link)
        self.unique_code = Architects.unique_code+1
        self.govt_reg_no = govt_reg_no
        Architects.unique_code = Architects.unique_code+1

    def take_a_loan(self, other3):  # Taking loan method for developers
        # other3 is the Krankodesigns account that holds the money that Krankodesigns has
        from datetime import datetime
        date_today = date.today()
        days_since_joining = date_today - datetime.strptime(self.doj,
                                                            "%d/%m/%Y").date()  # Calculating the amount of time the user has been a Krankodesigns account owner
        if days_since_joining < timedelta(
                days=90):  # Set minimum days needed without asking for a loan is 90 days. Checking whether user's membership period has reached this
            print("You can only borrow after being a user of KrankoDesigns for more than 90 days")
            # Takes to main menu
        else:
            while True:
                try:
                    amount = float(input("Please enter amount you want to borrow without the $"))
                    break
                except ValueError:
                    print("Please enter a float value")
            if amount > 15000:  # Checks whether amount is within the borrowing max of aarchitects = 15000
                print("Request out of range. Can only borrow a maximum of $15000. Try the process again")
            elif amount > other3:  # checks whether amount is available in the Krankodesigns account
                print("Amount not available. Try the process again with a lower request")
            else:  # If all conditions met, the amount is added to the user's account and subtracted from KrankoDesigns
                self.acc = self.acc + amount
                other3 = other3 - amount
                print(f"Operation Successful. You have borrowed {amount}. Your repayment period is 6 months")

        return True
if __name__=="__main__":
    Hussein = Architects("Jeremiah","Ater","1997","12/12/2001","12/12/2015",1234567,1234567,"skyscraper design","yes",8,1234567,"rtyhgfdewsag","KEG 12345/LM")