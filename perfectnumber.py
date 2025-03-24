
def is_perfect(number):
    if number < 1:
        return False
    return sum(div for div in range(1, number) if number % div == 0) == number

print(is_perfect(28))  # Output: True
print(is_perfect(12))  # Output: False
