def F(n):
	if(n < 2):
		return 1
	else:
		fib1 = 1
		fib2 = 1
		for i in range(2, n):
			fib3 = fib1 + fib2
			fib1 = fib2
			fib2 = fib3
		return fib3
		
print(F(0))
print(F(1))
print(F(7))
print(F(30))