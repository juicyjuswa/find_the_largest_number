#ask user for input
integer_1= int(input("Enter the first number: "))
integer_2= int(input("Enter the second number: "))
integer_3= int(input("Enter the third number: "))
integer_4= int(input("Enter the fourth number: "))

#check integer_1
if integer_1 > integer_2 or integer_1 > integer_3 or integer_1 > integer_4:
  print ("the largest number is " + integer_1)


#check integer_2
elif integer_2 > integer_1 or integer_2 > integer_3 or integer_2 > integer_4:
  print ("the largest number is " + integer_2)


#check integer_3
elif integer_3 > integer_1 or integer_3 > integer_2 or integer_3 > integer_4:
  print ("the largest number is " + integer_3)

#check integer_4
#else 
else:
  print ("the largest number is " + integer_4)