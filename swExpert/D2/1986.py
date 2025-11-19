#1986 지그재그 

T = int(input())

for tc in range(1,T+1):
    n = int(input()) #처음 받는 정수 

    ans = sum(map(lambda x: -x if x % 2==0 else x, range(1,n+1)))
    
    
    print(f"#{tc} {ans}")