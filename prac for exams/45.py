def copy(file1,file2):
    try:
        with open(file1,'r') as filea:
            content=filea.read()
        with open(file2,'w') as fileq:
            fileq.write(content)
    except Exception as e:
        print(e)

a=input("copy from")
b=input("copy to")
copy(a,b)

