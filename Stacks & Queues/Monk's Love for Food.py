class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
q=input();
S=Stack();
while q:
	q-=1;
	A=map(int,raw_input().split());
	if A[0] == 1:
		if(S.isEmpty()):
			print("No Food");
		else :
			print(S.pop())
	else :
		S.push(A[1])
