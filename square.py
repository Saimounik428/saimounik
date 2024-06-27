import math

def is_perfect_square(num):
    if num < 0:
        return False
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num


num = 25  
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
