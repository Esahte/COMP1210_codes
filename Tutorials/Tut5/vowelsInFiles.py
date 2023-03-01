with open('textSample.txt') as file:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowelCount = 0
    consonantCount = 0
    for i in file.readlines():
        for j in i:
            if j in vowels:
                vowelCount += 1
            elif j.isalpha():
                consonantCount += 1
    print(vowelCount, consonantCount)
