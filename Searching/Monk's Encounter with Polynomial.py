t=input();
while t > 0:
	t-=1;
	a,b,c,d=map(int,raw_input().split());
	if(c==d):
		print 0;
	else :
		x=1;
		while True :
			z=a*x*x+b*x+c;
			if z > d:
				break;
			else :
				x=x*2;
		y=x/2;
		mid=0;
		while y<x:
			mid=(y+x)//2;
			if((a*mid*mid+b*mid+c)==d):
				break;
			if((a*mid*mid+b*mid+c)<d):
				y=mid+1;
			else :
				x=mid;
		if((a*mid*mid+b*mid+c)>=d):
			print mid;
		else:
			print x;
		
