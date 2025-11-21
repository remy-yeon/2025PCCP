def solve():
    N = int(input())
    #방향 인덱스 변수 초기화 
    top = 0
    left = 0
    right = N-1
    bottom = N-1
    
    grid = [[-1]*N] #차이:이건 1차원 배열  1*N과 같음 
    num = 0 #num은 저장되는 값이므로 문제 조건에 맞게 1로 초기화해야함 
    row, col = 0, 0 
    
    #N제곱을 도는 이중 반복문 
    for i in range(N): # 이부분에서 틀린게 이중 반복문 안에 무한 루프를 넣는게 아니라 무한 루프 안에 반복문을 넣어야함, 
        #해당 문제에서는 그림으로 보이는것만 grid일 뿐, 이 4가지 방향으로 푸는 방법에선 이중반복문이 필요 없음 
        for j in range(N):
            while True:
                for row in range(left, right):  # n-1인 right 까지 돌려면 right+1해야함  
                    grid[top][row] = num 
                    #num +=1은 여기서 해야함, 반복문 안에 있어야 계속 Num이 증가하니까 
                    if left <right: #l->r로 이동했을때 그만 움직이게 되는 경우는 마지막 줄 top이 bottom보다 커졌을 경우 즉, 더이상 내려갈 top이 없는 경우 
                        num +=1
                        left +=1 #left는 이미 for문 조건에 들어가있기 때문에 위 if문을 종료시키는 조건인 top +=1을 해야함 
                    
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