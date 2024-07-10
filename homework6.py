#Словари
my_dict = {'Egor': 2005, 'Lera': 1996, 'Sasha': 1985}
print(my_dict, my_dict['Egor'], my_dict.get('Might'), sep='/n')
my_dict.update({'Vasya': 2010, 'Liza': 2015})
print(my_dict)
a = my_dict.pop("Egor")
print(a)
print(my_dict)
#Множества
my_set = {1, 1, 'Python', 5, 8.8}
print(my_set)
my_set.update({'Урбан','Университет'})
print(my_set)
my_set.discard('Python')
print(my_set)
