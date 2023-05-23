import os
def Cls():
    os.system("cls")
Cls()

print("""
{1} - Создайте класс Bank, который имеет атрибуты name и branches. Реализуйте методы add_branch() и remove_branch(), которые добавляют и удаляют филиалы банка.

{2} - Создайте класс Library, который имеет атрибуты name и books. Реализуйте методы add_book() и remove_book(), которые добавляют и удаляют книги из библиотеки.

{3} - Создайте класс BankAccount, который имеет атрибуты account_number, balance и owner. Реализуйте метод deposit(amount) для внесения средств на счет и метод withdraw(amount) для снятия средств со счета.


""")

x = input(">>>> ")
match x:
    # //////////////////////////////////////////////////
    case '1':
        Cls()
        class Bank:
            def __init__(self, name,) -> None:
                self.name = name
                self.branches = []

            def add_branche(self,temp):
                self.branches.append(temp)
            
            def remove_branch(self, temp):
                if temp in self.branches:
                    self.branches.remove(temp)
                else:
                    print("შენი ჩაწერილი ფილიალი არ არის შეყვენილი")


        bank1 = Bank("TBC")
        bank1.add_branche("varketili")
        bank1.add_branche("samgori")
        bank1.add_branche("isani")
        print(bank1.branches)

        bank1.remove_branch("isani")
        print(bank1.branches)
    # //////////////////////////////////////////////////
    case '2':
        Cls()
        class Library:
            def __init__(self, name,) -> None:
                self.name = name
                self.books = []

            def add_book(self, temp):
                self.books.append(temp)

            def remove_book(self, temp):
                if temp in self.books:
                    self.books.remove(temp)
                else:
                    print("Nop")

        library1 = Library("national")
        library1.add_book("Harry Potter")
        library1.add_book("Cosmos")
        print(library1.books)

        library1.remove_book("Cosmos")
        print(library1.books)
    # //////////////////////////////////////////////////
    case "3":
        Cls()
        class BanckAccount:
            def __init__(self, account_number, balance, owner) -> None:
                self.account_number = account_number
                self.balance = balance
                self.owner = owner

            def deposite(self, amount):
                self.balance += amount

            def withdraw(self, amount):
                if self.balance >= amount:
                    self.balance -= amount
                else:
                    print("თქვენ არ გაქვთ საკმარისი თანხა:")

        bankAccount1 = BanckAccount(15578, 10, "beqa")
        print(bankAccount1.account_number)
        print(bankAccount1.balance,"$")
        print(bankAccount1.owner,'\n')

        bankAccount1.deposite(700)
        print(bankAccount1.account_number)
        print(bankAccount1.balance,"$")
        print(bankAccount1.owner,'\n')

        bankAccount1.withdraw(800)
        print(bankAccount1.account_number)
        print(bankAccount1.balance,"$")
        print(bankAccount1.owner,'\n')