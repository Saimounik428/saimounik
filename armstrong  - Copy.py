def is_armstrong(number):
    # Calculate the number of digits in the number
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the Armstrong sum
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    return armstrong_sum == number

# Example usage:
num = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
