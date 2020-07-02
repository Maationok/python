print("Vvedite kolichestvo tovara")
k = int(input())
n = 1
a = []
b = []
c = {}
while n <= k:
    a = dict({'Название': input("Введите название "), 'Цена': input("Введите цену "), 'Количество': input("Введите количество "), 'Ед': input("Введите единицу измерения ")})
    b.append((n, a))
    n += 1
    c = dict(
        {'Название': a.get('Название'), 'Цена': a.get('Цена'), 'Количество': a.get('Количество'), 'Ед': a.get('Ед')})
print(b)
print(c)
