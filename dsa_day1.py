*****assignment1*****
#DSA-Assgn-1

def merge_list(list1, list2):
    for i in range(0,len(list1)):
        for n, i in enumerate(list1):
            if i == None:
                list1[n] = "3"
    for i in range(0,len(list2)):
        for n, i in enumerate(list2):
            if i == None:
                list2[n] = "3"
    list2.reverse()
    list3=[]
    for i in range(0,len(list1)):
        list3.append(list1[i]+list2[i])
    s=(" ".join(list3))
    o=s.replace('3','')
    print(o)
list1=['T', 'sk', None, 'bl']
list2=['ue', 'is', 'y', 'he']
merge_list(list1, list2)


*******assignment3******
#DSA-Assgn-3

def check_double(list1,list2):
    new_list=[]
    r=[]
    for i in range(0,len(list2)):
        r.append(list2[i]/2)
    for i in range(0,len(list1)):
        for j in range(0,len(r)):
            if(list1[i]==r[j]):
                new_list.append(list1[i])
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25, 15]
list2=[6, 33, 50,31, 46, 78, 16,34]
print(check_double(list1, list2))




