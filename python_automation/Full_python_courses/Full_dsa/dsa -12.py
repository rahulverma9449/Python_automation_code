#Map()

def cube(x):
     return x*x*x
print(cube(2))
#
l = [1,2,4,6,4,3]

newl = list(map(lambda x: x*x*x, l))
print(newl)

# Filter finction()
l2 = [1,2,4,6,4,3]

newnewl2 = list(filter(lambda x: x>2, l2))
print(newnewl2)

#newnewl = list(filter(filter_function, l))



