from sets import Set
t=input();
while t > 0:
	t-=1;
	n=input();
	S=[];
	i=0;
	while i < n:
		s=raw_input();
		S.append(s);
		i+=1;
	S=list(set(S));
	S.sort();
	for x in S:
		print x;
