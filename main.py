def is_valid_credit_card(card_number):
    """
    Validate credit card number length and IIN range, then calculate the checksum using the Luhn algorithm

    Args:
        card_number (str): Credit card number as a string

    Returns:
        str: Error message or 'Valid credit card number'
    """
    card_number = card_number.strip()

    if not card_number.isdigit():
        return 'Invalid characters in the credit card number'

    if len(card_number) < 12 or len(card_number) > 19:
        return 'Invalid card number length'

    iin_ranges = ['0', '1', '8600', '9704', '9860']
    if not any(card_number.startswith(iin) for iin in iin_ranges):
        return 'Invalid IIN range, unknown validation algorithm'

    # Luhn algorithm
    check_digit = int(card_number[-1])
    card_digits = list(map(int, card_number[:-1]))
    card_digits.reverse()

    for i in range(len(card_digits)):
        if i % 2 == 0:
            card_digits[i] *= 2
            if card_digits[i] > 9:
                card_digits[i] -= 9

    total = sum(card_digits) + check_digit

    if total % 10 == 0:
        return 'Valid credit card number'
    else:
        return 'Luhn algorithm validation failed'

try:
    user_input = input("Enter a credit card number: ")
    result = is_valid_credit_card(user_input)
    print(result)
except ValueError:
    print('Error: Input is not a valid number')
