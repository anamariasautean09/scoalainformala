# GRILE

# num_calls = 0
#
# def ex(x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return x * x
#
# print(ex(4))
# raspuns 16


# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())
# raspuns 1 1

# x = [1, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))
# raspuns 5

# x = (1,2,3)
# x[1] = 4
# print(x)
# raspuns TypeError - tuplu nu are item assigment

# a = [1,2,3]
# b = [4,5]
#
# print(a + b * 3)
# raspuns [1, 2, 3, 4, 5, 4, 5, 4, 5]

# x = [1, 2, 3, 4]
# print(x[-1:])
# raspuns [4]

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)
# raspuns [0,1,2]

# def ex(i):
#     for i in range(i):
#         return i
# x = ex(3)
# print(x)
# raspuns 0  - iese din for dupa prima iteratie

# a = range(10)
# y = [x*x for x in a if x%2 == 0]   # se iau numerele pare din intervalul 0-9 si dupa se face patratul lor
# print(y)
# raspuns [0, 4, 16, 36, 64]


# def make_acc():
#     return {"balance": 0}   #balance e cheia si 0 valoarea
#
# def deposit(account, amount):
#     account["balance"] += amount   #acount[0] = 10
#     return account['balance']
#
# a = make_acc()
# print(deposit(a, 10))
#
# raspuns 10

# "foo" + 2
# TypeError: can only concatenate str (not "int") to str

# try:
#     print('a')
# except:
#     print('b')
# else:
#     print('c')
# finally:
#     print('d')
#
# raspuns a c d

# for k in {'x': 1, 'y': 2}:   - se iau cheile nu valorile
#     print(k)
# raspuns x y

# print(list('python'))
# raspuns ['p', 'y', 't', 'h', 'o', 'n']

# def func(*args):
#     return 3 + len(args)
#
# print(func(4, 4, 4))
# raspuns 6

# count = (3, 2, 5, 4)
# while len(count) < 5:
#     count0 = count[0] + 1
#     print("Hello Geek")
#
# raspuns loop infinit in care se afiseaza Hello geek

# def ex(var):
#     for letter in "geeksforgeeks":
#         if letter == 'e' or letter == 's':
#             continue
#         print("current letter: ", letter)
#         var = 10
#         print(var)
#
# print(ex(20))
#
# none

# diferenta dintre liste si tupluri
# raspuns Listele sunt mutabile, tuplurile sunt imutabile

# def f(a, list=[]):
#     for i in range(a):
#         list.append(i*i)
#     print(list)
#
# f(3)
# f(2, [1,2,3])
# f(2)
# raspuns
# [0, 1, 4]
# [1, 2, 3, 0, 1]
# [0, 1, 4, 0, 1]

# list = ['1', '2', '3', '4', '5']
# print(list[12:])
# raspuns []

