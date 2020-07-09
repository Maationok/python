spisok_chisel = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
noviy_spisok = [el for el in spisok_chisel if spisok_chisel.count(el) == 1]
print(noviy_spisok)
