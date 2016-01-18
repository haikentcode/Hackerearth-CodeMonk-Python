'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)
x=input();
while x > 0:
	n,m=map(int,raw_input().split());
	y=[0]*n;
	z=[0]*(n+1);
	y[0]=input();
	z[0]=0;
	for i in range(n-1):
		y[i+1]=input();
		z[i+1]=z[i]+y[i];
	z[n]=z[n-1]+y[n-1]
	flag=0;
	for i in range(1,n+1) :
		k=z[i]-m;
		q=binary_search(z, k, 0, n);
		if(q!=-1) :
			flag =1;
			break;
	x=x-1;

	if flag == 1:
		print "YES";
	else :
		print "NO";
