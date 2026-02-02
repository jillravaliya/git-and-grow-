calculation = input("What you want to calculate?: ")

if calculation.find("==") != -1:
   value1 = int(calculation[0:calculation.find("==")].strip())
   value2 = int(calculation[calculation.find("==") + 2:].strip())
   print("Your answer is :", value1 == value2)

elif calculation.find("!=") != -1:
   value1 = int(calculation[0:calculation.find("!=")].strip())
   value2 = int(calculation[calculation.find("!=") + 2:].strip())
   print("Your answer is :", value1 != value2)

elif calculation.find(">") != -1:
   value1 = int(calculation[0:calculation.find(">")].strip())
   value2 = int(calculation[calculation.find(">") + 1:].strip())
   print("Your answer is :", value1 > value2)

elif calculation.find(">=") != -1:
   value1 = int(calculation[0:calculation.find(">=")].strip())
   value2 = int(calculation[calculation.find(">=") + 2:].strip())
   print("Your answer is :", value1 >= value2)

elif calculation.find("<") != -1:
   value1 = int(calculation[0:calculation.find("<")].strip())
   value2 = int(calculation[calculation.find("<") + 1:].strip())
   print("Your answer is :", value1 < value2)

elif calculation.find("<=") != -1:
   value1 = int(calculation[0:calculation.find("<=")].strip())
   value2 = int(calculation[calculation.find("<=") + 2:].strip())
   print("Your answer is :", value1 <= value2)
