
def find_upper_and_lower(sentence):
    c1=0
    c2=0
    result_list=[]
    for i in sentence:
        if i.islower():
            c1=c1+1
        elif i.isupper():
            c2=c2+1
    result_list.append(c2)
    result_list.append(c1)
    return result_list

sentence="Welcome to Mysore"
print(find_upper_and_lower(sentence))
