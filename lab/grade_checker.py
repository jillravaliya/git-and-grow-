percentage = int(input("Enter your percentage: "))

if percentage >= 90:
    print("Grade : A")
    if percentage > 95:
        print("Grade : A+")
elif percentage >= 80:
    print("Grade : B")
    if percentage > 85:
        print("Grade : B+")
elif percentage >= 70:
    print("Grade : c")
elif percentage >= 33:
    print("Grade : D")
    if percentage > 50:
        print("try harder !")
    elif percentage < 50:
        print("you're near to fail !")
else:
    print("Better luck next time, you're fail !")

print("congratulations bro!, you perform very well in your exam")
