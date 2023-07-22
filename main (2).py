num = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

userinput2 = input("What operation do you want to do?: ")

if userinput2 == "+" : 
  result = num+num2

elif userinput2 == "-" : 
  result = num-num2

elif userinput2 == "*" : 
  result = num*num2

elif userinput2 == "/" : 
  result = num/num2
else:
  print("Please use an operation next time")

print("Your answer is:", result)

if result==result: {
  print("Correct!")
  
}

