class Account:
    def __init__(self, ID):
        self.ID = ID
        self.currentBalance = 500
        self.withdraw = 0
        self.deposit = 0

    def getCurrentBal(self):
        return self.currentBalance

    def setWithdraw(self, amount):
        self.currentBalance-=amount

    def setDeposit(self, amount):
        self.currentBalance+=amount

# Create a list of Account objects
listOfAccounts = []
for x in range(10): listOfAccounts.append(Account(x))

# Prompts user to enter ID
userID = int(input('Enter your ID: '))

# Function to determine if user id is valid
def isValidId(UserID, lst):
    newLst = []
    for i in lst: newLst.append(i.ID)
    return UserID in newLst

# Function to return user index
def getUser(UserID, lst):
    for i in lst:
        if UserID == i.ID:
            return lst.index(i)

# Prompts user to reenter ID if invalid ID Entered
while not isValidId(userID, listOfAccounts):
    userID = int(input('Invalid ID number try again: '))

# Gives user a menu of options
while isValidId(userID, listOfAccounts):
    menuOptions = int(input('Press 1 to view current balance\nPress 2 to withdraw money\nPress 3 to deposit money\n'
                            'Press 4 to exit main menu\n: '))
    if menuOptions == 4:
        break
    elif menuOptions == 1:
        print(listOfAccounts[getUser(userID, listOfAccounts)].currentBalance)
    elif menuOptions == 2:
        with_draw = int(input('How much do you want to withdraw: '))
        listOfAccounts[getUser(userID, listOfAccounts)].setWithdraw(with_draw)
    elif menuOptions == 3:
        deposit_ = int(input('How much do you want to deposit: '))
        listOfAccounts[getUser(userID, listOfAccounts)].setDeposit(deposit_)