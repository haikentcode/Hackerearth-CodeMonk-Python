import Queue as Q
def check(n):
	c=0;
	while(n>0):
		if((n&1)==1):
			c+=1;
		n>>=1;
	return c;
t=input();
while t > 0:
	t-=1;
	n=input();
	A=map(int,raw_input().split());
	h=[0]*65;
	i=0;
	while i < 65:
		h[i]=Q.Queue();
		i+=1;
	i=0;
	while i < n:
		x=check(A[i]);
		h[x].put(A[i]);
		i+=1;
	i=0;
	for i in range(65):
		while not h[i].empty() :
			print h[i].get(),
	print "";
