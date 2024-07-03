filename=input("enter the file name")
try:
    with open(filename,'r') as file:
        content=file.read()
        print("content of the file:")
        print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("the same ")
except Exception as e:
    print("an error occured")