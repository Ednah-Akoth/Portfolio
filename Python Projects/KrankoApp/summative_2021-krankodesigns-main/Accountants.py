from datetime import datetime

from Developers import*
class Accountants(Developers):
    unique_code = 98000000#initializing the unique code
    #Setting instance Attributes
    def __init__(self, fname, lname, password, dob, doj, phone_no, acc, specialty, availability,
                 years_of_experience, rate, portfolio_link, licence_no):
        super().__init__(fname, lname, password, dob, doj, phone_no, acc, specialty, availability, years_of_experience, rate, portfolio_link)
        self.unique_code = Accountants.unique_code+1
        self.licence = licence_no
        Accountants.unique_code = Accountants.unique_code+1

    def take_a_loan(self, other3):  # Taking loan method for developers
        # other3 is the Krankodesigns account that holds the money that Krankodesigns has
        from datetime import datetime
        date_today = date.today()
        days_since_joining = date_today-datetime.strptime(self.doj, "%d/%m/%Y").date()  # Calculating the amount of time the user has been a Krankodesigns account owner
        if days_since_joining < timedelta(days=90):  # Set minimum days needed without asking for a loan is 90 days. Checking whether user's membership period has reached this
            print("You can only borrow after being a user of KrankoDesigns for more than 90 days")
            # Takes to main menu
        else:
            while True:
                try:
                    amount = float(input("Please enter amount you want to borrow without the $"))
                    break
                except ValueError:
                    print("Please enter a float value")
            if amount > 6000:  # Checks whether amount is within the borrowing max of accountants = 6000
                print("Request out of range. Can only borrow a maximum of $6000. Try the process again")
            elif amount > other3:  # checks whether amount is available in the Krankodesigns account
                print("Amount not available. Try the process again with a lower request")
            else:  # If all conditions met, the amount is added to the user's account and subtracted from KrankoDesigns
                self.acc = self.acc + amount
                other3 = other3 - amount
                print(f"Operation Successful. You have borrowed {amount}. Your repayment period is 6 months")

        return True
if __name__=="__main__":
    accountant = Accountants("Gilbert", "Odipo", "1997", "12/12/1978", "12/12/2010", 789654325, 50000,
                             "Auditor", "yes", 7, 23455, "ghjoiuytgfredsw","KBG/345tr/ICPAk")