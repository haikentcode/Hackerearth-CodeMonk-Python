A,B=map(int,raw_input().split());
s=raw_input();
ans=0;
for i in range(len(s)):
	if(s[i]=='1'):
		ans=(ans+A)%B;
	A=(A*A)%B;
print(ans);
