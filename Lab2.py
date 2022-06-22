# А зачем делать через цикл? Давайте лучше так:
print('Type "break" to quit')

while True:                             # Чтобы каждый раз не перезапускать программу
    string = str(input())
    if string.lower() == 'break':
        break

    string = string[0:2]+string[3:-1]
    print(string)
    string = string.lower()
    if string.find('с') != -1 or string.find('c') != -1:
        print("В строке есть символ С")
