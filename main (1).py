#leapyear
year=int(input("Enter the year:"))
if year%400==0:
  print("it is leapyear")
elif year%100!=0:
  print("it is a leayera")
else:
  print("it is not a leapyear")
  