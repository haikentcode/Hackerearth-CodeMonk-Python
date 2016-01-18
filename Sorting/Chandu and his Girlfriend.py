'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
x=input();
while x > 0:
	x=x-1;
	n=input();
	a=map(int,raw_input().split());
	a.sort();
	while n > 0 :
		print a[n-1],
		n-=1;
	print "";
