print('Type "break" to quit')
while True:                            # Чтобы каждый раз не перезапускать программу
    string = input()
    if string.lower() == 'break':
        break
    
    a = ''
    for i in range(len(string)):
        if i != 2 and i != len(string)-1:
            a+=string[i]
    string = string.lower()

    print('\n'+a)

    if string.find('с') != -1 or string.find('c') != -1:
        print("В строке есть символ С")
