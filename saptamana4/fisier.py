file=open('data.txt', 'r+')
# r -> se citeste, nu se adauga, este valoarea cu care vine default functia open, daca fisieryl nu exista apare eroare
# w-> drept de scriere, daca fisierul nu exista, il creeaza
# a-> deschidem fisierul cu drept de adaugare, datele existente raman, creaza fisierul daca nu exista
# r+ -> deschidem fisierul cu drept de scriere, dar si de citire

# file.write('Hello1')
# file.close()
# file=open("data3.txt" , "w")
# try:
#     file.write('hello')
# finally:
#     file.close()

# with open('data.txt', 'w') as file:
#     file.write('curs python\n')
#     file.write('curs python1\n')
#     file.write('curs python2\n')

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line,'line')

# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)
#
# with open('data.txt', 'r') as file:
#     while True:
#         line=file.readline()
#         if not line:
#             break
#         print(line)