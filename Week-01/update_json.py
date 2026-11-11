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
    
        students = load_students(filename)
        for student in students:
            if student["name"] == name:
                student["score"]= new_score
                save_students(filename,students)
                return True
        return False

save_students("students.json", students)

loaded = load_students("students.json")

assert loaded == students
assert update_student_score("students.json", "John", 95) is True

students = load_students("students.json")
assert students[1]["score"] == 95

assert update_student_score("students.json", "Ali", 80) is False


before = load_students("students.json")

assert update_student_score("students.json", "Ali", 80) is False

after = load_students("students.json")

assert before == after
print("All tests passed!")

