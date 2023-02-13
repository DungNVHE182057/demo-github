import random
n = int(input())
numlist=[]
for i in range(n):
    numlist.append(random.randint(1, 1000))
print("Dãy số ban đầu là","\n",numlist)
for i in range (1,n):
    key = numlist[i]
    j = 0
    while numlist[i]>numlist[j]:
        j+=1
    for k in range(0,i-j):
        numlist[i-k]=numlist[i-k-1]
    numlist[j]=key
print("Dãy số kết quả ,à","\n",numlist)