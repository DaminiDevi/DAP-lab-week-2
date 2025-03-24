def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(-9876))  # Output: 30
