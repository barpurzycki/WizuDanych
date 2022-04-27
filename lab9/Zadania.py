#Zad 1

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# grupa = df.groupby('Rok').agg({'Liczba':['sum']})
# grupa.plot()
# x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
# plt.xticks(x, rotation='vertical')
# plt.show()

#Zad 2

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# grupa = df.groupby('Plec').agg({'Liczba':['sum']})
# grupa.plot(kind = 'bar')
# plt.legend('Ilość urodzonych dzieci w latach 2000-2017')
# plt.ylabel('Ilość urodzonych dzieci (skrócone)')
# plt.show()

#Zad 3

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# grupa = df.groupby(['Rok', 'Plec']).agg({'Liczba':['sum']}).tail(10)
# grupa.plot(kind = 'pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(8,8))
# plt.show()

#Zad 4

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

grupa = df.groupby('Sprzedawca').agg({'idZamowienia':['count']})
grupa.plot(kind='bar')
plt.show()
