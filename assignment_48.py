def find_correct(word_dict):
    c1=0
    c2=0
    c3=0
    for key in word_dict:
        if(key==word_dict[key]):
            c1+=1
        elif(len(key)==len(word_dict[key])):
            c=0
            for i in range(0,len(key)):
                if(key[i]!=word_dict[key][i]):
                    c+=1
            if(c<=2):
                c2+=1
            else:
                c3+=1
        else:
            c3+=1
    list=[]
    list.append(c1)
    list.append(c2)
    list.append(c3)
    return list

word_dict={"THREE": "TRICE", "MOST": "MICE", "GET": "GOT", "COME": "COME"}
print(find_correct(word_dict))
