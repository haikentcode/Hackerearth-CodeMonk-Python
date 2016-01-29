s=raw_input();
x=len(s);
A=[0]*(x+1);
for i in range(x):
	A[i+1]=A[i]+ord(s[i])-ord('a');
t=input();
while t > 0:
	t-=1;
	l1,r1,l2,r2=map(int,raw_input().split());
	f=A[r1]-A[l1-1];
	q=A[r2]-A[l2-1];
	if(s[l1-1]==s[l2-1] and f==q):
		print "Yes";
	else :
		print "No"
