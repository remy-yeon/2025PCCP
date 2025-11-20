def solve():
    #정수 입력받아서 생성     
    N, M= map(int,input().split())
    Gsum = 0 
    Ngrid = []
    Mgrid = [[0] * N for _ in range(M)] #파리채 생성 
    # print(Mgrid)
    #정수 입력받아서 그리드에 저장 ->각 row를 받아서 1차원 리스트의 원소로 넣기 
    for _ in range(N): 
        row = list(map(int, input().split()))
        Ngrid.append(row)
    # print(Ngrid)

    #Ngrid를 row와 col로 완전 탐색하면서 M grid만큼 sum을 항상 구하기 
    for r in range(N-M+1): 
        for c in range(N-M+1):
            current = 0 #여기가 문제 
            for i in range(r, r+M):
                for j in range(c, c+M):
                    current += Ngrid[i][j] #i,j번째 있는 것들의 합 
            if current > Gsum:
                Gsum = current
            
    print(Gsum)
    return Gsum 
            
            # if(r and c == N-M+1):
                # Gsum = sum(Mgrid)
        
solve()