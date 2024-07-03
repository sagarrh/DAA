#Python – Get number of characters, words, spaces and lines in a file



def getinfo(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
            num_char=len(content)
            num_words=len(content.split())
            num_spaces=content.count(' ')
            num_lines=content.count('\n')+1
            return num_char,num_lines,num_spaces,num_spaces
    except Exception as e:
        print(e)








filename=input("enter the filename ")

char,lines,spaces,words=getinfo(filename)
print(lines,spaces,words,char)
