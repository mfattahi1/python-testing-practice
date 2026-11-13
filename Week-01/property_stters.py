class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = 0
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if type(value) is int:
            if 0 <= value <= 100:
                self._score = value
            

student = Student("Sara", 70)

student.score = False
assert student.score == 70

student.score = -20
assert student.score == 70

student.score = 100
assert student.score == 100

student2 = Student("John", 150)
assert student2.score == 0
student = Student("John", 150)

assert student.score == 0

student.score = 85
assert student.score == 85

print("All tests passed!")