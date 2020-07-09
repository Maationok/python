spisok_chisel = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
noviy_spisok = [el for i, el in enumerate(spisok_chisel) if spisok_chisel[i - 1] < spisok_chisel[i] and i > 0]
print(noviy_spisok)
