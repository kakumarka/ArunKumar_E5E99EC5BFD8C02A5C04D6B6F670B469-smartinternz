# To find the Leap year
y = int(input("Enter the Year"))
if (y % 4 == 0):
  print("{} is Leap Year".format(y))
else:
  print("{} is Not a Leap Year".format(y))
