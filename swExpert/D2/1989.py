#1989. 초심자의 회문 검사
# 단어 가운데 숫자 기준 
# 양옆으로 가면서 똑같은지 아닌지 확인 -> 홀수일때만 적용 가능 

#짝수 홀수 상관없이 할수 있는 경우로 풀이 
def solve():
    st = str(input())
    left = 0
    right = len(st) - 1 
    ans = 0
    for _ in range(len(st)):
        if st[left] == st[right]:
            left += 1
            right -= 1
            ans = 1
        else:
            ans = 0
    return ans 

T = int(input())
for tc in range(1,T+1):
    ans = solve()
    print(f"#{tc} {ans}")