def check(arr, mid, k):
	nexta=arr[0]+mid;
	k-=1;
	for i in range(1,len(arr)):
		if (nexta+mid<arr[i]):
			if(k==0):
				return False;
			k-=1;
			nexta=arr[i]+mid;
	return True;
n,K=map(int,raw_input().split());
A=map(int,raw_input().split());
A.sort();
l=0
u=10000000
mid=0;
while l<=u :
	mid=(l+u)/2;
	if check(A,mid,K) :
		if not check(A,mid-1,K) :
			break;
	if (check(A,mid,K)) :
		u=mid-1;
	else :
		l=mid+1;
print(mid);
