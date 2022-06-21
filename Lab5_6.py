def to_list(x):
    return x.split(',')

def to_dict(x,y):
    return dict(zip(x,y)).items()

#list = 'Съешь,ещё,этих,мягких,французских,булок,да,выпей,чаю'
#keylist = 'Вводим,через,запятую,список,слов,формируем,из,этого,множество'

list = to_list(str(input()))

print()
print('Длина списка:',len(list),'\nВеедите список с таким же количеством слов')
print()

keylist = to_list(input())

print()
for key,value in to_dict(list,keylist):
    print(key,':',value)

