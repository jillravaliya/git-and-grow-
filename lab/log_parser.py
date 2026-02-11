name = "jill"
age = 21
work = "Engineer"
hobby = "music,photography,coding"
pursuits = hobby.split(",")
routine = "programming"
daily_routine = routine.replace("programming", "coding")

print(f"Hi, my name is {name}, my age is {age}, and i work as an {work}")
print("My hobbies are basically ", pursuits)
print(f"But believe me my mostly time goes in {daily_routine} !\n")


filename = input("Paste here your files, i will ask you type ! : \n").strip().lower()

if filename.endswith(".txt"):
    print("These is a text file !\n")

elif filename.endswith(".log"):
    print("These is a log file !\n")

else :
    print("These filetype is unknown!")

your_data = filename.split()
print("Your input is : ", your_data)
print("But let see what your input try to say !\n")

permissions = your_data
print("Your permissions are : ", permissions[0])

hard_links = your_data
print("Your hard_links are : ", hard_links[1])

owner = your_data
print("Your owner are : ", owner[2])

group = your_data
print("Your group are : ", group[3])

size = your_data
print("Your size are : ", size[4])

date = your_data
print("Your date are : ", date[5])

month = your_data
print("Your month are : ", month[6])

time = your_data
print("Your time are : ", time[7])

filename = your_data
print("Your filename are : ", filename[8])
