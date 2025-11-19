def make_snail(n):
    grid = [[0] * n for _ in range(n)]
    top, left = 0, 0
    bottom, right = n - 1, n - 1
    num = 1

    while True:
        # 1) 위쪽 줄 (왼 → 오)
        for c in range(left, right + 1):
            grid[top][c] = num
            num += 1
        top += 1
        if top > bottom:
            break

        # 2) 오른쪽 줄 (위 → 아래)
        for r in range(top, bottom + 1):
            grid[r][right] = num
            num += 1
        right -= 1
        if left > right:
            break

        # 3) 아래쪽 줄 (오 → 왼)
        for c in range(right, left - 1, -1):
            grid[bottom][c] = num
            num += 1
        bottom -= 1
        if top > bottom:
            break

        # 4) 왼쪽 줄 (아래 → 위)
        for r in range(bottom, top - 1, -1):
            grid[r][left] = num
            num += 1
        left += 1
        if left > right:
            break

    return grid


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    grid = make_snail(n)

    print(f"#{tc}")
    for row in grid:
        print(*row)
