def merge(A,l,r):
	mid=(l+r)>>1;
	Aux=[[0]*3 for i in range(r-l+1)];
	p=l;
	q=mid+1;
	i=0;
	j=0;
	while (p<=mid and q<=r):
		if (A[p][2]<A[q][2]):
			A[p][1]+=(q-mid-1);
			Aux[i]=A[p];
			p+=1;
		else :
			Aux[i]=A[q];
			q+=1;
		i+=1;
	while (p<=mid):
		A[p][1]+=(r-mid);
		Aux[i]=A[p];
		i+=1;
		p+=1;
	while (q<=r) :
		Aux[i]=A[q];
		i+=1;
		q+=1;
	for j in range(i):
		A[l]=Aux[j];
		l+=1;

def split(A,l,r):
	if l==r :
		return 0;
	mid=(l+r)>>1;
 	split(A,l,mid);
 	split(A,mid+1,r);
 	merge(A,l,r);

t=input();
while t > 0:
	t=t-1;
 	n=input();
 	A=[[0]*3 for i in range (n)]
 	B=[0]*(100000);
 	for i in range(n):
 		A[i][0]=i;#day
 		A[i][1]=0;#ans
 		A[i][2]=input();
 	split(A,0,n-1);
 	for i in range(n):
 		B[A[i][0]]=A[i][1];
 	for i in range(n):
 		print B[i],
 	print "";
