calculation = input("What you want to calculate?: ")

if calculation.find("+") != -1:
   value1 = int(calculation[0:calculation.find("+")])
   value2 = int(calculation[calculation.find("+") + 1:])
   print("Your answer is :", value1 + value2)

elif calculation.find("-") != -1:
   value1 = int(calculation[0:calculation.find("-")])
   value2 = int(calculation[calculation.find("-") + 1:])
   print("Your answer is :", value1 - value2)

elif calculation.find("*") != -1:
   value1 = int(calculation[0:calculation.find("*")])
   value2 = int(calculation[calculation.find("*") + 1:])
   print("Your answer is :", value1 * value2)

elif calculation.find("/") != -1:
   value1 = int(calculation[0:calculation.find("/")])
   value2 = int(calculation[calculation.find("/") + 1:])
   print("Your answer is :", value1 / value2)

else:
   print("Sorry i can't help you !")
