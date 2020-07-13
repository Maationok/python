zamena = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
perenos = []
file = open('5.4.1.txt', 'r')
for i in file:
    i = i.split(' ', 1)
    perenos.append(zamena[i[0]] + ' ' + i[1])
file2 = open('5.4.2.txt', 'w')
file2.writelines(perenos)
file.close()
file2.close()
