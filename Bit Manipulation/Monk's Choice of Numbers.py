t = int(raw_input())
for i in range(t):
	n , k = map(int , raw_input().split())
	arr = map(int , raw_input().split())
	for i in range(n):
		count = 0
		n = arr[i]
		while n:
			n = n & (n-1)
			count += 1
		arr[i] =  count
	arr = sorted(arr , reverse = True)
 	print sum(arr[0:k])
