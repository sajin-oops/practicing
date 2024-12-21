#Python Iterators

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple =("sajin","lijin")
myit = iter(mytuple)
print(next(myit))
print(next(myit))

'''
O/P
apple
banana
cherry
sajin
lijin
'''