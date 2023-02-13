import random
n = int(input())
numlist=[]
for i in range(n):
    numlist.append(random.randint(1, 1000))
print("Dãy số ban đầu là","\n",numlist)
for i in range (n-1):
    for j in range(n-i-1):
        if numlist[j] > numlist[j+1]:
            index = numlist[j]
            numlist[j] = numlist[j+1]
            numlist[j+1] = index
print("Dãy số kết quả là","\n",numlist)
# anh nho em nhieu lam
