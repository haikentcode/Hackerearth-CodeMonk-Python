t=input();
while t > 0:
	t-=1;
	n=input();
	f=0;
	A=[0]*1000009;
	while n > 0:
		n-=1;
		m,k=map(int,raw_input().split());
		A[m]+=1;
		if A[k] > 0:
			A[k]-=1;
		else :
			f+=1;
	print f;
