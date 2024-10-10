N,K=map(int,input().split()) 

B = list(map(int, input().split()))
B= [b-K for b in B]
lst=[[b] for b in B]

for n in range(1,N+1):
    for l in lst:
        for b in B:
            if sum(l)+b>=0:
                lst.append(l+[b])
    for j in lst:
        if len(j)!=n+1:
            lst.remove(j) 

print(lst)







