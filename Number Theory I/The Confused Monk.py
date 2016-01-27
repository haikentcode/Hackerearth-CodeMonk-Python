def GCD(a,b):
	if(b==0):
		return a;
	return GCD(b,a%b);

n=input();
A=map(int,raw_input().split());
f=1;
con=1000000007;
for i in range(n):
	f=(f*A[i])%con;
gcd=A[0];
for i in range(1,n):
	gcd=GCD(gcd,A[i]);
	if(gcd==1):
		break;
	a=0;
if(gcd>1) :
	a=f;
	for i in range(1,gcd):
		f=(f*a)%con;
print(f);
