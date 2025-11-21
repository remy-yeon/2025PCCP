def solve():
    N = int(input())
    #방향 인덱스 변수 초기화 
    top = 0
    left = 0
    right = N-1
    bottom = N-1
    grid = [[-1]*N]
    num = 0 
    row, col = 0, 0 
    
    #N제곱을 도는 이중 반복문 
    for i in range(N):
        for j in range(N):
            while True:
                for row in range(left, right): 
                    grid[top][row] = num 
                    if left <right:
                        num +=1
                        left +=1
                    
                for col in range(top, bottom):
                    grid[col][right] = num 
                    if top < bottom:
                        num += 1
                        top +=1

                for row in range(right, left+1, -1): #이런거 였음 
                    grid[bottom][row] = num 
                    if right > left:
                        num += 1
                        right -=1
                
                for col in range(bottom, top+1, -1):
                    grid[col][left] = num 
                    if bottom > top+1:
                        num +=1
                        bottom +=1
    # print(grid) 
    return grid                 

T = int(input())
ans = []
for tc in range(1,T+1):
    print(f"#{tc}")
    
    ans = solve()
    for row in ans:
        print(*row)