# input an year and print leap or not
# div by 4 is leap   (ex: 2020)
# not div by 4 is not leap (ex: 2019)
# div by 100 is not leap (ex: 2100)
# but div by 400 is leap (ex: 2000)
year = int(input("enter the year:"))
if year%400==0:
    print("Leap Year")    
elif year%100 ==0:
    print(" not Leap year")
elif year%4==0:
    print("Leap year")
else:
    print("not Leap Year")
