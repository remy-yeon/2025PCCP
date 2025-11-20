#1926 369게임 
# 정수 n을 입력받고 그 1부터 n까지의 정수들을 출력하는데 이때 3,6,9의 경우 -로 대신 출력
# 36일 경우 -- 로 출력함 35일 경우 -5로 출력 

''' 오답 노트
- 

''' 
def solve(n):
    for i in range(n+1): #0부터 n까지 돎 
        s = str(i)
        if s == '3' or s =='6' or s == '9': #여기서 문제 발생 
            s = '-'
        print(s)
            # print(*digits)
    # return s #여기 문제 

n = int(input())
for _ in range(n):
    ans = solve(n)
    for row in ans:
        print(*row)