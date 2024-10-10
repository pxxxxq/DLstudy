'''
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
'''

#위의 코드는 메모리를 과다하게 먹는다...
#해결을 위해 itertools라는 순열, 조합을 만들수 있는 패키지를 이용하자. => itertools는 모든 부분 집합을 메모리에 한꺼번에 저장하지 않고 필요한 시점에 생성할 수 있다.

from itertools import permutations

N,K=map(int,input().split()) 

B = list(map(int, input().split()))
B = [b-K for b in B]
cnt=0

for case in permutations(B,N):
    wt=0
    bull=1
    for i in case:
        wt += i
        if wt < 0:
            bull = 0
            break
    if bull == 1:
        cnt += 1

print(cnt)






