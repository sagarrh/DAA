class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.student_class=None
    
    def display_atribbute(self):
        print(self.id)
        print(self.name)
        print(self.student_class)

stud= Student(12,"sagar")
stud.student_class="something"
stud.display_atribbute()
