#PF-Prac-23
def divisible_by_sum(number):
    n=[int(x) for x in str(number)]
    if(number%sum(n)==0):
        return True
    else:
        return False
    
number=42
print(divisible_by_sum(number))
