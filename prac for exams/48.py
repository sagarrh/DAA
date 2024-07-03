def store_student_data(filename):
    try:
        with open(filename, 'a') as file:
            name = input("Enter student name: ")
            roll_number = input("Enter student roll number: ")
            file.write(name + ',' + roll_number + '\n')
        print("Student data stored successfully.")
    except Exception as e:
        print("An error occurred:", e)

def read_student_data(filename):
    try:  
        with open(filename, 'r') as file:
            print("Student data stored in the file:")
            for line in file:
                name,roll_no=line.strip().split(',')
                print("Name:",name,"|Roll Number: ",roll_no)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

filename = "student_data.txt"
store_student_data(filename)
read_student_data(filename)
