prices={
"ACME":45.32,
"AAPL":612.76,
"IBM":205.44,
"HPQ":37.21,
"FB":10.75
}
'''利用字典推导式来从字典中取出需要的数据'''

#Make a dictionary of all prices over 200
p1={key:value for key,value in prices.items() if value >200}
#print  {'AAPL': 612.76, 'IBM': 205.44}

#Make a dictionary of tech stocks
tech_names={'AAPL','IBM','HPQ','MSFT'}
p2={key:value for key ,value in prices.items() if key in tech_names}
#print   {'AAPL': 612.76, 'IBM': 205.44, 'HPQ': 37.21}

'''还可以用一个筛选工具是itertools.compress（），
它接受一个可迭代对象以及一个布尔选择器序列作为输入。
输入相应的布尔选择器为True的可迭代对象元素。
同filter一样，返回一个迭代器'''
from itertools import compress
list(compress(prices,[value>200 for value in prices.values()]))
#print ['AAPL', 'IBM']