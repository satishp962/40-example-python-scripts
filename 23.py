class Student:
    def __init__(self, name, dept, marks):
        self.name = name
        self.dept = dept
        self.marks = marks

    def get_name(self):
        return self.name

    def get_Dept(self):
        return self.dept

    def get_marks(self):
        return self.marks

    def get_stu(self):
        return "Name: " + self.name + ", Dept: " + self.dept + ", Marks: " + str(self.marks)

    def __str__(self):
        return "Name: " + self.name + ", Dept: " + self.dept + ", Marks: " + str(self.marks)

    def __eq__(self, stu_obj):
        if self.marks == stu_obj.marks:
            return True
        else:
            return False

stu = Student('Satish', 'Computer', 25)
stu1 = Student('Mark', 'Computer', 25)
stu2 = Student('Steve', 'Computer', 29)

if stu == stu1:
    print(stu.get_stu())
    print(stu1.get_stu())
elif stu1 == stu2:
    print(stu1.get_stu())
    print(stu2.get_stu())
elif stu2 == stu:
    print(stu.get_stu())
    print(stu2.get_stu())
else:
    print("No two students has same marks.")
