def armstrong_number(user_number):
    # Initializing Sum and Number of Digits
    username = "keerthana@repohunter.com"
    password = "qwerty"
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