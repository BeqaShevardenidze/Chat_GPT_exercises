import os
def Cls():
    os.system("cls")
Cls()

print("""
{1} - Найти наибольший общий делитель (НОД) двух чисел.
{1.1} - Function + random

{2} - Проверить, является ли число простым.
{2.1} - Function

{3} - Найти сумму цифр числа.
      . У нас есть данное число, например, 12345.
      . Необходимо разложить число на отдельные цифры: 1, 2, 3, 4, 5.
      . После этого нужно просуммировать все цифры: 1 + 2 + 3 + 4 + 5 = 15.
{3.1} - Function

{4} - Проверить, является ли число палиндромом.

{5} - Проверить, является ли число совершенным (сумма всех делителей равна числу).

{6} - Вычислить факториал числа.

{7} - Найти все простые числа в диапазоне от 1 до заданного числа.

{8} - Проверить, является ли число числом Армстронга.

{9} - Проверить, является ли число совершенным квадратом (квадрат целого числа).

{10} - Проверить, является ли число числом Фибоначчи.

""")

x = input(">>>> ")
match x:
    case "1":
        Cls()
        # 15  20
        n1 = 15;    n1_list = []
        n2 = 20;    n2_list = []
        for i in range(1,n1):
            if n1 % i == 0:
                result = int(n1/i)
                n1_list.append(result)
                # print(f"{n1} / {i} = {result}")

        for i in range(1,n2):
            if n2 % i == 0:
                result = int(n2/i)
                n2_list.append(result)
                # print(f"{n2} / {i} = {result}")

        print(n1_list)
        print(n2_list)

        for num1 in n1_list:
            for num2 in n2_list:
                if(num1 == num2):
                    print(f"{num1} = {num2}")
    case '1.1':
        Cls()
        def f_two_num(num1, num2):
            n1_list = []; n2_list = []; result_list = []
            for i in range(1,num1):
                if num1 % i == 0:
                    result = int(num1/i)
                    n1_list.append(result)
            for i in range(1, num2):
                if num2 % i == 0:
                    result = int(num2/i)
                    n2_list.append(result)

            for i in n1_list:
                for j in n2_list:
                    if i == j:
                        result_list.append(i)
            return f"{result_list}"

            # return n1_list,n2_list
        
        print(f_two_num(15,20))
        print(f_two_num(15,30))

        import random
        n1 = random.randint(1,101)
        n2 = random.randint(1,101)
        print(n1," ", n2, " = ", f_two_num(n1,n2))

    case '2':
        Cls()
        n1 = 3; n1_list = []
        for i in range(1,n1 + 1):
            if n1 % i == 0:
                result = int(n1/i)
                n1_list.append(result)
                # print(f"{n1} / {i} = {result}")
        if len(n1_list) > 2:
            print("ეს ციფრი არ არის ნატურალური!")
        else:
            print("რიცხვი ნატურალურია")
    case '2.1':
        Cls()
        def f_prime_num(n1):
            temp = 0
            for i in range(1,n1+1):
                if n1 % i == 0:
                    temp+=1
            if temp > 2:
                return f"რიცხვი {n1} არ არის ნატურალური!" 
            else:
                return f"რიცხვი {n1} ნატურალურია"
            
        for i in range(1,100):
            print(f_prime_num(i))

    case '3':
        Cls()
        num1 = 12345
        n1 = int(num1/10000)
        n2 = int((num1/1000)%10)
        n3 = int((num1/100)%10)
        n4 = int((num1/10)%10)
        n5 = int(num1%10)
        
        result = n1 + n2 + n3 + n4 + n5
        print(result)
    case '3.1':
        Cls()
        def func(num1):
            temp = 0
            for i in str(num1):
                temp += int(i)
            return temp
        
        print(func(843942))

    case '4':
        Cls()
        def func(n1):
            temp = ""
            for i in reversed(str(n1)):
                temp += i
            if n1 == int(temp):
                return f"ციფრი {n1} პალიდრომია"
            else:
                return f"ციფრი {n1} პალიდრომი არ არის"
        print(func(123))
        print(func(121))