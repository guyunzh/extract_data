在字典中筛选所需的元素。可以用字典表达式的方法将满足条件的元素筛选出来。

同样可以利用itertools模块中的compress（）方法来实现。该函数接受一个可迭代的序列对象，以及一个有布尔值的可迭代对象。返回可迭代序列中对应布尔迭代对象中为True的元素。
与filter一样返回一个迭代器，可用list生成列表。