'''
实现分段执行
'''

def fun():
    for i in range(10):
        yield i

my =fun()
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))

