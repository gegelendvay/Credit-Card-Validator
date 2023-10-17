def checkCard(card):
    """
    Validate credit card number length and IIN range, then calculate the checksum using the Luhn algorithm

    Args:
        card (int): Credit card number

    Returns:
        str: Error message or 'Valid credit card number'
    """
    card = str(card)
    checkDigit = card[-1]

    if len(card) < 12 or len(card) > 19:
        return 'Invalid card number length'
    
    if str(card).startswith(('0', '1', '8600', '9704', '9860')):
        return 'Invalid IIN range, unknown validation algorithm'
    
    #Luhn algorithm
    checkSum = 0
    for i, digit in enumerate(reversed(card[:-1])):
        digit = int(digit)
        if i % 2 != 0:
            checkSum += digit
        elif digit >= 5:
            checkSum += digit*2-9
        else:
            checkSum += digit*2

    check = 10 - (checkSum % 10) if checkSum % 10 != 0 else 0

    if check != int(checkDigit):
        return 'Luhn algorithm validation failed'

    return 'Valid credit card number'

try:
    input = int(input("Enter a credit card number: "))
except ValueError:
    exit('Error: Input is not a number')

print(checkCard(input))