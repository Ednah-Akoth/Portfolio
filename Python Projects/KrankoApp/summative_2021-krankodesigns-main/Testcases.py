from krankodesigns1 import Krankodesigns
from Designers import Designers
from Developers import Developers
from Architects import Architects
from Accountants import Accountants
import unittest

#Test cases for Krankodesigns class
class TestKrankodesigns(unittest.TestCase):
    #samuel=Krankodesigns("samuel","wanza","1997",12/12/2001,12/12/2010,45678897654,10000000)

    def test_calulate_tax(self):
        samuel = Krankodesigns("samuel", "wanza", "1997", 12 / 12 / 2001, 12 / 12 / 2010, 45678897654, 10000000)
        result=samuel.calculate_tax()
        self.assertTrue(result, True)#Checks if the method runs well by checking if it returns True
    def test_buying_software(self):
        samuel = Krankodesigns("samuel", "wanza", "1997", 12 / 12 / 2001, 12 / 12 / 2010, 45678897654, 10000000)
        softwares_available = {"1": ["Drafano systems", 8000000], "2": ["kilemi accounting software", 20000000],
                               "3": ["android python installer", 23456700]}
        krankodesigns_acc = 100000000000

        result=samuel.buying_software(softwares_available, krankodesigns_acc)
        self.assertTrue(result, True)#Checks if the method runs well by checking if it returns True

    def test_hiring_developer(self):
        dictionary={}#dictionary for all developers
        #dict={}
        dict1={}#dictionary for all professionals
        list=[]#A list of all developers available for hire
        samuel = Krankodesigns("samuel", "wanza", "1997", 12 / 12 / 2001, 12 / 12 / 2010, 45678897654, 50000)
        krankodesigns_acc = 100000000000

        ahmed =Developers("Ahmed", "Mohamed", "1997", 12/12/2001,12/12/2012,"345678965",2000,"frontend",8,"yes",1000,"ertgghjuytf",)

        dict1[Developers.unique_code] = ahmed
        dictionary[Developers.unique_code] = ahmed
        list.append(ahmed)
        result=samuel.hiring_developer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(samuel.acc, 49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(ahmed.acc, 2800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)

    def test_hiring_architect(self):
        dictionary = {}#dictionary for all architects

        dict1 = {}#dictionary for all professionals
        list = []#A list of all architects available for hire
        samuel = Krankodesigns("samuel", "wanza", "1997", 12 / 12 / 2001, 12 / 12 / 2010, 45678897654, 50000)
        krankodesigns_acc = 100000000000
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 1000,
                             "skyscraper design", "yes", 8, 1000, "rtyhgfdewsag", "KEG 12345/LM")

        dict1[Architects.unique_code] = Hussein
        dictionary[Architects.unique_code] = Hussein
        list.append(Hussein)
        result = samuel.hiring_architect(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(samuel.acc, 49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(Hussein.acc, 1800)

    def test_hiring_designer(self):
        dictionary = {}#dictionary for all designers
        #dict = {}
        dict1 = {}#dictionary for all professionals
        list = []#A list of all designers available for hire
        samuel = Krankodesigns("samuel", "wanza", "1997", 12 / 12 / 2001, 12 / 12 / 2010, 45678897654, 10000000)
        krankodesigns_acc = 100000000000
        designer = Designers("josphat","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        # dict[Architects.unique_code] = ahmed
        dict1[Designers.unique_code] = designer
        dictionary[Designers.unique_code] = designer
        list.append(designer)
        result = samuel.hiring_designer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
    def test_hiring_accountant(self):
        dictionary = {}#dictionary for all designers
        #dict = {}
        dict1 = {}
        list = []
        samuel = Krankodesigns("samuel", "wanza", "1997", 12 / 12 / 2001, 12 / 12 / 2010, 45678897654, 50000)
        krankodesigns_acc = 100000000000
        accountant = Accountants("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Auditor", "yes", 7, 1000, "ghjoiuytgfredsw","KBG/345tr/ICPAk")
        # dict[Architects.unique_code] = ahmed
        dict1[Accountants.unique_code] = accountant
        dictionary[Accountants.unique_code] = accountant
        list.append(accountant)
        result = samuel.hiring_accountant(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(samuel.acc, 49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(accountant.acc, 50800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)


if __name__== "__main__"  :
    unittest.main()
    #<-------------------------------------------------------------------------------------------------------------->
#Test cases for designer class.
class TestDesigners(unittest.TestCase):
    #samuel=Krankodesigns("samuel","wanza","1997",12/12/2001,12/12/2010,45678897654,10000000)

    def test_calulate_tax(self):
        designer = Designers("Gilbert","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        result=designer.calculate_tax()
        self.assertTrue(result, True)
    def test_buying_software(self):
        designer = Designers("Gilbert","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        softwares_available = {"1": ["Drafano systems", 8000000], "2": ["kilemi accounting software", 20000000],
                               "3": ["android python installer", 23456700]}
        krankodesigns_acc = 100000000000

        result=designer.buying_software(softwares_available, krankodesigns_acc)
        self.assertTrue(result, True)

    def test_hiring_developer(self):
        dictionary={}#dictionary for all developers
        #dict={}
        dict1={}#dictionary for all professionals
        list=[]#A list of all developers available for hire
        designer=Designers("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000, "Graphic designer",
                  "yes", 7, 23455, "ghjoiuytgfredsw")
        krankodesigns_acc = 1000
        ahmed =Developers("Ahmed","Mohamed","123456", "12/12/2001","12/11/2021","0784803833",2000,"Data science",2,"yes",1000,"www.link.com")
        #dict[Developers.unique_code] = ahmed
        dict1[Developers.unique_code] = ahmed
        dictionary[Developers.unique_code] = ahmed
        list.append(ahmed)
        result=designer.hiring_developer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)#Checking whether the method has run successfully
        self.assertEqual(designer.acc,49000)#Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(ahmed.acc,2800)#Checking whether the professional's account balance has been increased accordingly(20% of rate)






    def test_hiring_architect(self):
        dictionary = {}#dictionary for all architects

        dict1 = {}#dictionary for all professionals
        list = []#A list of all architects available for hire
        designer = Designers("Gilbert","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        krankodesigns_acc = 100000000000
        Hussein = Architects("Jeremiah","Ater","1997",12/12/2001,12/12/2015,1234567,1000,"skyscraper design","yes",8,1000,"rtyhgfdewsag","KEG 12345/LM")
        # dict[Architects.unique_code] = ahmed
        dict1[Architects.unique_code] = Hussein
        dictionary[Architects.unique_code] = Hussein
        list.append(Hussein)
        result =designer.hiring_architect(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(designer.acc,49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(Hussein.acc,1800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)

    def test_hiring_designer(self):
        dictionary = {}#dictionary for all designers
        #dict = {}
        dict1 = {}#dictionary for all professionals
        list = []#A list of all designers available for hire
        designer1 = Designers("josphat","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        krankodesigns_acc = 100000000000
        designer = Designers("Gilbert","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        # dict[Architects.unique_code] = ahmed
        dict1[Designers.unique_code] = designer1
        dictionary[Designers.unique_code] = designer1
        list.append(designer1)
        result = designer.hiring_designer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)

    def test_hiring_accountant(self):
        dictionary = {}#dictionary for all accountants

        dict1 = {}#dictionary for all professionals
        list = []#A list of all accountants available for hire
        designer =Designers("Gilbert","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        krankodesigns_acc = 100000000000
        accountant = Accountants("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Auditor", "yes", 7, 1000, "ghjoiuytgfredsw","KBG/345tr/ICPAk")

        dict1[Accountants.unique_code] = accountant
        dictionary[Accountants.unique_code] = accountant
        list.append(accountant)
        result = designer.hiring_accountant(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(designer.acc,49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(accountant.acc, 50800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)
    def test_take_leave(self):
        designer = Designers("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Graphic designer", 7, "yes", 23455, "ghjoiuytgfredsw")
        result = designer.take_leave()
        self.assertTrue(result,True)
        self.assertEqual(designer.availability,"no")#Checking whether the availability has been changed to no

    def test_resume_from_leave(self):
        designer = Designers("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Graphic designer", 7, "yes", 23455, "ghjoiuytgfredsw")
        result = designer.resume_from_leave()
        self.assertTrue(result, True)
        self.assertEqual(designer.availability, "yes")  # Checking whether the availability has been changed to yes

    def test_terminate_contract(self):
        dict = {}
        designer = Designers("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        designer1 = Designers("Gilberts", "Odipos", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")

        dict[Designers] = designer1
        result = designer.terminate_contract(dict)
        self.assertTrue(result, True)



#<----------------------------------------------------------------------------------------------------->
#Test cases for Accountants class
class TestAccountants(unittest.TestCase):
    def test_calulate_tax(self):
        accountant = Accountants("John","Ganda","123456",12/12/1978,12/10/2021,789877665,2000,"Auditing","yes",4,2000,"www.mylink.com","KE_gov_1902")
        result = accountant.calculate_tax()
        self.assertTrue(result, True)

    def test_buying_software(self):
        accountant = Accountants("John", "Ganda", "123456", 12 / 12 / 1978, 12 / 10 / 2021, 789877665, 2000, "Auditing",
                                 "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        softwares_available = {"1": ["Drafano systems", 8000000], "2": ["kilemi accounting software", 20000000],
                               "3": ["android python installer", 23456700]}
        krankodesigns_acc = 100000000000

        result = accountant.buying_software(softwares_available,krankodesigns_acc)
        self.assertTrue(result, True)
    def test_hiring_developer(self):
        dictionary={}#dictionary for all developers

        dict1 = {}  #dictionary for all professionals
        list= [] #developers available for hire
        accountant = Accountants("John", "Ganda", "123456", 12 / 12 / 1978, 12 / 10 / 2021, 789877665, 50000, "Auditing",
                                 "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        krankodesigns_acc = 100000000000
        ahmed =Developers("Ahmed","Mohamed","123456", "12/12/2001","12/11/2021","0784803833",2000,"Data science",2,"yes",1000,"www.link.com")
        #dict[Developers.unique_code] = ahmed
        dict1[Developers.unique_code] = ahmed
        dictionary[Developers.unique_code] = ahmed
        list.append(ahmed)
        result = accountant.hiring_developer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(accountant.acc,49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(ahmed.acc,2800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)

    def test_hiring_architect(self):
        dictionary = {}#dictionary for all architects
        #dict = {}
        dict1 = {}#dictionary for all professionals
        list = [] #architects available for hire
        accountant = Accountants("John", "Ganda", "123456", 12 / 12 / 1978, 12 / 10 / 2021, 789877665, 50000, "Auditing",
                                 "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        krankodesigns_acc = 100000000000
        Hussein = Architects("Jeremiah","Ater","1997",12/12/2001,12/12/2015,7343448,50000,"skyscraper design","yes",8,1000,"rtyhgfdewsag","KEG 12345/LM")
        # dict[Architects.unique_code] = ahmed
        dict1[Architects.unique_code] = Hussein
        dictionary[Architects.unique_code] = Hussein
        list.append(Hussein)
        result =accountant.hiring_architect(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(accountant.acc, 49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(Hussein.acc,50800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)

    def test_hiring_designer(self):
        dictionary = {}#dictionary for all designers
        #dict = {}
        dict1 = {}#dictionary for all professionals
        list = []#designers available for hire
        accountant = accountant = Accountants("John", "Ganda", "123456", 12 / 12 / 1978, 12 / 10 / 2021, 789877665, 2000, "Auditing",
                                 "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        krankodesigns_acc = 100000000000
        designer1 = Designers("Gilbert","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        # dict[Architects.unique_code] = ahmed
        dict1[Designers.unique_code] = designer1
        dictionary[Designers.unique_code] = designer1
        list.append(designer1)
        result = accountant.hiring_designer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
    def test_hiring_accountant(self):
        dictionary = {}#dictionary for all accountants
        #dict = {}
        dict1 = {}#dictionary for all professionals
        list = []#accountants available for hire
        accountant1 = Accountants("John", "Ganda", "123456", 12 / 12 / 1978, 12 / 10 / 2021, 789877665, 50000, "Auditing",
                                 "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        krankodesigns_acc = 100000000000
        accountant = Accountants("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Auditor", "yes", 7, 1000, "ghjoiuytgfredsw","KBG/345tr/ICPAk")
        # dict[Architects.unique_code] = ahmed
        dict1[Accountants.unique_code] = accountant
        dictionary[Accountants.unique_code] = accountant
        list.append(accountant)
        result = accountant1.hiring_accountant(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(accountant1.acc,49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(accountant .acc,50800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)

    def test_take_a_loan(self):
        accountant1 = Accountants("John", "Ganda", "123456", "12/12/1978", "12/10/2021", 789877665, 2000,
                                  "Auditing",
                                  "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        krankodesigns_acc = 100000000000
        result=accountant1.take_a_loan(krankodesigns_acc)
        self.assertTrue(result, True)
    def test_take_leave(self):
        accountant1 = Accountants("John", "Ganda", "123456", "12/12/1978", "12 / 10 / 2021", 789877665, 2000,
                                  "Auditing",
                                   4,"yes", 2000, "www.mylink.com", "KE_gov_1902")
        result=accountant1.take_leave()
        self.assertTrue(result, True)
        self.assertEqual(accountant1.availability, "no")  # Checking whether the availability has been changed to no
    def test_resume_from_leave(self):
        accountant1 = Accountants("John", "Ganda", "123456", "12 / 12 / 1978", "12 / 10 / 2021", 789877665, 2000,
                                  "Auditing",
                                  4,"yes", 2000, "www.mylink.com", "KE_gov_1902")
        result=accountant1.resume_from_leave()
        self.assertTrue(result, True)
        self.assertEqual(accountant1.availability, "yes")  # Checking whether the availability has been changed to yes
    def test_terminate_contract(self):
        dict={}
        accountant1 = Accountants("John", "Ganda", "123456", "12 / 12 / 1978", "12 / 10 / 2021", 789877665, 2000,
                                  "Auditing",
                                  "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        accountant2 = Accountants("Johns", "Gandia", "123456", "12 / 12 / 1978", "12 / 10 / 2021", 789877665, 2000,
                                  "Auditing",
                                  "yes", 4, 2000, "www.mylink.com", "KE_gov_1902")
        dict[Accountants.unique_code]=accountant2
        result=accountant1.terminate_contract(dict)
        self.assertTrue(result,True)










#<------------------------------------------------------------------------------------------------------------->
class TestArchitects(unittest.TestCase):
    def test_calulate_tax(self):
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 1234567,
                             "skyscraper design", "yes", 8, 1234567, "rtyhgfdewsag", "KEG 12345/LM")
        result = Hussein.calculate_tax()
        self.assertTrue(result, True)

    def test_buying_software(self):
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 1234567,
                             "skyscraper design", "yes", 8, 1234567, "rtyhgfdewsag", "KEG 12345/LM")
        softwares_available = {"1": ["Drafano systems", 8000000], "2": ["kilemi accounting software", 20000000],
                               "3": ["android python installer", 23456700]}
        krankodesigns_acc = 100000000000

        result = Hussein.buying_software(softwares_available,krankodesigns_acc)
        self.assertTrue(result, True)
    def test_hiring_developer(self):
        dictionary={}#dictionary for all developers

        dict1 = {}#dictionary for all professionals
        list= []#A list with developers available for hire
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 50000,
                             "skyscraper design", "yes", 8, 50000, "rtyhgfdewsag", "KEG 12345/LM")
        krankodesigns_acc = 100000000000
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12/12/2001,12/12/2012,345678965,50000,"frontend",7,"yes",1000,"ertgghjuytf")

        dict1[Developers.unique_code] = ahmed
        dictionary[Developers.unique_code] = ahmed
        list.append(ahmed)
        result = Hussein.hiring_developer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(Hussein.acc, 49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(ahmed.acc, 50800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)


    def test_hiring_architect(self):
        dictionary = {}#dictionary for all architects

        dict1 = {}#dictionary for all professionals
        list = []#A list with architects available for hire
        Hussein1 = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 50000,
                             "skyscraper design", "yes", 8, 50000, "rtyhgfdewsag", "KEG 12345/LM")
        krankodesigns_acc = 100000000000
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 50000,
                             "skyscraper design", "yes", 8, 1000, "rtyhgfdewsag", "KEG 12345/LM")
        # dict[Architects.unique_code] = ahmed
        dict1[Architects.unique_code] = Hussein
        dictionary[Architects.unique_code] = Hussein
        list.append(Hussein)
        result =Hussein1.hiring_architect(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(Hussein1.acc, 49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(Hussein.acc, 50800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)

    def test_hiring_designer(self):
        dictionary = {}#dictionary for all designers

        dict1 = {}#dictionary for all professionals
        list = []#A list with architects available for hire
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 1234567,
                             "skyscraper design", "yes", 8, 1234567, "rtyhgfdewsag", "KEG 12345/LM")
        krankodesigns_acc = 100000000000
        designer1 = Designers("Gilbert","Odipo","1997",12/12/1978, 12/12/2010, 789654325,50000, "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        # dict[Architects.unique_code] = ahmed
        dict1[Designers.unique_code] = designer1
        dictionary[Designers.unique_code] = designer1
        list.append(designer1)
        result = Hussein.hiring_designer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
    def test_hiring_accountant(self):
        dictionary = {}#dictionary for all accountants

        dict1 = {}#dictionary for all professionals
        list = []#A list with accountants available for hire
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 50000, 50000,
                             "skyscraper design", "yes", 8, 50000, "rtyhgfdewsag", "KEG 12345/LM")
        krankodesigns_acc = 100000000000
        accountant = Accountants("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                             "Auditor", "yes", 7, 1000, "ghjoiuytgfredsw","KBG/345tr/ICPAk")
        # dict[Architects.unique_code] = ahmed
        dict1[Accountants.unique_code] = accountant
        dictionary[Accountants.unique_code] = accountant
        list.append(accountant)
        result = Hussein.hiring_accountant(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)
        self.assertEqual(Hussein.acc,49000)  # Checking whether the clients account balance has been reduced accordingly (80% of rate)
        self.assertEqual(accountant.acc, 50800)  # Checking whether the professional's account balance has been increased accordingly(20% of rate)

    def test_take_a_loan(self):
        Hussein = Architects("Jeremiah", "Ater", "1997", "12/12/2001", "12/12/2015", 1234567, 1234567,
                             "skyscraper design", "yes", 8, 1234567, "rtyhgfdewsag", "KEG 12345/LM")
        krankodesigns_acc = 100000000000
        result=Hussein.take_a_loan(krankodesigns_acc)
        self.assertTrue(result, True)

    def test_take_leave(self):
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 50000, 50000,
                             "skyscraper design", 8,"yes", 50000, "rtyhgfdewsag", "KEG 12345/LM")
        result = Hussein.take_leave()
        self.assertTrue(result, True)
        self.assertEqual(Hussein.availability, "no")  # Checking whether the availability has been changed to no

    def test_resume_from_leave(self):
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 50000, 50000,
                             "skyscraper design", 8,"yes", 50000, "rtyhgfdewsag", "KEG 12345/LM")
        result = Hussein.resume_from_leave()
        self.assertTrue(result, True)
        self.assertEqual(Hussein.availability, "yes")  # Checking whether the availability has been changed to no

    def test_terminate_contract(self):
        dict = {}
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 1234567,
                             "skyscraper design", "yes", 8, 1234567, "rtyhgfdewsag", "KEG 12345/LM")
        Hussein2 = Architects("Jeremiahs", "Aters", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 1234567,
                             "skyscraper design", "yes", 8, 1234567, "rtyhgfdewsag", "KEG 12345/LM")
        dict[Architects] = Hussein2
        result = Hussein.terminate_contract(dict)
        self.assertTrue(result, True)


if __name__== "__main__"  :
    unittest.main()

#<------------------------------------------------------------------------------------------------------------>
class TestDevelopers(unittest.TestCase):
    def test_calulate_tax(self):
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        result = ahmed.calculate_tax()
        self.assertTrue(result, True)

    def test_buying_software(self):
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        softwares_available = {"1": ["Drafano systems", 8000000], "2": ["kilemi accounting software", 20000000],
                               "3": ["android python installer", 23456700]}
        krankodesigns_acc = 100000000000

        result = ahmed.buying_software(softwares_available, krankodesigns_acc)
        self.assertTrue(result, True)

    def test_hiring_developer(self):
        dictionary = {}#dictionary for all developers
        # dict={}
        dict1 = {} #dictionary for all professionals
        list = [] #Developers available for hire
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 2000, "frontend",
                           8, "ertgghjuytf", 1000,"yes")
        krankodesigns_acc = 100000000000
        ahmed1 = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 50000, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        # dict[Developers.unique_code] = ahmed
        dict1[Developers.unique_code] = ahmed
        dictionary[Developers.unique_code] = ahmed
        list.append(ahmed)
        result = ahmed1.hiring_developer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)


    def test_hiring_architect(self):
        dictionary = {}#dictionary for all architects
        # dict = {}
        dict1 = {}#dictionary for all professionals
        list = []#architects available for hire
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 50000, "frontend",
                           8, "ertgghjuytf", 1000, "yes")
        krankodesigns_acc = 100000000000
        Hussein = Architects("Jeremiah", "Ater", "1997", 12 / 12 / 2001, 12 / 12 / 2015, 1234567, 50000,
                             "skyscraper design", "yes", 8, 1000, "rtyhgfdewsag", "KEG 12345/LM")
        # dict[Architects.unique_code] = ahmed
        dict1[Architects.unique_code] = Hussein
        dictionary[Architects.unique_code] = Hussein
        list.append(Hussein)
        result = ahmed.hiring_architect(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)


    def test_hiring_designer(self):
        dictionary = {}#dictionary for all designers

        dict1 = {}#dictionary for all professionals
        list = []#Designers available for hire
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        krankodesigns_acc = 100000000000
        designer1 = Designers("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                              "Graphic designer", "yes", 7, 23455, "ghjoiuytgfredsw")
        # dict[Architects.unique_code] = ahmed
        dict1[Designers.unique_code] = designer1
        dictionary[Designers.unique_code] = designer1
        list.append(designer1)
        result = ahmed.hiring_designer(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)

    def test_hiring_accountant(self):
        dictionary = {} #dictionary for all accountants
        # dict = {}
        dict1 = {}#dictionary for all professionals
        list = []#accountants available for hire
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        krankodesigns_acc = 100000000000
        accountant = Accountants("Gilbert", "Odipo", "1997", 12 / 12 / 1978, 12 / 12 / 2010, 789654325, 50000,
                                 "Auditor", "yes", 7, 23455, "ghjoiuytgfredsw", "KBG/345tr/ICPAk")
        # dict[Architects.unique_code] = ahmed
        dict1[Accountants.unique_code] = accountant
        dictionary[Accountants.unique_code] = accountant
        list.append(accountant)
        result = ahmed.hiring_accountant(dictionary, list, dict1, krankodesigns_acc)
        self.assertTrue(result, True)

    def test_take_a_loan(self):
        ahmed = Developers("Ahmed", "Mohamed", "1997", "12/12/2001", "12/12/2012", 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        krankodesigns_acc = 100000000000
        result=ahmed.take_a_loan(krankodesigns_acc)
        self.assertTrue(result, True)



    def test_take_leave(self):
        ahmed = Developers("Ahmed", "Mohamed", "1997", "12/12/2001", "12/12/2012", 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        result = ahmed.take_leave()
        self.assertTrue(result, True)

    def test_resume_from_leave(self):
        ahmed = Developers("Ahmed", "Mohamed", "1997", "12/12/2001", "12/12/2012", 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")
        result = ahmed.resume_from_leave()
        self.assertTrue(result, True)

    def test_terminate_contract(self):
        dict = {}#dictionary for all professionals
        ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 1234567, "frontend",
                           8, 123456, "ertgghjuytf", "yes")

        dict[Developers] = ahmed
        result = ahmed.terminate_contract(dict)
        self.assertTrue(result, True)

    # def test_terminate_contract(self):
    #     dict = {}
    #     ahmed = Developers("Ahmed", "Mohamed", "1997", 12 / 12 / 2001, 12 / 12 / 2012, 345678965, 1234567, "frontend",
    #                        8, 123456, "ertgghjuytf", "yes")
    #
    #     dict[Developers] = ahmed
    #     result = ahmed.terminate_contract(dict)
    #     self.assertRaises(SystemExit(1),True)


if __name__ == "__main__":
    unittest.main()


