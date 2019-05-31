from difflib import SequenceMatcher
s1=input()
s2=input()
match=SequenceMatcher(None,s1,s2).find_longest_match(0,len(s1),0,len(s2))
if(match.size!=0):
    print(s1[match.a:match.a+match.size])
else:
    print("")
