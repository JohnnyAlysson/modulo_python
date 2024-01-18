# 8. Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
#Opcionalmente, valide a data e retorne NULL caso a data seja inválida
import myModule

user_date=input("   Write a date:\n    DD/MM/AAAA\n")

# breaking_date = []
# for char in user_date:
#     if char == "/":
#         pass
#     elif int(char) >= 0 and int(char) <=9:
#         breaking_date.append(char)
# print(breaking_date)

# day=int(breaking_date[0]+breaking_date[1])
# month=int(breaking_date[2]+breaking_date[3])
# year=int(breaking_date[4]+breaking_date[5]+breaking_date[6]+breaking_date[7])

# date=datetime.date(year,month,day)

# d = date.strftime("%d %B, %Y")
# print(f"The date is {d}")

date=myModule.changeMonth(user_date)
print(f"The date is {date}")

# datetime.day
# datetime.month
# datetime.year

# breaking_date = {"day":"","month": "","year":""}
# breaking_date{"day"=""}
# breaking_date{"month"=""}
# breaking_date{"year"=""}