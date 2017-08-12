#-*- coding:utf-8 -*-

def is_palindrome(n):
	return str(n)==str(n)[::-1] and len(str(n))>1


output=filter(is_palindrome,range(1000))
	
print(list(output))



