# Zadatak1
# def total_euro(radni,sat):
#     return radni*sat

# radni_sati=int(input("Unesite broj radnih sati: \n"))
# satnica=float(input("Unesite vasu satnicu: \n"))
# ukupno=total_euro(radni_sati,satnica)
# print(ukupno)


# Zadatak2
# try:
#     ocjena=float(input("Unesite ocijenu: \n"))
#     if ocjena>=0.0 or ocjena<=1.0:
#         if(ocjena>=1.0):
#             print("Ponovite unos")
#         elif(ocjena>=0.9):
#             print("A")
#         elif(ocjena>=0.8):
#             print("B")
#         elif(ocjena>=0.7):
#             print("C")
#         elif(ocjena>=0.6):
#             print("D")
#         else:
#             print("F")
            


# except:
#     print("Upisite valjan uvjet")

# Zadatak3
# brojevi=[]
# brojac=0
# try:
#     while True:
#         broj=int(input("Unesite broj u listu: \n"))
#         if broj=="Done":
#             break
#         else:
#             brojevi.append(broj)
#             brojac+=1


# except:
#     print("Unesite valjan unos\n")

# print("Korisnik je unio ",brojac," brojeva")
# print("Srednja vrijednost: ",sum(brojevi)/len(brojevi))
# print("Minimalna vrijednost: ",min(brojevi))
# print("Maksimalna vrijednost: ",max(brojevi))
# brojevi.sort()
# print(brojevi)

# #Zadatak4
# spam_counter = 0
# sum = 0.0

# unos = input("unesite ime tekstualne datoteke \n")
# datoteka = 'C:\\Users\\student\\Desktop\\PSU\\'+unos+'.txt'
# try:
#   dat = open(datoteka, 'r')
# except:
#     print("Datoteka ne postoji")

# for line in dat:
#    line = line.split()
#    if("X-DSPAM-Confidence:" in line):
#       spam_counter += 1
#       sum += float(line[1])


# print("Srednja vrijednost pouzdanosti je : ", sum/spam_counter)

#Zadatak4
# spam_counter = 0
# sum = 0.0

# unos = input("unesite ime tekstualne datoteke \n")
# datoteka = 'C:\\Users\\student\\Desktop\\'+unos+'.txt'
# try:
#   dat = open(datoteka, 'r')
# except:
#     print("Datoteka ne postoji")

# for line in dat:
#    line = line.split()
#    if("X-DSPAM-Confidence:" in line):
#       spam_counter += 1
#       sum += float(line[1])


# print("Srednja vrijednost pouzdanosti je : ", sum/spam_counter)

#Zadatak5
#rijecnik = {}
# brojac = 0
# try:
#  dat = open("C:\\Users\\student\\Desktop\\song.txt", 'r')


# except:
#     print("datoteka ne postoji")

# for line in dat:
#    line = line.split()
#    for rijec in line:
#       if rijec in rijecnik:
#          rijecnik[rijec] += 1
#       else:
#          rijecnik[rijec] = 1

# unikatne_rijeci = []

# for rijeci in rijecnik:
#    if rijecnik[rijeci] == 1:
#       unikatne_rijeci.append(rijeci)
#       brojac += 1


# print(rijecnik)
# print("Broj unikatnih rijeci: ", brojac)
# print(unikatne_rijeci)

#Zadatak6
# spam_sum = 0
# ham_sum = 0
# spam_counter = 0
# ham_counter = 0
# usklicnici_counter = 0
# try:
#  dat = open("C:\\Users\\student\\Desktop\\SMSSpamCollection.txt", 'r')

# except:
#     print("Datoteka ne postoji")

# for line in dat:
#    line = line.split()
#    if(line[0] == "ham"):
#       ham_counter += 1
#       ham_sum += len(line)
#    elif(line[0] == "spam"):
#       spam_counter += 1
#       spam_sum += len(line)
#       if("!" in line[-1]):
#          usklicnici_counter += 1

# print("prosjecan broj rijeci u sms porukama tipa ham: ", ham_sum/ham_counter)
# print("prosjecan broj rijeci u sms porukama tipa spam: ", spam_sum/spam_counter)
# print("broj sms poruka spam koje završavaju sa !", usklicnici_counter)
