calculation = input("What you want to calculate?: ")

if "and" in calculation:
    value1 = calculation[:calculation.find("and")].strip()
    value2 = calculation[calculation.find("and") + 3:].strip()

    result1 = False
    result2 = False

    if "==" in value1:
        a = value1[:value1.find("==")].strip()
        b = value1[value1.find("==") + 2:].strip()
        result1 = a == b

    elif "!=" in value1:
        a = value1[:value1.find("!=")].strip()
        b = value1[value1.find("!=") + 2:].strip()
        result1 = a != b

    elif ">=" in value1:
        a = value1[:value1.find(">=")].strip()
        b = value1[value1.find(">=") + 2:].strip()
        result1 = a >= b

    elif "<=" in value1:
        a = value1[:value1.find("<=")].strip()
        b = value1[value1.find("<=") + 2:].strip()
        result1 = a <= b

    elif ">" in value1:
        a = value1[:value1.find(">")].strip()
        b = value1[value1.find(">") + 1:].strip()
        result1 = a > b

    elif "<" in value1:
        a = value1[:value1.find("<")].strip()
        b = value1[value1.find("<") + 1:].strip()
        result1 = a < b


    if "==" in value2:
        a = value2[:value2.find("==")].strip()
        b = value2[value2.find("==") + 2:].strip()
        result2 = a == b


    elif "!=" in value2:
        a = value2[:value2.find("!=")].strip()
        b = value2[value2.find("!=") + 2:].strip()
        result2 = a != b

    elif ">=" in value2:
        a = value2[:value2.find(">=")].strip()
        b = value2[value2.find(">=") + 2:].strip()
        result2 = a >= b

    elif "<=" in value2:
        a = value2[:value2.find("<=")].strip()
        b = value2[value2.find("<=") + 2:].strip()
        result2 = a <= b

    elif ">" in value2:
        a = value2[:value2.find(">")].strip()
        b = value2[value2.find(">") + 1:].strip()
        result2 = a > b

    elif "<" in value2:
        a = value2[:value2.find("<")].strip()
        b = value2[value2.find("<") + 1:].strip()
        result2 = a < b


    result = result1 and result2
    print("Your answer is:", result)


elif "or" in calculation:
    value1 = calculation[:calculation.find("or")].strip()
    value2 = calculation[calculation.find("or") + 2:].strip()

    result1 = False
    result2 = False

    if "==" in value1:
        a = value1[:value1.find("==")].strip()
        b = value1[value1.find("==") + 2:].strip()
        result1 = a == b

    elif "!=" in value1:
        a = value1[:value1.find("!=")].strip()
        b = value1[value1.find("!=") + 2:].strip()
        result1 = a != b

    elif ">=" in value1:
        a = value1[:value1.find(">=")].strip()
        b = value1[value1.find(">=") + 2:].strip()
        result1 = a >= b

    elif "<=" in value1:
        a = value1[:value1.find("<=")].strip()
        b = value1[value1.find("<=") + 2:].strip()
        result1 = a <= b

    elif ">" in value1:
        a = value1[:value1.find(">")].strip()
        b = value1[value1.find(">") + 1:].strip()
        result1 = a > b

    elif "<" in value1:
        a = value1[:value1.find("<")].strip()
        b = value1[value1.find("<") + 1:].strip()
        result1 = a < b

    if "==" in value2:
        a = value2[:value2.find("==")].strip()
        b = value2[value2.find("==") + 2:].strip()
        result2 = a == b


    elif "!=" in value2:
        a = value2[:value2.find("!=")].strip()
        b = value2[value2.find("!=") + 2:].strip()
        result2 = a != b

    elif ">=" in value2:
        a = value2[:value2.find(">=")].strip()
        b = value2[value2.find(">=") + 2:].strip()
        result2 = a >= b

    elif "<=" in value2:
        a = value2[:value2.find("<=")].strip()
        b = value2[value2.find("<=") + 2:].strip()
        result2 = a <= b

    elif ">" in value2:
        a = value2[:value2.find(">")].strip()
        b = value2[value2.find(">") + 1:].strip()
        result2 = a > b

    elif "<" in value2:
        a = value2[:value2.find("<")].strip()
        b = value2[value2.find("<") + 1:].strip()
        result2 = a < b

    result = result1 or result2
    print("Your answer is:", result)

else:
    print("Invalid input")
