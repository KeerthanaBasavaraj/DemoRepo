#The below program is to check whether the number is Armstrong number or not

def armstrong_number(user_number):
    # Initializing Sum and Number of Digits
    n_power_digits_sum = 0
    number_of_digits = 0

    # Calculating Number of individual digits
    user_number_copy = user_number
    while user_number_copy > 0:
        number_of_digits = number_of_digits + 1
        user_number_copy = user_number_copy // 10

    # Finding Armstrong Number
    user_number_copy = user_number
    for i in range(1, number_of_digits + 1):
        digit = user_number_copy % 10
        n_power_digits_sum = n_power_digits_sum + (digit ** number_of_digits)
        user_number_copy //= 10
    return n_power_digits_sum

# End of Function

# User Input
user_number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

if (user_number == armstrong_number(user_number)):
    print("\n %d is Armstrong Number.\n" % user_number)
else:
    print("\n %d is Not a Armstrong Number.\n" % user_number)
