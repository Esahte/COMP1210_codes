def isPositive(num):
    if num>0: return 'Positive'
    elif num<0: return 'Negative'
    return 'Zero'

prompt = input('Enter an integer: ')
while prompt != 'end':
    print(isPositive(int(prompt)))
    prompt = input('Enter an integer: ')