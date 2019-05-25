#PF-Prac-7
def seed_no(number,ref_no):
    n=[int(x) for x in str(number)]
    product=1
    for i in range(0,len(n)):
        product+product*n[i]
    s=product*number
    if(s==ref_no):
        return True
    else:
        return False
number=123
ref_no=738
print(seed_no(number,ref_no))
