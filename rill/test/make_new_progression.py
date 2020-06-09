# base testing for make new progression

# a progression is a tuple 
# take a tuple and item and an index
# insert item at index and return new tuple

a = ('a', 'b', 'c')
A = 'A'
B = 'B'
C = 'C'

def replace(tup, index, item):
    """index 0"""
    l = []
    for i in range(len(tup)):
        l.append(tup[i])
    l[index] = item
    new_tuple = tuple(l)
    return new_tuple

if __name__ == '__main__':
    new_list = replace(a, 0, 'X')
    print(new_list)
