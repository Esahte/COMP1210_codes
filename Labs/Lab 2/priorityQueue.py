# def get_pos(el, lst):
#     if not lst:
#         return 0
#     elif el[0] < lst[0][0]:
#         return 0 + get_pos(el, [])
#     return 1 + get_pos(el, lst[1:])

def get_pos(el, lst):
    return 0 if el[0] < lst[0][0] else 1 + get_pos(el, lst[1:])

def enqueue_p(el, queue):
    queue[1].insert(get_pos(el, queue[1]), el)


# print(get_pos((4,"f"),[(1,"g"),(2,"r"),(5,"t"),(6,"e")]))
# print(get_pos((1,"t"),[(1, "a"),(2, "r")]))
enqueue_p((4,"f"), queue1 := ('queue', [(1,"g"),(2,"r"),(5,"t"),(6,"e")]))
print(queue1)