import random
my_list = []
# Не найоптимальніший варіант рішення
for i in range(random.randint(0, 15)):
    my_list.append(random.randint(0, 10))
print(my_list)