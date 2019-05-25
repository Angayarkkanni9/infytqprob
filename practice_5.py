def count_digits_letters(sentence):
    l=[]
    c1=0
    c2=0
    for i in sentence:
        if(ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122):
            c1+=1
        elif((ord(i)>=0 or ord(i)<=9) and not(i==" ")):            
            c2+=1
    l.append(c1)
    l.append(c2)
    return l

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))

