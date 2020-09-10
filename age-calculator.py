from datetime import *


date_time = datetime.now()
print("Example of birth time : 22 January,2009")
birth_time = input("Enter your birth time:\n")


months = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}

current_day = date_time.strftime("%d")
current_month = months[date_time.strftime("%B")]
current_year = date_time.strftime("%Y")


birth_year = birth_time.split(",")[1]

birth_month = months[str(birth_time.split(",")[0]).split(" ")[1]]

birth_day = birth_time.split(" ")[0]



days = str(int(current_day) - int(birth_day))
months = str(int(current_month) - int(birth_month))
years = str(int(current_year) - int(birth_year))

if "-" in days:
    days.replace("-","")


if "-" in months:
    months.replace("-","")


if "-" in years:
    years.replace("-","")


print(f"You are {years} Years, {months} Months and {days} Days old.")

