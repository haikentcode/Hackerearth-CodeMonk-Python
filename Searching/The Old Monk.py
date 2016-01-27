def binarysearch(b,n,i):
	le=len(b);
	mid=0;
	l=i;
	u=le-1;
	pos=0;
	while l<=u :
		mid=(l+u)/2;
		if b[mid]<n:
			u=mid-1;
		elif b[mid]>=n :
			pos=mid;
			l=mid+1;
	return pos;
t=input();
while t > 0:
	t-=1;
	n=input();
	A=map(int,raw_input().split());
	B=map(int,raw_input().split());
	ans=-1;
	for i in range(n):
		j=binarysearch(B,A[i],i);
		ans=max(ans, j-i)
	print(ans);
