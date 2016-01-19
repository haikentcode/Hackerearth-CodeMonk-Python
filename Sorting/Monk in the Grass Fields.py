import Queue as Q
t=input();
while t > 0:
	t-=1;
	n,k=map(int,raw_input().split());
	r=Q.PriorityQueue();
	c=Q.PriorityQueue();
	A=[[0]*n for i in range(n)];
	for i in range(n):
		A[i]=map(int,raw_input().split());
	B=[0]*n;
	C=[0]*n;
	for i in range(n):
		for j in range(n):
			B[i]+=A[i][j];
			C[j]+=A[i][j];
	for i in range(n):
		r.put(B[i]);
		c.put(C[i]);
	usingRows=[0]*(k+1);
	usingCols=[0]*(k+1);
	usingRows[0] = 0;
	usingCols[0] = 0;
	for i in range(1,k+1):
		rt = r.get();
		ct = c.get();
		usingRows[i] = usingRows[i-1] + rt;
		usingCols[i] = usingCols[i-1] + ct;
		r.put(rt + n);
		c.put(ct + n);
	s=1000000000;
	for i in range(k+1):
		s=min(s,usingRows[i] + usingCols[k-i] + i*(k-i));
	print s;
