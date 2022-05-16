def two_times(x):
	return x*3

result = map(two_times, [3,6,9,12])
print(type(result))
print(list(result))

