def sum_of_elements(num_list,number):
    p=[]
    s=[]
    if(num_list[0]==0):
        return 0
    if(num_list[-1]==number):
        return 0
    for i in range(len(num_list)):
        if(num_list[i]==number):
            p.append(num_list[i])
            p.append(num_list[i+1])
            p.append(num_list[i-1])
    for i in p:
        if i in num_list:
            num_list.remove(i)
    result_sum=0
    if(len(num_list)==0):
        return 0
    for i in range(0,len(num_list)):
        result_sum=result_sum+num_list[i]
    return result_sum
    
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list,number))
