#Zad 1

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

#Zad 2
#1)
print(df[df["Liczba"]>1000])
#2)
print(df[df['Imie']=='MACIEJ'])
#3)
print(df.agg({'Liczba': ['sum']}))
#4)
print(df.where(df.Rok<2006).agg({'Liczba':['sum']}))
#5)
sumch=df.where(df.Plec=='M').agg({'Liczba':['sum']})
print(sumch)
sumdz=df.where(df.Plec=='K').agg({'Liczba':['sum']})
print(sumdz)
print(sumch+sumdz)
#6)
print(df.sort_values("Liczba", ascending=False).groupby(['Rok', 'Plec']).nth(0))

#Zad 3

df=pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
print(df)

#1)
print(np.unique(df.Sprzedawca))

#2)
print(df.sort_values(by='Utarg').tail())
#3)
print(df.groupby(by='Sprzedawca').agg({'idZamowienia':[('count')]}))

#4)
print(df.groupby(by='Kraj').agg({'Utarg':['sum']}))

#5)
df['year']=pd.DatetimeIndex(df['Data zamowienia']).year
print(df.where(df.Kraj=="Polska").where(df['year']==2005).agg({'Utarg':['sum']}))

#6)
print(df.where(df['year']==2004).agg({'Utarg':['mean']}))


