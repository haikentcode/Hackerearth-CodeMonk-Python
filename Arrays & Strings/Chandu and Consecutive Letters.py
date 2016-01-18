'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
import sys;
x=input();
while x > 0 :
	y=raw_input();
	l=len(y);
	j=1;
	sys.stdout.write(y[0]);
	while j < l :
		if y[j]!=y[j-1] :
			sys.stdout.write(y[j]);
		j=j+1;
	print "";
	x=x-1;
