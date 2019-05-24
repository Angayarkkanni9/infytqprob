#PF-Assgn-40
def is_palindrome(word):
    l=word.lower()
    if(l==l[-1::-1]):
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
