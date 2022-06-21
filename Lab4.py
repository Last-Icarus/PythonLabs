#Откуда у нас количество овощей?

A = [str(input()),str(input()),str(input())]
#A = ['Картошка','Капуста','Огурец']

print(('{0}, {1}, {2}'.format(*A)).lower())
print(('{0}, {1}, {2}'.format(*A)).upper())
print(('{0}, {1}, {2}'.format(*[i.capitalize() for i in A])))
