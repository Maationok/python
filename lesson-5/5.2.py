file = open('5.2.txt', 'r')
stroki = file.readlines()
print('Kolichestvo strok = ', len(stroki))
for i in range(len(stroki)):
    stroka = stroki[i].split()
    print(i + 1, '-aya stroka: ', len(stroka), 'slov')
file.close()
