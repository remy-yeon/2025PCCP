#sweq 1984 문제 
# 수 10개를 입력받아 최대 최소를 제외하고 나머지의 평균값을 구하는 문제 

def solve():
    m, n, s = 0,0,0 
    arr = list(map(int, input().split()))
    m = max(arr)
    # print(m)
    n = min(arr)
    # print(n)
    arr.remove(m)
    arr.remove(n)
    # s = sum(arr)
    # print(s)
    ans = sum(arr) / len(arr)
    # print(ans)
    ans = round(ans)
    # print(ans)
    return ans
#test case 입력 

solve()

# T = int(input())

# for tc in range(1,tc+1):
#     ans = solve()
#     print(f"#{tc} {ans}")