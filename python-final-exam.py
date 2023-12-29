class User:
    def_account_num=1010
    def __init__(self,name,email,account_type,password,address) -> None:
        self.name=name
        self.email=email
        self.account_type=account_type
        self.password=password
        self.address=address
        self.balance=0
        self.account_number=User.def_account_num
        User.def_account_num+=1
        self.transactions=[]
        self.count_loan=1

    def Deposit(self,amount):
        if amount>0:
            self.balance+=amount
            transation=f'Deposit Amount: {amount}'
            self.transactions.append(transation)
            print(f'You Are Deposited: {amount}')
        else:
            print('Please Deposti More then: 00')
    
    def Withdraw_amount(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f'Your Withdraw Amount is: {amount}')
            print(f'Now Current Balance is: {self.balance}')
            transation=f'Withdraw Amount: {amount}'
            self.transactions.append(transation)
        else:
            print('Withdrawal amount exceeded')

    def Check_balance(self):
        print(f'Available Balance is: {self.balance}')

    def Transation_history(self):
        print('---TRANSATION HISTORY---')
        for transation in self.transactions:
            print(transation)
    
    def Take_loan(self,amount):
        if self.count_loan<2:
            self.balance+=amount
            transation=f'Loan: {amount}'
            self.transactions.append(transation)
            self.count_loan+=1
            print(f'Receive Loan: {amount} And Now Your Available Balance is: {self.balance}')
        else:
            print('You have already taken loan 2 times, So now you can not take loan')

    def Transfer_money(self,recipient_account,amount):
        if self.balance>amount:
            recipient_account.Deposit(amount)
            self.balance-=amount
            transation=f'Transferred {amount} to Account: {recipient_account.account_number}'
            self.transactions.append(transation)
            print(f'Transferred Money: {amount}, to Account {recipient_account.account_number}')
            print(f'Now Current balance is: {self.balance}')
        else:
            print('Account does not exist')

   

class Admin:
    def __init__(self) -> None:
        self.users=[]

    def create_user_account(self,name,email,account_type,password,address):
        user=User(name,email,account_type,password,address)
        self.users.append(user)

    def delete_account(self,account_num):
        for user in self.users:
            if user.account_number == account_num:
                self.users.remove(user)
                print('Account Has Been Deleted')
                return
            
        print('Account Number is Wrong. Please provide the right Account Number')
    
    def users_account_list(self):
        print('---Account List---')
        for user in self.users:
            print(f'User Name: {user.name} And Account Number: {user.account_number}')


    def Total_bank_balance(self):
        total=sum(user.balance for user in self.users)
        print(f'Total available balance of the bank: {total}')

    def Total_loan_amount(self):
        total_loan=sum(user.balance for user in self.users if user.count_loan)
        print(f'Total loan amount: {total_loan}')

    def loan_feature(self,loan):
        if loan:
            self.loanFeature=True
            print('Loan Feature is Now Enable')
        else:
            print('Loan Feature is not Enable')


    def admin_interface(self):
        while True:
            print('---Admin Menu----')
            print('Enter 1 to Create a user account: ')
            print('Enter 2 to Delete a user account: ')
            print('Enter 3 to View all user account List: ')
            print('Enter 4 to Check the total available balance of the bank: ')
            print('Enter 5 to Check the total loan Amount: ')
            print('Enter 6 loan feature of the bank on/off: ')
            print('Enter 7 to log out as admin: ')


            choice=int(input('Choice then Menu Number: '))

            if choice==1:
                name=input('Enter the User Name: ')
                email=input('Enter your Email: ')
                password=input('Enter your Password: ')
                account_type=input('Enter Your Account Type Savings/Student: ')
                address=input('Enter your Address: ')
                
                new_user=User(name,email,account_type,password,address)
                self.users.append(new_user)
                print(f'User name {new_user.name}, Account Number: {new_user.account_number} created Successfully')

            elif choice==2:
                account_number_to_delete=int(input('Enter Your Account Number: '))
                self.delete_account(account_number_to_delete)
            elif choice==3:
                self.users_account_list()

            elif choice==4:
                self.Total_bank_balance()
            elif choice==5:
                self.Total_loan_amount()
            elif choice==6:
                enable_loan=input('Enable Or Disable Your Loan Feature(yes/no): ').strip().lower()
                self.loan_feature(enable_loan=='yes')
            elif choice==7:
                break
            else:
                print('Plase Input Valid Number')


def user_interface(self):
    while True:
        print('---User Menu----')
        print('Enter 1 to Deposit: ')
        print('Enter 2 to WithDraw: ')
        print('Enter 3 to Check Balance: ')
        print('Enter 4 to Transaction History: ')
        print('Enter 5 to Take Loan: ')
        print('Enter 6 to Transfer Money: ')
        print('Enter 7 to Exit: ')


        choice=int(input('Choice then Menu Number: '))

        if choice==1:
            amount=float(input('Enter Your Deposit Amount: '))
            self.Deposit(amount)
            

        elif choice==2:
            amount=float(input('Enter Your Withdraw Amount: '))
            self.Withdraw_amount(amount)
        elif choice==3:
            self.Check_balance()

        elif choice==4:
            self.Transation_history()
        elif choice==5:
            amount=float(input('Enter Your Loan Amount: '))
            self.Take_loan(amount)
        elif choice==6:
            recipient_account_number=int(input('Enter Your recipient Account Number: '))
            amount=float(input('Enter Your Amount: '))
            recipient=None
            for recipient_user in admin.users:
                recipient_user.account_number==recipient_account_number
                recipient=recipient_user
                break
            if recipient:
                user.Transfer_money(recipient,amount)
            else:
                print('Have not Enough Money')
        elif choice==7:
            break
        
  
admin=Admin()
admin.create_user_account('admin','admin@gmail.com','admin','admin123','admin')

while True:
    print('------Choose Your Login Type------')
    print('Enter 1 to Login Admin')
    print('Enter 2 to User Interface')
    print('Enter 3 to Exist')

    choice=int(input('Enter Your Choice: '))
    if choice==1:
        admin_password=input('Enter Admin Password: ')
        if admin_password=='admin123':
            print('Welcome To Admin Panel')
            admin.admin_interface()

        else:
            print('Admin Login Faild. Incorrect Password')

    elif choice==2:
        account_number=int(input('Enter Your Account Number: '))
        password=input("Enter Your Password: ")
        user=None
        for u in admin.users:
            if u.account_number==account_number and u.password==password:
                user=u
                break
        if user:
            print(f'Welcome {user.name}')
            user_interface(user)

        else:
            print('Login Failed. Incorrect Account Number Or Password')
    
    elif choice==3:
        break


        

    







            


        