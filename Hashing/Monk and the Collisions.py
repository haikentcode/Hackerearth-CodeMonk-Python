t=input();
while t > 0:
	t-=1;
	n=input();
	A=map(int,raw_input().split());
	B=[0]*10;
	i=0;
	while i < n:
		B[A[i]%10]+=1;
		i+=1;
	i=0;
	ans=0;
	while i < 10:
		ans+=B[i];
		if B[i] :
			ans-=1;
		i+=1;
	print ans;
