from random import random
from math import acos

class Calculator:
    def __init__(self):
        pass

    def abs(self,first):
        return abs(first)

    def fac(self,first):
        a = 0
        for i in range(first+1):
            a += i
        return a

    def rand(self):
        return int(random() * 100 // 1)

    def acos(self,first):
        return round(acos(first),6)

    def mainloop(self):
        while True:
            inp = str(input())
            if inp.lower() == 'q':
                break
            inp = inp.replace('arccos', 'Calc.acos')
            inp = inp.replace('rand', 'Calc.rand()')
            inp = inp.replace('mod', 'Calc.abs')
            inp = inp.replace('fac', 'Calc.fac')
            print(eval(inp))

print('Для операций используются команды +,-,/,*,pow,mod,random,fac,arccos')
#WARNING! Незлья закрывать скобки до того, как введёте содержимое, иначе Python не распознает аргумент

Calc = Calculator()

Calc.mainloop()




    