def my_func(argument_1, argument_2, argument_3):
    if argument_1 <= argument_2 and argument_1 <= argument_3:
        return argument_2 + argument_3
    if argument_2 <= argument_1 and argument_2 <= argument_3:
        return argument_1 + argument_3
    if argument_3 <= argument_1 and argument_3 <= argument_2:
        return argument_1 + argument_2


print("Vvedite argument_1")
argument_1 = int(input())
print("Vvedite argument_2")
argument_2 = int(input())
print("Vvedite argument_3")
argument_3 = int(input())
print(my_func(argument_1, argument_2, argument_3))
