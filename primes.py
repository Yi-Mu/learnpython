#-*- coding: utf-8 -*-
#埃氏筛法

#定义一个从3开始的奇数序列;
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

#定义一个筛选函数;
def _not_divisible(n):
	return lambda x: x%n>0
		
#定义一个生成器，不断返回下一个素数;
def primes():
	yield 2
	it=_odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(_not_divisible(n),it)

#primes()是一个无限序列，调用时需要设置一个退出循环的条件(需要输出的最大的素数);
number=int(input('Please enter the maximum integer: '))
for n in primes():
	if n<number:
		print(n)
	else:
		break
		

