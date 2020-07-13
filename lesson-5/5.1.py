file = open('5.1.txt', 'w')
print("Vvedite dannie")
dannie = input()
while dannie:
    file.writelines(dannie)
    print("Vvedite dannie")
    dannie = input()
    if not dannie:
        break

file.close()
