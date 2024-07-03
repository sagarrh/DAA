#WAP to copy contents of 1 file to another Let user specify name of source and destination files  


def copy(form,to):
    try:
        with open(form,'r') as file:
            content=file.read()
        with open(form,'a') as file1:
            file1.write(content)
    except Exception as e:
        print("Exception is ",e)



form=input("enter the source to copy form")
to=input("enter where to paste it ")

copy(form,to)
