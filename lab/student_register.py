print("Principle : hey, trisha(teacher) did you make register of marks for all students ? ")
print("Teacher : Yeah i am just working on that, i reach you after complete it.")

print("Enter in the class and ask for all students keep their result out !")
print("Teacher : Ok class i will ask all students that came one by one and gave their marks !")
print("Teacher : Ok who's first ?")

subjects = ["Math", "Science", "Social science", "English", "Gujarati", "Sanskrit", "Computer"]
register = []
total = 0
passed = 0
highest_percentage = 0
topper_name = 0
total_perc = 0
failed = 0

num_students = int(input("How many students? : "))

for i in range(1, num_students + 1):
    print(f"\nTeacher: Ok, who's next? Student {i}!")

    student = {}

    name = input("What's your name? : ")
    student["name"] = name
    student["Marks"] = {}

    for subject in subjects:
        mark = int(input(f"How many marks you got in {subject}? : "))
        student["Marks"][subject] = mark

    total = 0
    for mark in student["Marks"].values():
        total = total + mark

    total_sub = len(subjects) * 80
    student["percentage"] = round((total / total_sub) * 100, 2)

    register.append(student)
    print(f"{name}'s percentage: {student['percentage']}%")


print("Teacher : Ok who's next ?")
print("Class : Mam all are done !\n")

print("Ok than keep silence let do all your classwork i came in few minutes !")
print("Teacher : Sir i got all details in register !\n")

print("Principle: Ok so what are results of board of our class ?")

for student in register:
    if student["percentage"] > 40:
        passed = passed + 1

for student in register:
    if student["percentage"] < 40:
        failed = failed + 1

print(f"Teacher : Total {passed} pass and {failed} failed !\n")

print("Principle: Ok and who scored highest in our class ?")

for student in register:
    if student["percentage"] > highest_percentage:
        highest_percentage = student["percentage"]
        topper_name = student["name"]

print(f"Teacher : Mmm in class highest score of {topper_name} with {highest_percentage} !\n")

for student in register:
    total_perc = total_perc + student["percentage"]

total_class = len(register)
average = round(total_perc / total_class, 2)

print("Principle: Ok and what's average of our class ?")
print(f"Teacher : Mainly average is {average} !")
