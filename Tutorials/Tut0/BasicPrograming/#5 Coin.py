def coin(num):
    # users initial number
    cent = num
    # dictionary of coins
    coins = {'quarter':0, 'dime':0, 'nickel':0, 'penny':0}

    # increments values of keys in dictionary
    while cent != 0:
        while cent>=.25:
            coins['quarter'] += 1
            cent = round(cent-.25, 2)
        while cent>=.1:
            coins['dime'] += 1
            cent = round(cent-.1, 2)
        while cent>=.05:
            coins['nickel'] += 1
            cent = round(cent-.05, 2)
        while cent>=.01:
            coins['penny'] += 1
            cent = round(cent-.01, 2)

    # list to store keys in dictionary with values
    coinLst = []
    # iterates through dictionary to extract keys with values
    for (k, v) in coins.items():
        if v != 0:
            coinLst.append(k)

    # stores initial list size
    initialLen = False
    if len(coinLst) == 1: initialLen = True

    # creates statement to be returned
    statement = f'{num} cents is '
    while len(coinLst)>1:
        if coins[coinLst[0]] > 1 and coinLst[0] == 'penny': statement += f'{coins[coinLst.pop(0)]} pennies, '
        elif coins[coinLst[0]] > 1: statement += f'{coins[coinLst[0]]} {coinLst.pop(0)}s, '
        else: statement += f'{coins[coinLst[0]]} {coinLst.pop(0)}, '
    if coins[coinLst[0]] > 1 and coinLst[0] == 'penny' and initialLen: statement += f'{coins[coinLst.pop(0)]} pennies'
    elif coins[coinLst[0]] == 1 and initialLen: statement += f'{coins[coinLst[0]]} {coinLst.pop(0)}'
    elif coins[coinLst[0]] > 1 and initialLen: statement += f'{coins[coinLst[0]]} {coinLst.pop(0)}s'

    elif coins[coinLst[0]] > 1 and coinLst[0] == 'penny': statement += f'and {coins[coinLst.pop(0)]} pennies'
    elif coins[coinLst[0]] > 1: statement += f'and {coins[coinLst[0]]} {coinLst.pop(0)}s'
    else: statement += f'and {coins[coinLst[0]]} {coinLst.pop(0)}'

    return statement


prompt = float(input('Enter a coin value: '))
print(coin(prompt))