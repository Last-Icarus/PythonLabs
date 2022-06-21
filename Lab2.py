# А зачем делать через цикл? Давайте лучше так:

string = str(input())
string = string[0:2]+string[3:-1]
print(string)
if string.find('с') != -1 or string.find('c') != -1:
    print("В строке есть символ С")
print("Длина строки:",len(string))