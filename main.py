a = int(input("Enter the number you want to check"))
if(a%4 == 0):
 if(a%100 == 0):
   if (a%400 == 0):
     print("leap year")
   else:
     print("Not leap year")
 else:
   print("leap year")
else:
  print("Not leap year")