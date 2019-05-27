def list_of_count(word_list):
    l=[]
    for i in range(0,len(word_list)):
        s=len(word_list[i])
        l.append(s)
    
    return l

word_list=["COme","here"]
print(list_of_count(word_list))
