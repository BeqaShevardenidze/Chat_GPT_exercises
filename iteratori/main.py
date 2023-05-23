import os
def Cls():
    os.system("cls")
Cls()

print("""
{1} - Создайте итератор, который возвращает все числа от 0 до заданного числа n.

{2} - Создайте итератор, который возвращает все числа Фибоначчи до заданного числа n.

{3} - Создайте итератор, который возвращает все простые числа до заданного числа n.
""")

x = input(">>>> ")

match x:
    # ///////////////////////////////////////////////////////
    case '1':
        Cls()
        class Counter:
            def __init__(self, n) -> None:
                self.n = n
                self.counter = 0

            def __iter__(self):
                return self
            
            def __next__(self):
                if self.counter != self.n:
                    self.counter += 1
                    return self.counter
                raise StopIteration

        count1 = Counter(10)
        for i in count1:
            print(i)
    # ///////////////////////////////////////////////////////
    case '2':
        Cls()
        class fibo:
            def __init__(self, num):
                self.num = num
                self.n1, self.n2 = 0, 1
                self.count = 0

            def __iter__(self):
                a, b = 0, 1
                for i in range(self.num):
                    yield a
                    a, b = b, a + b

            def __next__(self):
                raise StopIteration

        fibo1 = fibo(10)
        for i in fibo1:
            print(i)
    # ///////////////////////////////////////////////////////
    case '3':
        Cls()
        class SimpleNums:
            def __init__(self, num) -> None:
                self.num = num
                self.count = 0
                self.i = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.i == self.num:
                    raise StopIteration  
                self.i += 1
                self.count = 0
                for j in range(1,self.i+1):
                    if (self.i % j == 0):
                        self.count += 1
                        if self.count <= 2:
                            if self.i / j == 1 and self.i / 1 == self.i:
                                return self.i
                        else:
                            return self.__next__()
                            

        num1 = SimpleNums(100)
        for i in num1:
            print(i)

    case '3.1':
        Cls()
        for i in range(1,100):
            count = 0
            for j in range(1,i+1):
                if (i % j == 0):
                    result = i/j
                    count += 1
                    if count <= 2:
                        if i / j == 1 and i / 1 == i:
                            print(f"{i} / {j} = {result}        {count}")