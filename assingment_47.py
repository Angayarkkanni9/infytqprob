#PF-Assgn-47
def encrypt_sentence(sentence):
    sentence=sentence
    s=""
    list=[]
    list=sentence.split(" ")
    for i in range(0,len(list)):
        if((i+1)%2!=0):
            a=list[i]
            list[i]=a[::-1]
        else:
            v=""
            c=""
            for j in list[i]:
                if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u"):
                    v+=j
                else:
                    c+=j
            list[i]=c+v
    for i in range(0,len(list)):
        s+=list[i]
        if(i!=len(list)-1):
            s+=" "
        
    return s

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
