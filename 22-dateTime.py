#datetime
import datetime
x = datetime.datetime.now()
print(x);
print(x.year) #2023
y = datetime.datetime(2020,5,17)
print(y)

#strftime()
# formatting date objects into readable strings

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%a")) #Fri , Weekday short version
print(x.strftime("%A")) #Friday , Weekday full version
print(x.strftime("%w")) #5 , Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d")) #01 ,  Day of month 01-31
print(x.strftime("%b")) #jun, monthname short version
print(x.strftime("%B")) #june, monthname full version
print(x.strftime("%m")) #06 , month number 
print(x.strftime("%y")) #18 , year short version
print(x.strftime("%Y")) #2018 , year full  version
print(x.strftime("%H")) #00 , 	Hour 00-23
print(x.strftime("%I")) #12, Hour 00-12
print(x.strftime("%p")) #AM , AM/PM
print(x.strftime("%M")) #00 , Minute 00-59
print(x.strftime("%S")) #00 , Second 00-59
print(x.strftime("%f")) #000000, Microsecond 000000-999999
print(x.strftime("%z")) # UTC offset
print(x.strftime("%Z")) #Timezone
print(x.strftime("%j")) #152, Day number of year 001-366
print(x.strftime("%U")) #21 , Week number of year, Sunday as the   first day of week, 00-53
print(x.strftime("%W")) #22 , Week number of year, Monday as the first day of week, 00-53
print(x.strftime("%c")) #Fri Jun  1 00:00:00 2018, Local version of date and time
print(x.strftime("%C")) #20 , Century
print(x.strftime("%x")) #06/01/18 , Local version of date
print(x.strftime("%X")) #00:00:00 , Local version of time
print(x.strftime("%%")) #% , A % character
print(x.strftime("%G")) #2018 , ISO 8601 year
print(x.strftime("%u")) #5 , ISO 8601 weekday (1-7)
print(x.strftime("%V")) #22 , ISO 8601 weeknumber (01-53)







