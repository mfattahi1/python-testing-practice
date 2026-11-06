students = [
    {"name": "Anna", "score": 78},
    {"name": "Sara", "score": 91},
    {"name": "Omid", "score": 54},
    {"name": "John", "score": 85}
]

def analyze_students(students):
    sum = 0
    average=0
    if not students:
            return {"average":0, "passed": 0, "top_student":None}
    highest_score=students[0]["score"]
    top_student=students[0]["name"]
    passed_count=0
    
    for student in students:
        sum += student["score"]
        if student["score"] >= 60:
            passed_count +=1
        if student["score"] > highest_score:
            top_student = student["name"]
            highest_score= student["score"]

    average = (sum / len(students))
    our_dict = {"average": average, "passed": passed_count, "top_student":top_student}
    return our_dict

assert analyze_students(students) == {
    "average": 77.0,
    "passed": 3,
    "top_student": "Sara"
}

assert analyze_students([]) == {
    "average": 0,
    "passed": 0,
    "top_student": None
}

assert analyze_students([
    {"name": "Ali", "score": 90},
    {"name": "Reza", "score": 90}
])["top_student"] == "Ali"

assert analyze_students([
    {"name": "Ali", "score": 40}
])["passed"] == 0

print("All fine!")