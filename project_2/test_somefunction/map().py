"""
map(function, iterable)

> function -- 函数
> iterable -- 序列
map函数的第一个参数是一个函数，第二个参数是一个序列，里面的每个元素作为函数的参数进行计算和判断。函数返回值则被作为新的元素存储起来。
"""
def add(x):
    return x**2			#计算x的平方

lists = range(11)       #创建包含 0-10 的列表
a = map(add,lists)      #计算 0-10 的平方，并映射
print(a)                # 返回一个迭代器：<map object at 0x0000025574F68F70>
print(list(a))          # 使用 list() 转换为列表。结果为：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 使用lambda匿名函数的形式复现上面的代码会更简洁一些
print(list(map(lambda x:x**2,range(11))))   # 结果为：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
