#PF-Assgn-36
def create_largest_number(number_list):
    
    number_list.sort(reverse=True)
    s = [str(i) for i in number_list] 
    res = int("".join(s)) 
    return res

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
