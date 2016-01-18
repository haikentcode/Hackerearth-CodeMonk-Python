'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
x=input();
while x > 0 :
	y=raw_input()
	y=y[::-1]
	print y
	x=x-1
