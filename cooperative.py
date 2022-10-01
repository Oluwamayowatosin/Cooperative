import mysql.connector
import sys
import random
import time


class ATO_Class:
    def __init__(self):
        self.connection()
        self.option()

    def connection(self):
        self.mycon = mysql.connector.connect(host="localhost", user="root", passwd="", database="COOPERATIVE_MANAGEMENT" )
        self.mycursor = self.mycon.cursor()
        # self.mycursor.execute("CREATE DATABASE COOPERATIVE_MANAGEMENT")
        # self.mycursor.execute("CREATE TABLE Bolton_Branch (Member_Id INT(4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR(40), Gender VARCHAR(7), Address VARCHAR(50), Phone_No VARCHAR(11), UserName VARCHAR(20) UNIQUE KEY, Occupation VARCHAR(20), Savings INT(10), Unique_Id VARCHAR(4) UNIQUE KEY, Loan INT(10), Interest INT(10), Loan_Breakdown INT(10), Due_Interest INT(10)) ")

  
    def option(self):
        print("""                   Welcome to ATO Co_operative Network                                 
                               Boltin's United Kingdom
              1. First Timer
              2. Regular
              3. Quit""")
        self.userInput = input("Enter your option to countinue: ")
        if self.userInput == "1":
            self.FirstTimer()
        elif self.userInput == "2":
            self.Regular()
        elif self.userInput =="3":    
            self.Quit()
        else:
            print("Invalid input")
            self.option() 
    
    
    def FirstTimer(self):
        self.user1 = input("As a first timer, you are expected to pay registration fee of #10000 (Type that in) \n>>  ")
        if self.user1 == "10000":  
                time.sleep(2)
                print("Loading.................")
                print("we would like you to reply to this notification with 'OK' to know that you agree to all terms and conditions")
                self.Notification()
                self.user2 = input(">> ")
                if self.user2.lower() == "ok":
                    time.sleep(2)
                    self.Register()
                else:
                    print("Please type in 'OK' to be sure you agreed to the terms and conditions")
                    self.Notification()
        else:
            print("You are expected to pay the sum of #10000 as your registration fee")
            self.FirstTimer()
            
    def Notification(self):
        print("""
                Here are the few notifications of ATO Co_operative Network

                1. Every First Wednesday of the Month at 12pm will be the time of the meeting

                2. Your Savings at every meeting is compulsory and which the minimum amount is #5000

                3. You have to Save continously for good six(6) month before you are Eligible to get a loan
        """)    
        
    def Register(self):    
        self.connection()
        print("NOTE THAT YOU ARE EXPECTED TO BE ABOVE 18 BEFORE YOU CAN JOIN THIS CO_OPERATIVE NETWORK \n Now please provide your details")
        self.UserAge = input("Your AGE please : ")
        if self.UserAge >= "18":
            self.contact = input("PHONE NO. : ")
            self.Register()
            
            detail = ["fName", "gender", "address", "phoneNo", "user_Name", "occupation"]
            request = ["Full name", "Gender", "Address", "Phone No.", "User Name", "Occupation"]
            for i in range(6):
                detail[i] = input("Enter your "+request[i]+"  ")
            Unique_Id = "01"+str(random.randint(10000000, 90000000))
            myquery = """INSERT INTO bolton_branch (Full_Name, Gender, Address, Phone_No,
                    UserName, Unique_Id, Occupation) VALUE(%s, %s, %s, %s, %s, %s, %s)"""
            val = (detail[0], detail[1], detail[2], detail[3], detail[4],  Unique_Id, detail[5] )
            self.cursor = self.mycon.cursor()
            self.mycursor.execute(myquery, val)
            self.mycon.commit()
            self.mycon.close()
            print ("Please wait your Registration is being processing")
            time.sleep(3)
            print(self.mycursor.rowcount, """registration is successful 
                Your Unique Id is """+Unique_Id)
            print("You are now a full Member of ATO Co_operative Network. You can now proceed to the main room\n PLEASE DO NOT FORGET YOUR UNIQUE ID")
            self.option()
        else:
            time.sleep(3)
            print("You are an underage so... bye")
            sys.exit()     
   
        
    def Regular(self):
        print("""Welcome to today's co_operative meeting
            What would you like to do,,,, TAKE NOTE!!! Your Savings first""")   
        choose = ["1. Save", "2. Loan", "3. Check Savings Balance", "4. Pay loan back", "5. Members", "6. Notification for the day", "7. Check co_operative Info ", "8. Customer Details", "9. Close Account", "10. Quit"]
        self.user_name = input("Enter your user name: ")
        self.unique_Id = input("Enter your unique Id: ") 
        query = "SELECT * FROM bolton_branch WHERE UserName=%s AND Unique_Id=%s"
        val = (self.user_name, self.unique_Id)  
        self.mycursor.execute(query, val)
        self.record = self.mycursor.fetchall()
        if self.record:
            print("You are welcome dear "+self.record[0][1]+" "+self.record[0][2])
            for val in choose:
                print(val)
            self.userInput = input("Enter an option to continue: ")
            if self.userInput == "1":
                time.sleep(2)
                self.Savings()
            elif self.userInput == "2":
                time.sleep(2)
                self.Loan()
            elif self.userInput == "3":
                time.sleep(2)
                self.CheckBalance()
            elif self.userInput == "4":
                time.sleep(2)
                self.PayBack()
            elif self.userInput == "5":
                time.sleep(2)
                self.Members()
            elif self.userInput == "6":
                time.sleep(2)
                self.Notification4Today()
            elif self.userInput == "7":
                time.sleep(2)
                self.Notification()
                time.sleep(3)
                self.Regular()
            elif self.userInput == "8":
                time.sleep(2)
                self.MemberDetails()
            elif self.userInput == "9":
                time.sleep(2)
                self.CloseAccount()
            elif self.userInput == "10":
                time.sleep(2)       
                sys.exit()
            else:
                print("Input the right string")
                self.Regular()
        else:
            print("Invalid Details. please go and register first to continue")
            self.Regular()
            self.option()
            


    def Savings(self):
        Query = "SELECT Savings FROM bolton_branch WHERE UserName=%s AND Unique_Id=%s"
        Val = (self.user_name, self.unique_Id) 
        self.mycursor.execute(Query, Val)
        self.savingsBal = self.mycursor.fetchone() 
        for self.mySavings in self.savingsBal:
            pass       
        self.inputSavings = int(input("How much would you like to save today\n NOTE!!! nothing less than #5000 \n>> "))
        self.amount = "5000"
        if self.inputSavings >= int(self.amount):
            self.newSavings = int(self.savingsBal[0] + self.inputSavings)
            balQuery = "UPDATE bolton_branch SET Savings=%s WHERE Unique_Id=%s"
            unique_Id = (self.newSavings, self.unique_Id)
            self.mycursor.execute(balQuery, unique_Id)
            self.mycon.commit()
            time.sleep(2)
            print("Successfully saved " + str(self.inputSavings) + "\n THAT'S IT, now you can proceed to do any other thing")
            self.Regular()
        else:
            print("You are supposed to input an amount equals to or greater than #5000")
            self.Savings() 
        self.option()
        

    def CheckBalance(self):
        query = "SELECT Savings FROM bolton_branch WHERE  Unique_Id=%s"
        UserName = (self.unique_Id,)
        self.mycursor.execute(query, UserName)
        self.Savingsbalance = self.mycursor.fetchone()
        print ("processing")
        time.sleep(3)
        print("Dear Cusomer; \n  Your current Savings Balance is: #" +str(self.Savingsbalance[0]))
        self.Regular()
        self.CheckBalance()
        self.option()
        
   
    def Members(self):
        print("")
        print("This are list of our members, you can get to know more about yourselves here")
        memberQuery = "SELECT Full_Name FROM bolton_branch"
        self.mycursor.execute(memberQuery)
        myreg = self.mycursor.fetchall()
        for members in myreg:
            print(members)
        self.Regular() 
        self.option()   
     

    def Loan(self):
        self.unique_Id = input("ENter your Unique Id: ")
        loanQuery = "SELECT Loan FROM bolton_branch WHERE Unique_Id=%s"
        loanVal = (self.unique_Id,)
        self.mycursor.execute(loanQuery, loanVal)
        myreg1 = self.mycursor.fetchone()
        for self.loanBalance in myreg1:
            pass
        print("Loan Eligibility Status.......................")
        Savebalance = int(input("how much do you in your savings? "))
        if Savebalance >= 60000:
            # query = "SELECT Savings=%s FROM bolton_branch WHERE Unique_Id=%s"
            # account = (self.unique_Id,)
            # self.mycursor.execute(query, account)
            # self.balance = self.mycursor.fetchone()
            name = input("What is your UserName? ")
            month_spt = str(input("How many month have you been cooperating with us? "))
            if month_spt >= "6":
                print("Congratulations "+name+", you are eligible to receive a loan. ")
            elif month_spt < "6":
                print("Unfortunately, you are can not receive a loan at this time. ")
                self.option()
            else:
                print("An error has occured with the software, please try again")
        elif Savebalance < 60000:
            print("Unfortunately, you are can not receive a loan at this time. ")
            self.option() 
        else:
            print("An error has occured with the software, please try again")
        print("""
        ABOUT THE INTEREST
                
            - NOTE that on every pay back, there's an interest of 5%

            - NOTE that this loan has to be paid within 6 month of collecting the loan, which means you have to return the loans in 6 different times OR LESS, as you wish
        """)
        time.sleep(2)
        self.loanMoney = float(input("How much would you like to get as your loan; \n>> "))
        time.sleep(1)
        if self.loanBalance == 0:
            balQuery1 = "UPDATE bolton_branch SET Loan=%s WHERE Unique_Id=%s"
            valQuery1 = (self.loanMoney, self.unique_Id)
            self.mycursor.execute(balQuery1, valQuery1)
            self.mycon.commit()
            print("PLEASE TAKE YOUR LOAN \n" + str(self.loanMoney))
            time.sleep(2)
            print("This is the breakdown of your Loan Pay back")
            self.breakdown = float(self.loanMoney / 6)
            self.interest = float((5 / 100) * self.loanMoney)
            self.totalInterest = float(self.interest * 6)
            self.total = float(self.breakdown + self.interest)
            time.sleep(2)
            balQuery2 = "UPDATE bolton_branch SET Loan_Breakdown=%s, Due_Interest=%s, Total_Interest=%s WHERE Unique_Id=%s"
            valQuery2 = (self.breakdown, self.interest, self.totalInterest, self.unique_Id)
            self.mycursor.execute(balQuery2, valQuery2)
            self.mycon.commit()
            print("AMOUNT COLLECTED; " + str(self.loanMoney))
            print("AMOUNT TO BE RETURNED AT EACH MEETING; " + str(self.breakdown))
            print("INTEREST OF 5%; " + str(self.interest))
            print("INTEREST plus AMOUNT TO BE RETURNED; " + str(self.total))
            print("SO YOUR PAYBACK HAS TO BE " + str(self.total) + " EIGHT DIFFERENT TIME OR LESS, AS YOU WISH")
            time.sleep(3)
            self.Regular()
        else:
            print("You have an unpaid Loan of " + str(self.loanBalance))
            self.Regular() 
        self.option()
        
    def PayBack(self):
        payBackQuery = "SELECT Loan FROM bolton_branch WHERE Unique_Id=%s"
        payBackVal = (self.unique_Id,)
        self.mycursor.execute(payBackQuery, payBackVal)
        myreg3 = self.mycursor.fetchone()
        for self.payBackBalance in myreg3:
            pass
        self.userPay = float(input("WELCOME;  \n Input your payback.. NOTE - just the real money alone not with interest \n> "))
        payBackQuery2 = "SELECT loan_Breakdown FROM bolton_branch WHERE unique_ID=%s"
        payBackVal2 = (self.unique_Id,)
        self.mycursor.execute(payBackQuery2, payBackVal2)
        myreg4 = self.mycursor.fetchone()
        for self.payBreakdown in myreg4:
            pass
        if self.userPay >= self.payBreakdown:
            print("Please wait while we proccess your request...")
            time.sleep(3)
            self.newBal = float(self.payBackBalance - self.userPay)
            balQuery = "UPDATE bolton_branch SET Loan=%s WHERE Unique_Id=%s"
            valQuery = (self.newBal, self.unique_Id)
            self.mycursor.execute(balQuery, valQuery)
            self.mycon.commit()
            print("Payment was Successful")
            time.sleep(2)        
            self.InterestPay()
        else:
            print("This is not up to your normal breakdown payment per month \n This is your breakdown payment " + str(self.payBreakdown))
            self.PayBack()

    def InterestPay(self):
        payIntQuery = "SELECT Due_Interest FROM bolton_branch WHERE Unique_Id=%s"
        payIntVal = (self.unique_Id,)
        self.mycursor.execute(payIntQuery, payIntVal)
        myreg5 = self.mycursor.fetchone()
        for self.dueInterest in myreg5:
            pass
        self.userInterest = float(input("Now your interest: "))
        payBackQuery3 = "SELECT Total_Interest FROM bolton_branch WHERE Unique_Id=%s"
        payBackVal3 = (self.unique_Id,)
        self.mycursor.execute(payBackQuery3, payBackVal3)
        myreg6 = self.mycursor.fetchone()
        for self.complanyInt in myreg6:
            pass
        if self.userInterest == self.dueInterest:
            print("Please wait while we proccess your request...")
            time.sleep(3)
            self.payInterest = float(self.complanyInt - self.userInterest)
            interestQuery = "UPDATE bolton_branch SET Total_Interest=%s WHERE Unique_Id=%s"
            interestVal = (self.payInterest, self.unique_Id)
            self.mycursor.execute(interestQuery, interestVal)
            self.mycon.commit()
            print("Payment of interest was Successful")
            time.sleep(3)
            self.Regular()
        else:
            print("That is not the right amount for the interest \n The normal interest that should be paid back is "+ str(self.dueInterest))
            self.InterestPay()
                
    def MemberDetails(self):
            self.unique_Id = input("Enter your unique ID: ")
            query = "SELECT * FROM bolton_branch WHERE Unique_Id=%s"
            account = (self.unique_Id,)
            self.mycursor.execute(query, account)
            result = self.mycursor.fetchone()
            for i in result:
                print(i, end=" ")
            self.option() 
            
    def CloseAccount(self):
            self.unique_Id = input("Enter your unique ID: ")
            query= "DELETE FROM bolton_branch WHERE Unique_Id=%s"
            account = (self.unique_Id,)
            self.mycursor.execute(query, account)
            self.mycon.commit()
            print("Account Data deleted Successfully....")
            self.option() 
           
    def Notification4Today(self):
        print("""
        There's nothing much for today, Just make sure
            - You pay your savings
            - Return due loan &
            - Invite others
        """)   
        time.sleep(3)
        self.Regular() 
        self.option()     
           
    def Quit(self):
        self.mycon.close()
        sys.exit()

Cooperative = ATO_Class()

