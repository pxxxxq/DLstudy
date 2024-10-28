N,M=map(int,input().split())
lst = [i+1 for i in range(N)]


for _ in range(M):
    i,j=map(int,input().split())
    temp=lst[i-1:j]
    temp.reverse()
    lst[i-1:j]=temp

for i in range(N):
    print(lst[i], end=' ')