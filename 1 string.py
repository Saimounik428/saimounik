import string

def is_pangram(input_string):
    
    input_string = input_string.lower()
    
    
    alphabet_set = set(string.ascii_lowercase)
    
    
    for char in input_string:
        
        if char in alphabet_set:
            alphabet_set.remove(char)
        
        
        if not alphabet_set:
            return True
    
    
    return False


input_string = "a very good morning friends"
if is_pangram(input_string):
    print(f"'{input_string}' is a pangram.")
else:
    print(f"'{input_string}' is not a pangram.")
