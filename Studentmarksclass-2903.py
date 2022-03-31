
#student - attribute - name

class Student:
    def __init__(self,name):
        self.name = name
    def exam(self):
        i = 0
        while i == 0:
            name = input("Enter Name of Student: ")
            y = input("Enter marks of student: ")
            marks = {name:y}
            print("The marks of students till now is: ", marks)
            ans = input("do you want to continue? Y/N")
            if ans == "Y":
                continue
            else:
                break
class GradStudent(Student):
    def __init__(self,name):
        self.name = name
        super().
    def endsem(self):
        i = 0
        while i == 0:
            z = input("Enter the endsem marks for: ", name)
            mark = {name: z}
            print("Endsem marks is: ", mark)

            ans = input("do you want to continue? Y/N")
            if ans == "Y":
                continue
            else:
                break




student2 = GradStudent("Mohajit")
student2.exam()
