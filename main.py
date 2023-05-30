input = input("Enter a credit card number: ")

def check_card(card):
    card = card.strip().replace(" ", "")

    if not card.isdigit():
        return 'Card number is not a digit'

    if len(card) < 12 or len(card) > 19:
        return 'Card number length is invalid'

    return 'Valid credit card number'

print(check_card(input))