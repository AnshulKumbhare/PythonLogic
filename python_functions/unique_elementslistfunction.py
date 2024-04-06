"""
Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
"""

l = [1, 2, 3, 3, 3, 3, 4, 5]


def unique_list(l):
    u_l = []
    for i in l:
        if (l.count(i) == 1) and i not in u_l:
            u_l.append(i)
        else:
            if (l.count(i) > 1) and (i not in u_l):
                u_l.append(i)

    return u_l

print(unique_list(l))
