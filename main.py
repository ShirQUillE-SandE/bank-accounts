class Bank_Account:
  def __init__(self, name):
    self.balance = 0.00
    self.name = name

  def deposit(self, amount):
    self.balance += amount
    return  

  def withdraw(self, amount):
    try:
       amount = float(amount)
       if self.balance < amount:
              return f" You do not have enough balance: {amount}"
       else:
                self.balance -= amount
                return 
  
    except exceptions:
         raise ValueError("Enter the correct amount")
          
  @staticmethod
  def transfer(from_account, to_account, amount):
    from_account.withdraw(amount)
    to_account.deposit(amount)
    return

  # def balance(self):
  #   return f"{self.balance}"

  def display(self):
        balance = round(self.balance, 2)
        return balance
    
wanjiru = Bank_Account("wanjiru")
juma = Bank_Account("juma")
linda = Bank_Account("linda")

wanjiru.deposit(152.00)
wanjiru.deposit(158.00)
wanjiru.deposit(164.00)
wanjiru.deposit(171.00)
wanjiru.deposit(178.00)
wanjiru.deposit(182.00)
wanjiru.deposit(184.00)
wanjiru.deposit(188.00)
wanjiru.withdraw(159.00)
wanjiru.withdraw(165.00)
wanjiru.withdraw(166.00)
wanjiru.withdraw(175.00)
wanjiru.withdraw(181.00)

juma.deposit(1557.17)
juma.deposit(1757.92)
juma.deposit(1757.92)
juma.withdraw(0)

linda.deposit(154.00)
linda.deposit(156.00)
linda.deposit(160.00)
linda.deposit(162.00)
linda.deposit(169.00)
linda.deposit(174.00)
(linda.deposit(180.00))

(linda.withdraw(20.00))
(linda.withdraw(167.00))
(linda.withdraw(176.00))

Bank_Account.transfer(wanjiru, linda, 218.25)
Bank_Account.transfer(wanjiru, juma, 97.50)
Bank_Account.transfer(wanjiru, linda, 246.75)
Bank_Account.transfer(wanjiru, juma, 300.00)
Bank_Account.transfer(wanjiru, linda, 500.00)
Bank_Account.transfer(wanjiru, juma, 600.00)


Bank_Account.transfer(juma, linda, 2000.00)
Bank_Account.transfer(juma, linda, 500.00)


Bank_Account.transfer(linda, juma, 2000.00)

print("wanjiru's balance is:", wanjiru.display())
print("juma's balance is:", juma.display())
print("linda's balance is:", linda.display())