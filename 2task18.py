age = int(input("Сколько вам лет?: "))
even_numbers = list(range(2,age,2))
odd_nubers = list(range(1,age,2))
if age % 2 == 0:
    print(even_numbers)
else:
    print(odd_nubers)


