#총 N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있다. i번 시험장에 있는 응시자의 수는 Ai명이다.

# 감독관은 총감독관과 부감독관으로 두 종류가 있다. 
# 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고, 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.

# 각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.

# 각 시험장마다 응시생들을 모두 감시해야 한다. 이때, 필요한 감독관 수의 최솟값을 구하는 프로그램을 작성하시오.


# 고사장의수 = N ## 틀린 풀이
# 응시자수 = A
import sys
sys.setrecursionlimit(10**9)
n = int(input())

A = list(map(int,input().split()))

b ,c = map(int,input().split())

cnt=0
def solve(start_val):
    global cnt
    ck=0   
    if start_val <=0:
        return 1
    
    cnt+=1
    #print(start_val-c)
    solve(start_val-c)


for i in range(n):
    cnt+=1
    solve(A[i]-b)

print(cnt)
################# 정답풀이
import sys
sys.setrecursionlimit(10**9)
n = int(input())

A = list(map(int,input().split()))

b ,c = map(int,input().split())


def solve():
    answer=n # 총감독은 무조건 각 고사장에 있어야하므로 고장사장 수만큼 카운트해준다
    for i in A:
        i-=b # 고사장 인원에서 총감독이 감시할수있는 인원을 빼준다
        if i >0: # 인원을 다 감시할수없으며 부감독을 데리고옴
            if i %c: # 총감독이 감시하는 인원을 뺀 현재 고사장 인원을 부감독관의 감시 인원을 나눈 나머지가 1 이상이면 
                     # 부감독관의 수는 (응시자의 수 - 총감독관) / 부감독관 감시 수로 구할 수 있습니다. 
                     #  이 때 나누어 떨어지는 경우는 값이 맞으나, 나머지가 발생하는 경우 부감독관 한 명이 더 있어야 합니다. 
                answer += (i//c+1)
            else:
                answer +=(i//c)
    print(answer)

solve()