students = [
    {'name': 'SOFA', 'ORT': 110, 'male': 'f'},
    {'name': 'ALEX', 'ORT': 98, 'male': 'm'},
    {'name': 'LINA', 'ORT': 120, 'male': 'f'},
    {'name': 'TIMUR', 'ORT': 75, 'male': 'm'},
    {'name': 'DIANA', 'ORT': 135, 'male': 'f'},
    {'name': 'ERLAN', 'ORT': 88, 'male': 'm'},
    {'name': 'NURA', 'ORT': 147, 'male': 'f'},
    {'name': 'ALI', 'ORT': 30, 'male': 'm'},
    {'name': 'ZARA', 'ORT': 123, 'male': 'f'},
    {'name': 'OMAR', 'ORT': 101, 'male': 'm'},
    {'name': 'JANA', 'ORT': 111, 'male': 'f'},
    {'name': 'RUSLAN', 'ORT': 67, 'male': 'm'},
    {'name': 'MIRA', 'ORT': 89, 'male': 'f'},
    {'name': 'NURIS', 'ORT': 144, 'male': 'm'},
    {'name': 'LANA', 'ORT': 26, 'male': 'f'},
    {'name': 'DASTAN', 'ORT': 76, 'male': 'm'},
    {'name': 'AYNA', 'ORT': 8, 'male': 'f'},
    {'name': 'BAKT', 'ORT': 105, 'male': 'm'},
    {'name': 'ELINA', 'ORT': 114, 'male': 'f'},
    {'name': 'SAMAT', 'ORT': 83, 'male': 'm'},
    {'name': 'NINA', 'ORT': 134, 'male': 'f'},
    {'name': 'ASLAN', 'ORT': 24, 'male': 'm'},
    {'name': 'GULYA', 'ORT': 29, 'male': 'f'},
    {'name': 'ISLAM', 'ORT': 22, 'male': 'm'},
    {'name': 'RAISA', 'ORT': 149, 'male': 'f'},
    {'name': 'ARSLAN', 'ORT': 10, 'male': 'm'},
    {'name': 'SARA', 'ORT': 126, 'male': 'f'},
    {'name': 'TALGAT', 'ORT': 87, 'male': 'm'},
    {'name': 'AINURA', 'ORT': 21, 'male': 'f'},
    {'name': 'YERLAN', 'ORT': 53, 'male': 'm'},
    {'name': 'ALINA', 'ORT': 117, 'male': 'f'},
    {'name': 'AZAMAT', 'ORT': 109, 'male': 'm'}
]

def distribute_students(students_list):
    distribution = {
        'university': [],
        'college': [],
        'army': [],
        'marriage': []
    }

    for student in students_list:
        ort_score = student['ORT']
        gender = student['male']
        name = student['name']

        if ort_score > 110:
            distribution['university'].append(name)
        elif 40 <= ort_score <= 109:
            distribution['college'].append(name)
        elif ort_score < 40:
            if gender == 'm':
                distribution['army'].append(name)
            else:
                distribution['marriage'].append(name)

    return distribution

student_distribution = distribute_students(students)

print("Студенты, поступившие в университет:", student_distribution['university'])
print("Студенты, поступившие в колледж:", student_distribution['college'])
print("Парни, ушедшие в армию:", student_distribution['army'])
print("Девушки, вышедшие замуж:", student_distribution['marriage'])
