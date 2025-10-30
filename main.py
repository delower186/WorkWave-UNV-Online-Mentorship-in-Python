# name = "Jahid"
# age = 20
# address = "Bogura"

# print(f"I am {name}, age {age} and I live in {address}")


# name = input("Enter you name & hit enter key")
# age = input("Enter you age & hit enter key")
# address = input("Enter you address & hit enter key")

# dict

# profile = {"name" : "John", "age" : 36, "address": "Bogura"}
# x = ["John", 36, "Bogura"]
#
# print(profile['address'])
# print(x[2])

# print(f"I am {profile}, age {age} and I live in {address}")

# 4th class

# Arithmetic Operators

# x = 15
# y = 4

# print(x + y) # 19
# print(x - y) # 11
# print(x * y) # 60
# print(x / y) # 3.75
# print(x % y) # 3
# print(x ** y) # 15 x 15 x 15 x 15 = 50, 625
# print(x // y) # 3


# Assignment Operators

# x += 3
# y = x +3
# print(x)
# print(y)

# Comparison Operators

# x = 5
# y = 3
#
# print(x == y) # false
# print(x != y) # true
# print(x > y) # true
# print(x < y) # false
# print(x >= y) # true
# print(x <= y) # false

# Logical Operators

# x = 5

# print(x > 0 and x < 10) # true

# print(x < 5 or x < 4) # false

# var = not (x < 5 and x < 10)  # false

# print(var)


# apple = 40
# orange = 50
# melon = 45
#
# if apple > orange:
#     print("Demand will rise for Orange")
# elif melon > orange:
#     print("Demand will rise for Orange")
# else:
#     print("Demand will rise for lowest in stock")

students = {
    "Galib": {
        "Bangla": 79,
        "English": 85
    },
    "Himel": {
        "Bangla": 95,
        "English": 76
    },
    "arman": {
        "Bangla": 75,
        "English": 76
    }
}


rasel = {
    "Bangla" : 79,
    "English": 85
}

gpa_scale = {
    "A+": range(80, 100),
    "A" : range(70, 89),
    "A-": range(60, 69),
    "B+": range(50, 59)
}

def generate_gpa(name, numbers):
    total = numbers['Bangla'] + numbers['English']

    average = total / len(numbers)
    average = int(average)

    print(f"{name}'s Overall Grade : {check_grade(average)}, Grade in Bangla: {check_grade(numbers['Bangla'])}, Grade in English: {check_grade(numbers['English'])}")


def check_grade(number):
    if number in gpa_scale['A+']:
        return "A+"
    elif number in gpa_scale['A']:
        return "A"
    elif number in gpa_scale['A-']:
        return "A-"
    elif number in gpa_scale['B+']:
        return "B+"
    else:
        return "FAiled"

# generate_gpa(rasel)

# for student in students:
#     generate_gpa(student, students[student])


fruits =  ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "apple":
        print(f"Please give a glass of {fruit} guice.")
    elif fruit == "banana":
        continue
    elif fruit == "cherry":
        print(f"Please give a plate of {fruit}.")
