input = input("Enter a credit card number: ")
def checkCard(card):
    card = card.strip().replace(" ", "")

    if not card.isdigit():
        return 'Invalid object type, input is not a number'

    if len(card) < 12 or len(card) > 19:
        return 'Invalid card number length'
    
    if str(card).startswith(('0', '1', '8600', '9704', '9860')):
        return 'Invalid IIN range, unknown validation algorithm'
    
    #Luhn algorithm
    checkSum = 0
    for i in range(0, len(card) - 1, 2):
        checkSum += int(card[i])
    for i in range(1, len(card) - 1, 2):
        multiplied = int(card[i])*2
        for digit in str(multiplied):
            checkSum += int(digit)

    checkDigit = 10 - (checkSum % 10)
    if checkDigit != int(card[-1]):
        return 'Luhn algorithm validation failed'

    return 'Valid credit card number'

print(checkCard(input))