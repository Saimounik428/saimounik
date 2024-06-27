def is_perfect_number(num):
    if num <= 0:
        return False
    
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors == num


num = 28  
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
