# def my_function(param_1):
#     pass
#
# my_function('string')

def numbers_sum(*var):
    suma = 0
    for item in var:
        suma = suma + item
    return suma

print(numbers_sum(1,2,3,4,5,6))


def numbers_dif(*var):
    dif = 0
    for item in var:
        dif = dif - item
    return dif

print(numbers_dif(1,2,3,4,5,6))
