from data_structure import get_name

# Dictionary
# if, elif, else condtions
# range
# custom function

rasel = {
    "Bangla" : 55,
    "English" : 60
}

rakib = {
    "Bangla" : 67,
    "English" : 55
}

gpa_scale = {
    "A+": range(80, 100),
    "A" : range(70, 89),
    "A-": range(60, 69),
    "B+": range(50, 59)
}

def generate_gpa(numbers):
    total = numbers['Bangla'] + numbers['English']

    average = total / len(numbers)

    print(f"Overall Grade : {check_grade(average)}, Grade in Bangla: {check_grade(numbers['Bangla'])}, Grade in English: {check_grade(numbers['English'])}")


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

generate_gpa(rakib)