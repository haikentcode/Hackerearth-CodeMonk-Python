def merge(a,l,m,r):
      L=a[l:m+1]
      R=a[m+1:r+1]
      i=0
      j=0
      k=l
      while i<len(L) and j<len(R):
             if L[i]>=R[j]:
                 a[k]=L[i]
                 i+=1
             else:
                 a[k]=R[j]
                 j+=1
             k+=1
      while i < len(L):
              a[k]=L[i]
              k+=1
              i+=1
      while j < len(R):
              a[k]=R[j]
              j+=1
              k+=1

t=input();
while t > 0:
	t-=1;
	n,m=map(int,raw_input().split());
	A=map(int,raw_input().split());
	B=map(int,raw_input().split());
	C=A+B;
	merge(C,0,n-1,n+m-1);
	for i in C:
		print i,
	print "";
