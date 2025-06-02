# Zadatak 1

# import pandas as pd
# import numpy as np

# mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\lv3vj\\mtcars.csv.csv')

# print(mtcars.sort_values(by='mpg').head(5))
# print(mtcars[mtcars.cyl == 8].sort_values(by='mpg').tail(3))

# cyl6 = mtcars[mtcars.cyl == 6]
# cyl6 = cyl6.iloc[:,1:2]
# print(cyl6.mean())

# car1 = mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2.000) & (mtcars.wt <2.200 )] 
# car1 = car1.iloc[:,1:2]
# print(car1.mean())

# manual = 0
# automatik = 0
# vrsta = mtcars.sort_values(by='am')
# for car in vrsta.am:
#     if(car == 0):
#         manual += 1

#     elif(car == 1):
#      automatik += 1
    
# print('Automatika ima ' , automatik , 'Manualaca ima', manual)

# car6 = (mtcars[(mtcars.am == 1) & (mtcars.hp > 100)])
# print('Ima ih' ,len(car6))

# car_kg = ([(mtcars.wt *1000 / 2.20462262)])
# print(car_kg) 

# Zadatak 2

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\LV3\\mtcars.csv.csv')


# sorted = mtcars.sort_values(by='cyl')
# cyl = sorted.iloc[:,2:3]
# mpg = sorted.iloc[:,1:2]
# vector = np.vectorize(np.int_)
# cyl = np.array([cyl])
# x = vector(cyl)

# vector = np.vectorize(np.int_)
# mpg = np.array([mpg])
# y = vector(mpg)
# #cyl = [sorted.cyl.to_numpy()]
# mpg = [sorted.mpg.to_numpy()]


# plt.bar(x, y)
# plt.title('Fruit Sales')
# plt.xlabel('Cylinders')
# plt.ylabel('mpg')
# plt.show()

# Zadatak 3

# import urllib.request
# import pandas as pd
# import xml.etree.ElementTree as ET
# import matplotlib.pyplot as plt

# def fetch_air_quality_data():
#     url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'
#     airQualityHR = urllib.request.urlopen(url).read()
#     return ET.fromstring(airQualityHR)

# def process_data(root):
#     df = pd.DataFrame(columns=('Mjerenje', 'Vrijeme'))
    
#     children = list(root)
#     for i, child in enumerate(children):
#         obj = list(child)
#         row = dict(zip(['Mjerenje', 'Vrijeme'], [obj[0].text, obj[2].text]))
#         row_s = pd.Series(row)
#         row_s.name = i
#         df = pd.concat([df, row_s])
#         df.at[i, 'Mjerenje'] = float(df.at[i, 'Mjerenje'])
    
#     df['Vrijeme'] = pd.to_datetime(df['Vrijeme'], utc=True)
#     df['month'] = df['Vrijeme'].dt.month
#     df['dayOfweek'] = df['Vrijeme'].dt.dayofweek
#     return df

# def plot_data(df):
#     df.plot(y='Mjerenje', x='Vrijeme')
#     plt.show()

# def get_top_3_days(df):
#     return df.sort_values(['Mjerenje'], ascending=False).head(3)

# if __name__ == "__main__":
#     root = fetch_air_quality_data()
#     df = process_data(root)
#     plot_data(df)
#     print("Top 3 dana s najvećom koncentracijom PM10:")
#     print(get_top_3_days(df))