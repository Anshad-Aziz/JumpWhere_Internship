from collections import Counter

def arg(s1,s2):
    if len(s1)!=len(s2):
        return False
    return Counter(s1)==Counter(s2)    
    
s1="slient"
s2="listen"
print(arg(s1,s2))