class CustomerBankAccount:
    def __init__ (self, account_number, balance, customer_name, email, phone_number):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        
    def get_act_num(self):
        return self.account_number


    def set_act_num(self, account_number):
        # if logic here to change account number if its the correct length for an acct number
        pass

    def get_balance(self):
        return self.balance
        
    def get_email(self):
        return self.email    
    
    def set_email(self,email):
        self.email = email
        
    # Could definitely used edge case testing
    def change_balance(self, balance):
        print("would you like to add to your balance or transfer funds?")
        user_input = input("Please write 'transfer' or 'add funds'")
        
        if user_input == 'add funds':
            print(f"your current balance is {self.get_balance()}")
            amount = input("how much money would you like to add to your account?")
            if float(amount) > 0.00:
                self.balance = self.balance + float(amount)
                print(f"{amount} has been transfered, your new balance is {self.get_balance()}, Have a brutal day")
            else:
                print("You need money to add money")
        else :
            transfer_amount = input(f"Your current balance is {self.get_balance()}, how much money would you like to transfer?")
            if float(transfer_amount) < self.balance:
                self.balance = self.balance - float(transfer_amount)
                print(f"{transfer_amount} has been transfered, your new balance is {self.get_balance()}, Have a brutal day")
        
        
customer1 = CustomerBankAccount(
    account_number="1234567890",
    balance=1000.0,  
    customer_name="John Doe",
    email="johndoe@example.com",
    phone_number="555-1234"
)

# customer1.change_balance(25.00)
print(customer1.get_email())
customer1.set_email('lmartin@gmail.com')
print(customer1.get_email())