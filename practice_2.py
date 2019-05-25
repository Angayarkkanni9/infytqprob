#PF-Prac-2
def bracket_pattern(input_str):
    c1=input_str.count("(")
    c2=input_str.count(")")
    if(input_str.startswith(")") and input_str.endswith("(")):
        return False
    if(c1==c2):
        return True
    elif(c1!=c2):
        return False
    
input_str="()((())())"
print(bracket_pattern(input_str))
