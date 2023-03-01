words = {}
prompt = input('Enter an incomplete word: ')
repCount = 0
for k, v in words.items():
    for i in range(len(prompt)):
        if prompt[i] == k[i]:
            repCount += 1
        else:
            break
    if repCount == len(prompt):
        print(v)
