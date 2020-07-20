class Matrix:
    def __init__(self, matrisa1, matrisa2):
        self.matrisa1 = matrisa1
        self.matrisa2 = matrisa2

    def __add__(self):
        matrisa = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(len(self.matrisa1)):
            for j in range(len(self.matrisa2[i])):
                matrisa[i][j] = self.matrisa1[i][j] + self.matrisa2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrisa]))

    def __str__(self):
        matrisa = self.matrisa1
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrisa]))

    def __str2__(self):
        matrisa = self.matrisa2
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrisa]))


matrisa1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrisa2 = [[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]]

summa_matris = Matrix(matrisa1, matrisa2)
print(summa_matris.__str__())
print("\n + \n")
print(summa_matris.__str2__())
print("\n = \n")
print(summa_matris.__add__())
