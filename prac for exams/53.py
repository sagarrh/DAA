class Invalidmarks(Exception):
    def __init__(self,marks):
        super().__init__(f"Marks obtained are '{marks}'")




def validate_marks(marks):
    if marks>100:
        raise Invalidmarks(marks)
    else:
        print("marks are valid")





try:
    marks=int(input("Enter marks scored by the student"))
    validate_marks(marks)
except Exception as e:
    print(e)