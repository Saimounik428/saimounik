def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]


string = "sky is blue my love is true"
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
