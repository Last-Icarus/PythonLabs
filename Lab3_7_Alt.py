from random import random
from math import acos


class Calculator:
    def __init__(self):
        pass

    def abs(self, first):
        return abs(first)

    def fac(self, first):
        a = 0
        for i in range(first + 1):
            a += i
        return a

    def rand(self):
        return int(random() * 100 // 1)

    def acos(self, first):
        return round(acos(first), 6)

    def mainloop(self):
        while True:
            oper = str(input())
            if oper == 'random':
                print(Calc.rand())
            if oper == 'mod':
                first = int(input())
                print(Calc.abs(first))
            elif oper == 'fac':
                first = int(input())
                print(Calc.fac(first))
            elif oper == 'acos':
                first = float(input())
                print(Calc.acos(first))
            else:
                if oper == '+':
                    first = int(input())
                    second = int(input())

                    print(first + second)
                elif oper == '-':
                    first = int(input())
                    second = int(input())
                    print(first - second)

                elif oper == '*':
                    first = int(input())
                    second = int(input())

                    print(first * second)
                elif oper == '/':
                    first = int(input())
                    second = int(input())

                    print(first / second)

                elif oper == 'pow':
                    first = int(input())
                    second = int(input())
                    print(pow(first, second))

                else:
                    print('Введена неверная операнда, повторите ввод')


print('Для операций используются команды +,-,/,*,pow,mod,random,fac,arccos')
# WARNING! Незлья закрывать скобки до того, как введёте содержимое, иначе Python не распознает аргумент

Calc = Calculator()

Calc.mainloop()