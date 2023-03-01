from math import sqrt

prompt = input('Enter an int grater than 2: ')
while prompt < '2' and not prompt.isdigit():
    prompt = input('Enter an int grater than 2: ')

while int(prompt) >= 2:
    prompt = round(sqrt(float(prompt)), 3)
    print(prompt)