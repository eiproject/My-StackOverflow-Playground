import os

path = r"Your PATH"

fname = input("Enter first name: ")
lname = input("Enter last name: ")
city = input("Enter home city: ")

result = []
for filename in os.listdir(path):
    with open(os.path.join(path, filename)) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
        if ((fname in lines) and (lname in lines) and (city in lines)):
            # Desired output (filename was taken care of)
            print(filename, fname, lname, city)
            result.append(filename.split('.')[0])
        file.close()
print(result)