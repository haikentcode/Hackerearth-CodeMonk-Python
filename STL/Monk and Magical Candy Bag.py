import Queue as Q
t=input();
while t > 0:
	t-=1;
	n,k=map(int,raw_input().split());
	A=map(int,raw_input().split());
	q=Q.PriorityQueue();
	while n > 0:
		q.put(-1*A[n-1]);
		n-=1;
	ans=0;
	while k > 0:
		a=q.get();
		a=-1*a;
		ans+=a;
		a=a/2;
		q.put(-1*a);
		k-=1;
	print ans;
