my_dict={'Sasha':1999,'Masha':2000,'Tanya':2002}
print('Dist: ',my_dict)
print('Existing value: ',my_dict['Sasha'])
print('Not existing value: ',my_dict.get('Anna'))
my_dict.update({'Dima':2001,'Andrey':1998})
ban=my_dict.pop('Masha')
print('Deleted value: ', ban)
print('Modified dictionary: ',my_dict)
print()
# Создайте переменную my_set и присвойте ей множество, состоящее из
# разных типов данных с повторяющимися значениями.
my_set={1, 2, 3, 4, 5, 'Банан', 3.14}
# Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print('Set: ',my_set)
#Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(6)
my_set.add('Ананас')
#Удалите один любой элемент из множества my_set.
my_set.remove(5)
#Выведите на экран измененное множество my_set.
print('Modified set: ', my_set)