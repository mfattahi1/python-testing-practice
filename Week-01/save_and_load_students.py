import json
students = [
    {"name": "Anna", "score": 90},
    {"name": "John", "score": 75},
    {"name": "Sara", "score": 85}
]


def save_students(filename, students):
    
    with open(filename, "w") as file:
        json.dump(students,file, indent=4)


def load_students(filename):
    with open(filename, "r") as file:
        students = json.load(file)
    return students

def update_student_score(filename, name, new_score):
    with open(filename, "w") as file:
        students = json.load(filename)
        for student in students:
            if student["name"] == name:
                json.dump(student["score"], new_score)
                return True
        return False

save_students("students.json", students)

loaded = load_students("students.json")

assert loaded == students
print("All tests passed!")