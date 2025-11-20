def solve(n):
    result = []  # 최종 출력용 문자열들을 모을 리스트

    for i in range(1, n+1):
        s = str(i)
        cnt = 0

        # 이번 숫자 i에서 3/6/9 개수 세기
        for ch in s:
            if ch in '369':
                cnt += 1

        if cnt == 0:
            result.append(s)         # 숫자 그대로
        else:
            result.append('-' * cnt) # 3/6/9 개수만큼 '-'

    return result


n = int(input())
ans = solve(n)
print(*ans)
