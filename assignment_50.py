def sms_encoding(data):
    new_list = []
    final_list = []
    final_ans = ""
    new_list = data.split(" ")
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    for i in range(0,len(new_list)):
        count = 0
        string = ""
        for j in range(0,len(new_list[i])):
            if new_list[i][j] in vowels:
                count = count + 1
                if(count==len(new_list[i])):
                    final_list.append(new_list[i])
            else: 
                string = string + new_list[i][j]
        if(len(string)!=0):
            final_list.append(string)    
    final_ans = " ".join(final_list)
    return final_ans
data="GOOD DAYS AND BAD DAYS"
print(sms_encoding(data))

