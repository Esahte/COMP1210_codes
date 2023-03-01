name = 'Mario'
empty_name = ''

# temp_name = ''
# if empty_name:
#     temp_name = empty_name
# else:
#     temp_name = name
if temp_name := empty_name or name:
    print(temp_name)

people = ['Bryan', 'Tammy', 'Rango']
# n = len(people)
# if n <= 3: print(n)

if (n := len(people)) <= 3: print(n)

