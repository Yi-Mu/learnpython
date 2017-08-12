#-*- coding: utf-8 -*-
#����ɸ��

#����һ����3��ʼ����������;
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

#����һ��ɸѡ����;
def _not_divisible(n):
	return lambda x: x%n>0
		
#����һ�������������Ϸ�����һ������;
def primes():
	yield 2
	it=_odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(_not_divisible(n),it)

#primes()��һ���������У�����ʱ��Ҫ����һ���˳�ѭ��������(��Ҫ�������������);
number=int(input('Please enter the maximum integer: '))
for n in primes():
	if n<number:
		print(n)
	else:
		break
		

