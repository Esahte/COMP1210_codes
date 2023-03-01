def isArmstrong(num):
    sumOfNums = []
    for i in num:
        sumOfNums.append(int(i)**len(num))
    return sum(sumOfNums) == int(num)

prompt = input('Enter a number: ')

# while prompt != 'end':
#     if isArmstrong(prompt):
#         print('This is an armstrong number.')
#     else:
#         print('This is not an armstrong number.')
#     prompt = input('Enter a number: ')


armstrongNums = []

for j in range(100, int(prompt)):
    if isArmstrong(str(j)):
        armstrongNums.append(j)

print(armstrongNums)


