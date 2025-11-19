def think():
    n = int(input())
    grid = [[0]*n for _ in range(n)]
    #print(grid)
    top = 0 # 가장 위 row 
    left = 0 #가장 왼쪽 col 
    right = n-1 #가장 우측 col 
    bottom = n-1 # 가장 아래쪽 row 
    
    #첫 시작 수 1 
    num = 1
    num = grid[top][left] #0 , 0 
    
    left += 1 #1
    num +=1 #2
    num = grid[top][left] #0, 1
    
    left += 1 # 2
    num +=1 #3
    num = grid[top][left] #0, 2 
    
    #left가 right가 되는 시점 
    top +=1 #1
    num +=1 #4 
    num = grid[top][left] #1,2 
    
    #left가 아직 2이니까 top + 1 
    top +=1 #2
    num +=1 #5 
    num = grid[top][left]
    
    #top이 bottom이 되는 시점 
    left -= 1 #1 
    num +=1 #6
    num = grid[top][left]
    
    #아직 left가 1이니까 0으로 
    left -=1 #0
    num +=1 #7 
    num = grid[top][left] #2,0 
    
    #left가 0이 됐으니까 top -1
    top -=1 
    num +=1 #8 
    num = grid[top][left]
    
    #겉 테두리를 다 돌았으므로, 
    
    

def solve(n): 
    grid = [[0]*n for _ in range(n)]
    top = 0
    left =0
    right = n-1
    bottom = n-1
    num = 1 
    
    while True:
        for c in range(left, right+1):
            grid[top][c] = num 
            num+=1 
        top +=1     
        if top > bottom:
            break
        for r in range(top, bottom+1):
            grid[r][right] = num 
            num +=1
        right -=1     
        if left > right:
            break
        
        for c in range(right, left-1, -1): #이부분 주의 
            grid[bottom][c] = num 
            num +=1
        bottom -=1     
        if top > bottom:
            break
        
        for r in range(bottom, top-1, -1):
            grid[r][left] = num 
            num +=1
        left +=1     
        if left > right:
            break
        
    return grid 

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    n = int(input())
    grid = solve(n)
    
    print(f"#{test_case}")
    for row in grid: 
        print(*row)

    