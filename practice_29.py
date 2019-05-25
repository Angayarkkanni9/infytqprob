#PF-Prac-29
def exchange_list(number_list):
    l=[]
    s=[]
    k=len(number_list)//2
    for i in range(0,k):
        l.append(number_list[i])
    for i in range(k,len(number_list)):
        s.append(number_list[i])
        s.sort(reverse=True)
    number_list=s+l
    return number_list
     
number_list=[1,2,3,4,5,6,7,8,9,10]
print(exchange_list(number_list))
