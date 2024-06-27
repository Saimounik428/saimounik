def is_prime(number):
    # Check if the number is less than or equal to 1
    if number <= 1:
        return False
    
    # Check for numbers 2 and 3 explicitly
    if number <= 3:
        return True
    
    # Check if number is divisible by 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    # Check for all numbers of the form 6k ± 1 up to sqrt(number)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Example usage:
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
