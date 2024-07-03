def count_letter(filename,letter):
    try:
        with open(filename,'r') as file:
            content=file.read()
        countofletter=content.count(letter)
        print("these many times",countofletter)
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured:",e)

a=r"C:\Users\harso\OneDrive\Desktop\Python\prac for exams\a.txt"
b='e'
count_letter(a,b)
