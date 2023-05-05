import os
def Cls():
    os.system("cls")
Cls()

print("""
======================Menu======================
{1} - Создайте класс Person, который имеет атрибуты name и age. Создайте объект класса и выведите значения атрибутов

{2} - Создайте класс Rectangle, который имеет атрибуты width и height. Реализуйте метод area(), который вычисляет площадь прямоугольника.

{3} - Создайте класс BankAccount, который имеет атрибуты account_number и balance. Реализуйте методы deposit(amount) и withdraw(amount), которые изменяют баланс счета.

{4} - Создайте класс Car, который имеет атрибуты brand, model и year. Реализуйте метод info(), который выводит информацию о машине.

{5} - Создайте класс Dog, который имеет атрибуты name и age. Реализуйте метод bark(), который выводит сообщение "Woof!".

{6} - Создайте класс Circle, который имеет атрибут radius. Реализуйте метод area(), который вычисляет площадь окружности.

{7} - Создайте класс Student, который имеет атрибуты name, grade и score. Реализуйте метод pass_exam(), который изменяет оценку студента на основе его результатов.

{8} - Создайте класс Book, который имеет атрибуты title, author и year. Реализуйте метод info(), который выводит информацию о книге.

{9} - Создайте класс Triangle, который имеет атрибуты side1, side2 и side3. Реализуйте метод is_equilateral(), который проверяет, является ли треугольник равносторонним.

{10} - Создайте класс Employee, который имеет атрибуты name, position и salary. Реализуйте метод calculate_bonus(), который вычисляет бонус сотрудника на основе его должности и зарплаты.

""")

x = input(">>>> ")
match x:
# //////////////////////////////////////////////
    case '1':
        Cls()
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __str__(self):
                return str(self.name) + " " + str(self.age)

        person1 = Person("sandro", 20)
        print(person1)
# //////////////////////////////////////////////
    case '2':
        Cls()
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height
            
        rectangle1 = Rectangle(10, 20)
        print(rectangle1.area())
# //////////////////////////////////////////////
    case '3':
        Cls()
        class BankAccount:
            def __init__(self, account_number, balance):
                self.account_number = account_number
                self.balance = balance

            def deposit(self,amount):
                self.balance += amount
                return f"It is your deposited amount {self.balance}"
            
            def withdraw(self, amount):
                if amount > self.balance:
                    return "There is not enough money in your balance"
                elif amount <= self.balance:
                    self.balance -= amount
                    return f"Your deposit is {self.balance}"
            
            def __str__(self) -> str:
                return f"Account = {self.account_number}:  Balance = {str(self.balance)}"
            
        account1 = BankAccount('123123', 0)
        print(account1.deposit(50))
        print(account1, "\n")
        print(account1.withdraw(20))
        print(account1, "\n")
        print(account1.withdraw(30))
        print(account1, "\n")
        print(account1.withdraw(10))
        print(account1, "\n")
# //////////////////////////////////////////////
    case '4':
        Cls()
        class Car:
            def __init__(self, brand, model, year) -> None:
                self.brand = brand
                self.model = model
                self.year = year

            def info(self):
                return f"""
                brand = {self.brand}
                model = {self.model}
                year = {self.year}
                """
            
        car1 = Car("Tesla", "Model X", 2015)

        print(car1.info())
# //////////////////////////////////////////////
    case '5':
        Cls()
        class Dog:
            def __init__(self, name, age) -> None:
                self.name = name
                self.age = age

            def bark(self):
                print("Woof")

        dog1 = Dog("jeka", 2)
        dog1.bark()
# //////////////////////////////////////////////
    case '6':
        Cls()
        class Circle:
            def __init__(self, radius) -> None:
                self.radius = radius

            def area(self):
                result = 3.14 * (self.radius ** 2)
                return result

        circle1 = Circle(20)
        print(circle1.area())
# //////////////////////////////////////////////
    case '7':
        Cls()
        class Student:
            def __init__(self, name, grade, score) -> None:
                self.name = name
                self.grade = grade
                self.score = score
            
            def pass_exam(self):
                temp = int(input(f"input score {self.name} >>>> "))
                self.score = temp
                if self.score >= 60:
                    return f"{self.name} Passed"
                else:
                    return f"{self.name} not passed"

        studen1 = Student("gio", "lala", 60)
        print(studen1.pass_exam())
# //////////////////////////////////////////////
    case '8':
        Cls()
        class Book:
            def __init__(self, title, author, year) -> None:
                self.title = title
                self.author =  author
                self.year = year

            def info(self):
                return f"title = {self.title}\nauthor = {self.author}\nyear = {self.year}"
            
        book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
        print(book1.info())
# //////////////////////////////////////////////
    case '9':
        Cls()
        class Triangle:
            def __init__(self, side1, side2, side3) -> None:
                self.side1 = side1 
                self.side2 = side2 
                self.side3 = side3

            def is_equilateral(self):
                if self.side1 == self.side2 and self.side2 == self.side3 and self.side1 == self.side3:
                    return "Equal"
                else:
                    return "Not Equal"
                
        triangle1 = Triangle(10,10,10)
        triangle2 = Triangle(5,6,7)
        print(triangle1.is_equilateral())
        print(triangle2.is_equilateral())
# //////////////////////////////////////////////
    case '10':
        Cls()
        class Employee:
            def __init__(self, name, position, salary) -> None:
                self.name = name
                self.position = position
                self.salary = salary

            def calculate_bonus(self):
                if self.position == "junior":
                    bonus = 2000
                    self.salary += bonus
                elif self.position == "middle":
                    bonus = 4000
                    self.salary += bonus
                elif self.position == "senior":
                    bonus = 6000
                    self.salary += bonus

        programer1 = Employee("zaza", "junior", 2000)
        programer2 = Employee("gio", "middle", 4000)
        programer3 = Employee("lela", "senior", 6000)

        programer1.calculate_bonus()
        print(programer1.salary)
        programer2.calculate_bonus()
        print(programer2.salary)
        programer3.calculate_bonus()
        print(programer3.salary)