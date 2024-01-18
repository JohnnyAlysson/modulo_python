import datetime

def changeMonth(date):
    breaking_date = []
    for char in date:
        if char == "/":
            pass
        elif int(char) >= 0 and int(char) <=9:
            breaking_date.append(char)

    day=int(breaking_date[0]+breaking_date[1])
    month=int(breaking_date[2]+breaking_date[3])
    year=int(breaking_date[4]+breaking_date[5]+breaking_date[6]+breaking_date[7])

    new_date=datetime.date(year,month,day)
    
    return new_date.strftime("%d %B, %Y")  
