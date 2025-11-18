def solve():
    arr = list(map(int, input().split())) #입력받은 정수를 리스트에 저장 1 
    return sum(arr) #sum 함수 내장 - 각 원소들의 합 

T = int(input()) # 반복할 테스트 케이스 횟수 

for i in range(1, T+1):
    ans = solve()
    print(f"#{i} {ans}") # 테스트 출력 케이스 포맷 

    