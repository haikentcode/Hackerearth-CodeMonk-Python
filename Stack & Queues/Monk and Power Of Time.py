class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
n=input();
A=map(int,raw_input().split());
B=map(int,raw_input().split());
i = 0;
time = 0;
j=0;
C = Queue()
while j<n:
	C.enqueue(A[j])
	j+=1;
while (not C.isEmpty()):
	num = C.dequeue();
	time+=1;
	if (num != B[i]) :
		C.enqueue(num)
	else :
		i+=1;
print(time);
