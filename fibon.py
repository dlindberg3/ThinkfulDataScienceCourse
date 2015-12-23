fibonarray = [1,1]
for i in range(2,30):
	fibonarray.append(fibonarray[i - 1] + fibonarray[i - 2])
print(fibonarray)