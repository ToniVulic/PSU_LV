# radni_sati=int(input("Radni sati: "))
# satnica=float(input("eura/h: "))
# zarada=radni_sati*satnica
# print("ukupno", zarada)

# def total_euro(sati,satnica):
#     return sati*satnica

# zarada2=total_euro(radni_sati,satnica)
# print(zarada2)



# try:
#     ocjena=5
#     while ocjena<0 or ocjena>1:
#         ocjena=float(input())
#         if ocjena<0 or ocjena>1:
#              print("Mora biti izmedju 0 i 1")
#     if ocjena<0.6:
#         print('F')
#     elif ocjena<0.7:
#         print('D')
#     elif ocjena<0.8:
#         print('C')
#     elif ocjena<0.9:
#         print('B')
#     else:
#         print('A')
# except:
#         print("to nije broj")

# try:
#     list=[]
#     while True:
#         a=input()
#         if a=='Done':
#             break
#         else:
#            list.append(int(a))
#     print("len: ",len(list))
#     print("avg: ",sum(list)/len(list))
#     print("max: ",max(list))
#     print("min: ",min(list))
#     list.sort()
#     print(list)
# except:
#     print("krivi unos")

spam_counter = 0
sum = 0.0

unos = input("unesite ime tekstualne datoteke \n")
datoteka = 'C:\\Users\\student\\Desktop\\'+unos+'.txt'
try:
  dat = open(datoteka, 'r')
except:
    print("Datoteka ne postoji")

for line in dat:
   line = line.split()
   if("X-DSPAM-Confidence:" in line):
      spam_counter += 1
      sum += float(line[1])


print("Srednja vrijednost pouzdanosti je : ", sum/spam_counter)