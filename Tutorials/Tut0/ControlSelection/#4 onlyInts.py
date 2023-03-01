prompt = input('Input an integer: ')
while not prompt.isdigit():
    print('Error try again!')
    prompt = input('Input an integer: ')
print(prompt)