def square(num):
    return num**2


def splicer(mystring):
    return 'EVEN' if len(mystring) % 2 == 0 else mystring[0]


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums):  # or list(map(square, my_nums) for list form
    print(item)
names = ['Andy', 'Eve', 'Sally']
meme = list(map(splicer, names))  # note no parentheses on splicer
print(meme)
my_nums = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, my_nums)))
print(list(map(lambda num: num**2, my_nums)))  # this is a lambda expression (inline function)
