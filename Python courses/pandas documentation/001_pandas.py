# import pandas as pd
# import json
# ############# razobratjsa s papkoi kuda devajutsja faily!!!!
# with open('../../Scratches_files/sample2.json','r', encoding='utf') as file:
#     data = json.load(file)
#
# df = pd.DataFrame(data['people'])
# print(df)
################
#
import pandas as pd

df = pd.read_csv('csv_files/2019.csv')
# # # # # # #
# # # # # # ###### skiprows=  (propusk stroki)
# # # # # # # df = pd.read_csv('csv_files/2019.csv', skiprows=1)
# # # # # # ######### heeader= zogolovok
# # # # # # # df = pd.read_csv('csv_files/2019.csv', header=None)
# # # # # # ### nrows= skolko znachenij schiatat
# # # # # #
# # # # # # # pd.set_option('display.max_colums', 9 )
# # # # # # # pd.set_option('display.max_rows', 156)
# # # # # #
# # # # # # # df = pd.read_csv('csv_files/2019.csv', header=0, names=['Country or region', 'GDP per capital'])
# # # # # # print(df)
# # # # # # print(type(df))
# # # # # # #
# # # # # # #
# # # # # # # for df in pd.read_csv('csv_files/2019.csv', chunksize=5):
# # # # # # #     print('**********************')
# # # # # # #     print(df)
# # # # # # #
# # # # # # ### Zapis dlja otsutstvija :
# # # # # # # df.to_csv('csv_file/new_csv.csv', index=False, header=False)
# # # # # #
# # # # # # # df.to_csv('data_files/2019.csv', colums=['Coutry of region', 'Overall rank'])
# # # # # # #
# # # # # # #
# # # # # # # print(df.columns)
# # # # # # # print(type(df.columns))
# # # # # #
# # # # # # # ##### head - golova , tail - poslednij
# # # # # # # print(df.head())
# # # # # # #
# # # # # # # print(df.tail())
# # # # # # #
# # # # # # # people = {
# # # # # # #     'first': ['Bob', 'Bill', 'Mary', 'John'],
# # # # # # #     'last': ['Smith', 'Gold', 'Summer', 'Black'],
# # # # # # #     'email': ['bob@example.com' , 'bill@example.com' , 'mary@example.com ', 'john@example.com']
# # # # # # #
# # # # # # # }
# # # # # # #
# # # # # # # df = pd.DataFrame(people)
# # # # # # # # # # print(df)
# # # # # # # # print(df['email'])
# # # # # # # # ### OR
# # # # # # # # # print(df.email)
# # # # # # # #
# # # # # # # # # print(type(df['email']))
# # # # # # # # print([['first','last', 'email']])
# # # # # # # #
# # # # # # # # # names = df['first']
# # # # # # # # names = df[['first', 'last']]
# # # # # # # # print(type(names))
# # # # # # # #
# # # # # # # # for name, lastname in names:
# # # # # # # #     print('Hello my name is ' + name + ' ' + lastname)
# # # # # # # #     print(name,lastname)
# # # # # # # #### dlja vyvoda rjadov
# # # # # # # print(df.iloc[0])
# # # # # # # print(type(df.iloc[0])
# # # # # # # # print(df.iloc[0][email])
# # # # # #
# # # # # # ### perechislenie konnkretnyh rjadov
# # # # # # print(df.iloc[[0, 3, 2]])
# # # # # # print(df.iloc[1:3])
# # # # # #
# # # # # # print(df.iloc[[0, 1, 2], [0, 1, 6]])
# # # # # # print(df.iloc[[45, 48],['Country or region', 'GDP per capital']])
# # # # # #
# # # # # # print(df)
# # # # # # print(df.shape[1])
# # # # # # ##### Delaet polnuju rospis s razborom (udobnyj)
# # # # # # for x in range(df.shape[0]):
# # # # # #     print(df.iloc[x])
# # # # # #
# # # # # #
# # # # # #
# # # # # # ####### podschitqvaet kol vo raz v spiske
# # # # # # print(df['Country or region'].value_counts())
# # # # # # #
# # # # # # print(df.loc[45, 48],['Country or region'])
# # # # # # print(df.loc[3, 'Country or region '])
# # # # #
# # # # #
# # # # # # print(df.loc[3, 5, 12, 124], 'GPD per capital')
# # # # # #
# # # # # # #
# # # # # # # print(df.loc[3:50, ['Country of region':'Healty life expectancy']])
# # # # # # # print(df.loc[[3, 65, 23, 123], 'Country of region ':'Healty life ecprect'])
# # # # # #
# # # # # # df2 = df.loc[3:40, 'Country or region':'Healty life expectancy']
# # # # # # print(type(df2))
# # # # #
# # # # # data = df.loc[50]
# # # # # # print(type(data))
# # # # # print(data['Coutry or region'])
# # # # #
# # # #
# # # # for index, row in df.iterrows():
# # # #     print(index)
# # # #     print(row)
# # #
# # # # ########## sravnenija
# # # # print(df.loc[df['Country or region'] == 'Estonia'])
# # # # print(df.loc[df['GDP per capital'] > 1])
# # # #
# # # #
# # # #
# # pd.set_option('display.max_columns', 9)
# # pd.set_option('display.max_rows', 156)
# # print(df)
# #
# ###### sortirovka
# # print(df.sort_values('Coutry or region'))
# #
#
# # print(df.sort_values(['Coutry or region', 'Generosity', 'Score'], ascending=False))
# # print(df.sort_values(['Coutry or region', 'Generosity', 'Score'], ascending=[0, 1]))
#
#
# # print(df.describe())
# #
# # ###### sozdanie novyh stolbcov s vybronnymi df // (type doetsja stolbcu celikom)
# # df['total'] = df['GDP per capital'] + df['Score'] + df['Helaty life exprectancy']
# # print(df)
# # # print(df.dtypes)
# # # print(df['total'])
# #
# # df = df.drop(columns=['total'])
# #
# #
# # print(df.loc[df['GDP per capital'] >1, ['Country or region']])
# # print(df)
#
#
# ############ poisk po soderzhaniju bukv ////   "|" znachook and
# print(df.loc[df.loc['Country or region'].str.contais('on')])
# print(df.loc[df.loc['Country or region'].str.contais('Es|ia'),['Country or region']])
#


########## Gruppirovka po vybrannym dannym. Esli porametry povtorjajutsja, to vyschityvaet srednij pokazatel
# print(df.groupby('Country or region').mean().sort_values('Score', ascending=False))
# print(df.groupby('Score').mean())


print(df.groupby('GDP per capital').sum())
print(df.groupby('GDP per capital').mean())
##### podschet
print(df.groupby('GDP per capital').count())


