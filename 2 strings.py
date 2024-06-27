from collections import Counter

def are_anagrams(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    
    
    if counter1 == counter2:
        return True
    else:
        return False


str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  
