from random import randint

sumOfNums = 0
while sumOfNums <= 1000:
    sumOfNums += sum([randint(1, 20), randint(1, 20)])
print(sumOfNums)