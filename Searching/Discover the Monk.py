from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
n,q=map(int,raw_input().split());
A=map(int,raw_input().split());
A.sort();
while q > 0:
	q-=1;
	w=input();
	a=binary_search(A, w, 0, n);
	if a==-1:
		print "NO";
	else:
		print "YES";
