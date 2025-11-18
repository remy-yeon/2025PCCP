def solve():
    ans = 0 #이거 없으면 런타임 에러 (UnboundLocalError)
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if(arr[i] % 2 != 0): 
            ans += arr[i]
    return ans
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answ = solve()
    print(f"#{test_case} {answ}")
