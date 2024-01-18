import datetime
import random

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


def rollDie():
    count1 = count2=count3=count4=count5=count6 = 0
    for i in range (1000000):
        die_roll=random.randint(1,6)
        if die_roll == 1:
            count1 +=1
        elif die_roll ==2:
            count2 += 1
        elif die_roll ==3:
            count3 += 1
        elif die_roll ==4:
            count4 += 1
        elif die_roll ==5:
            count5 += 1
        elif die_roll ==6:
            count6 += 1
    print(f" number 1 appeared {round((count1/1000000),2)*100} %")
    print(f" number 2 appeared {round((count2/1000000),2)*100} %")
    print(f" number 3 appeared {round((count3/1000000),2)*100} %")
    print(f" number 4 appeared {round((count4/1000000),2)*100} %")
    print(f" number 5 appeared {round((count5/1000000),2)*100} %")
    print(f" number 6 appeared {round((count6/1000000),2)*100} %")

def shuffleWord(word : str):
    breaking_word=[]
    for letter in word:
        breaking_word.append(letter.lower())
        #adicionar title aleatorio


    random.shuffle(breaking_word)
    new_word= ""
    for i in breaking_word:
        new_word= new_word+i
    
    print(new_word)