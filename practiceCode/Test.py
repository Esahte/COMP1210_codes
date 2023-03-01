
# location = Island(10, 12, 6)
# moose = Animal(1,3,location,'moose')
# rabit = Animal(9, 4, location, 'rabit')
# location.register(moose)
# location.register(rabit)
# moose.move()
# # location.remove(rabit)
# # location.init_animals(6, 12)
# rabit.move()
# print(location)

# def something(x, y):
#     lst = [1, 2, 3, 4, 5]
#     if x >= len(lst) or len(lst)<= y:
#         return 0
#     elif lst[x] == 1:
#         return 1
#     return 0
#
# print(something(5, 4))

# island = Island(10, 6, 12)
# animal = Prey(0, 0, island, 'moose')
# island.register()

string = 'This class is fun'

# var = [x for x in string if x != ' ']
#
# print(var)
#
# x = [1, 2, 4, 5]
# # y = [i for i in x]
# # y = x
# y = ''.join()
#
# print(y)

# A = [10, 20, 30, 40, 50]
# B = []
# for i in A:
#     if A.index(i) == 0: B.append(i + A[A.index(i)+1])
#     elif i == A[-1]: B.append(i + A[A.index(i)-1])
#     else: B.append(i + A[A.index(i)+1] + A[A.index(i)-1])
#
# print(B)
# num = int(input('Enter number: '))
# factor = sum(x for x in range(1, num+1) if 6%x == 0)
#
#
# print(factor)


# courseCodes = [ 'COMP1210' , 80 , 'COMP1215' , 60 ,
# 'COMP2210' , 50 , 'COMP1205' , 60 , 'FOUN2003' , 85 , 'COMP2220' , 80]
# courses = [tuple(courseCodes[i:i+2]) for i in range(0, len(courseCodes), 2)]
# for i in range(len(grades := (90, 80, 95, 75, 32))):
#     courses.append((courseCodes[i], grades[i]))

# def compute_letter_grade(num):
#     grades = {'A+': range(100, 91, -1), 'A': range(90, 81, -1), 'A-': range(80, 71, -1), 'B+': range(70, 61, -1),
#               'B': range(60, 51, -1), 'B-': range(50, 41, -1), 'C+': range(40, 31, -1), 'C': range(30, 21, -1),
#               'C-': range(20, 11, -1), 'D': range(10, 1, -1), 'F': range(0, 0, -1)}
#     return ''.join(k for k, v in grades.items() for i in v if num == i)
#
# print(courses)

dictionary = {1: [1, 2], 2:[3, 4]}
dictionary[1].append(3)
print(dictionary)