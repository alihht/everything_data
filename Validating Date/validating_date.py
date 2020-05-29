from array import *

day=0
month=0
year=0

day=int(input("Enter a day: "))
month=int(input("Enter a month: "))
year=int(input("Enter a year: "))

check_day=""
check_month=""
check_year=""
check_leap=""

chk_lep= None
chk_date= None

months_31=array('i',[1,3,5,7,8,10,12])
months_30=array('i',[4,6,9,11])

if (year < 1):
    check_year="The year is wrong, please enter a correct year."
    chk_date = False
else:
    by4 = year % 4
    by100 = year % 100
    by400 = year % 400
    chk_date = True
    if(by4 == 0) and (by100 == 0) and (by400 == 0):
        check_leap="It is a leap year."
        chk_lep = True
    elif(by100 == 0):
        check_leap="It is not a leap year."
        chk_lep = False
    elif(by4 == 0):
        check_leap="It is a leap year."
        chk_lep = True
    else:
        check_leap="It is not a leap year."
        chk_lep = False

if(month < 1) or (month > 12):
    chk_date=False
else:
    chk_date=True

if (day < 1):
    chk_date=False
else:
    chk_date=True

if (month == 2) and (chk_lep == True):
    if (day > 29) or (day < 1):
        check_day = "Day is worng. It is Feb and it is a leap year!"
        chk_date=False
    else:
        chk_date=True
elif(month == 2) and (chk_lep == False):
    if (day > 28) or (day < 1):
        check_day = "Day is wrong. It is Feb and it is not a leap year!"
        chk_date=False
    else:
        chk_date=True


for i in range(len(months_31)):
    if (month == months_31[i]):
        if (day > 31):
            check_day="This month has only 31 days, please enter a correct day."
            chk_date=False
        else:
            chk_date=True

for j in range(len(months_30)):
    if (month == months_30[j]):
        if (day > 30):
            check_day="This month has only 30 days, please enter the correct day."
            chk_date=False
        else:
            chk_date=True

print()
if(chk_date == True):
    print("The entred date is correct")
else:
    print("The entered date is wrong")