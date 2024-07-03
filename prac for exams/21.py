

def capitalize(a):
    words=a.split()
    capitalized_words=[word.capitalize() for word in words]
    cap_sentence= ' '.join(capitalized_words)
    return cap_sentence


    



sentenc=" hii my name is sagar"

print(capitalize(sentenc))