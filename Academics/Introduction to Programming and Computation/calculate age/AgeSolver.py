#ME11_2_QUISTO.py

from bdayfcn import Birthday

birthday = input("Enter your birthday(MM DD YYYY): ")
date = input("Enter a date(MM DD YYYY): ")
print("Birthday:", birthday)
print("Date of comparison:", date)
birthday = birthday.split()
date = date.split()
bday = Birthday(birthday[0], birthday[1], birthday[2])
DoC = Birthday(date[0], date[1], date[2])
print("Age: ", bday.compare(DoC.m, DoC.d, DoC.y)) 
