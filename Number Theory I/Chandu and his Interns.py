import math;
def check(num):
	if(num==2 or num==3):
		return True;
	sqr=int(math.sqrt(num));
	for i in range(2,sqr+1):
		if(num%i==0):
			if(i*i==num):
				return True;
			else:
				return False;
	return True;

n=input();
while n >0:
	n-=1;
	p=input();
	if check(p) :
		print("NO");
	else :
		print("YES");
