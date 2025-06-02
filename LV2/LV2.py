#Zadatak 1
# import numpy as np
# import matplotlib.pyplot as plt


# x = [1.0,3.0,3.0,2.0,1.0]
# y = [1.0,1.0,2.0,2.0,1.0]
# plt.plot(x, y, 'b', linewidth=1, marker=".", markersize=5)


# plt.axis([0,4,0,4])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('primjer 1')
# plt.show()

#Zadatak 2
# import numpy as np
# import matplotlib.pyplot as plt


# data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
# delimiter=",", skiprows=1)

# #print(data)
# mpg = data[:,0:1]
# hp = data[:,3:4]
# wt = data[:,5:6]
# cyl = data[:,1:2]

# plt.scatter(mpg, hp, c='purple', s=wt*12, cmap='plasma')
# plt.show()

# print(np.min(mpg))
# print(np.max(mpg))
# print(np.mean(mpg))



# '''for a in data[:,0:1]:
#     if a == 6:
#         mpg1= a[:,0:1]
# '''
# i = -1
# mpg2 = []
# for a in cyl:
#     i += 1
#     if a == 6:
#         mpg2.append(mpg[i])      


# print(np.min(mpg2))
# print(np.max(mpg2))
# print(np.mean(mpg2))        

# Zadatak 3

# import numpy as np
# import matplotlib.pyplot as plt
# img = plt.imread("C:\\Users\\Matija ciki\\Desktop\\LV2\\tiger.png")
# img = img[:,:,0].copy()
# img_array=[]
# print(img.shape)
# print(img.dtype)
# plt.figure()


# plt.imshow(np.rot90(img), cmap="gray")
# plt.show()
# plt.imshow(np.fliplr(img), cmap="gray")
# plt.show()


# img_array=img+0.6
# img_array[img_array>1]=1

# plt.figure(1)
# plt.title("a) brightness")
# plt.imshow(img_array,cmap='gray')

# img3 = img[::5,::5] #smanjena kvaliteta

# plt.figure(4)
# plt.title("d) smanjena kvaliteta slike")
# plt.imshow(img3,cmap='gray')
# redovi = img.shape[0] #broj redova
# stupci = img.shape[1] #broj stupaca
# dg = stupci//4
# gg = stupci//2

# pr_img = img.copy()
# for i in range(redovi):
#     for j in range(stupci):
#         if (j < dg or j > gg): 
#             pr_img[i][j] = 0



# plt.figure(5)
# plt.title("e) stupci")
# plt.imshow(pr_img, cmap='gray')
# plt.show()

# Zadatak 4

# import numpy as np
# import matplotlib.pyplot as plt

# def check(kvadrat,redovi,stupci):
#     crne = np.zeros((kvadrat,kvadrat))
#     bijele = np.ones((kvadrat,kvadrat))*255
#     red1 = np.hstack([crne,bijele]*(stupci//2))
#     if stupci % 2 != 0:
#         red1 = np.hstack([red1,crne])
    
#     red2 = np.hstack([bijele,crne]*(stupci//2))
#     if stupci % 2 != 0:
#         red2 = np.hstack([red2, bijele])

#     polje = np.vstack([red1,red2] * (redovi//2))
#     if redovi % 2 != 0:
#         polje = np.vstack([polje,red1])
#     return polje

# img = check(50,4,5)
# plt.imshow(img, cmap='gray', vmin=0, vmax=255)
# plt.show()