from sets import Set
t=input()
while t > 0:
	t-=1;
	n,m=map(int,raw_input().split());
	A=map(int,raw_input().split());
	i=0;
	S=Set();
	while i < n:
		S.add(A[i]);
		i+=1;
	while i < m+n:
		if(A[i] in S):
			print "YES";
		else :
			print "NO";
			S.add(A[i]);
		i+=1;
