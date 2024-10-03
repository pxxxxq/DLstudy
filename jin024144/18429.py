N,K=map(int,input().split()) 

lst = list(map(int, input().split()))
lst = [k-4 for k in lst]
l3=[[] for _ in range(N+1)]
l3[0]=lst
for j in range(N):
    for i in l3[j]:
        if i >= 0:
            l3[j+1].append(i)
    l3[j+1]=[k-4 for k in l3[j+1]]




print(l3)

