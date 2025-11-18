# # # n = int(input())
# # # f = float(input())
# # # s = input().strip() # 양쪽 공백 제거 2

# # H, W = map(int, input().split())
# # board = [list(input().strip()) for _ in range(H)]
# # # board[i][j] 가 i행 j열 문자
# # print(board)

# i = 0
# while i<5:
#     print("조건 전:", i)
#     i = i+1
#     print("조건 후:", i)
#     print("\n")
    
    
# print("#######반복문 종료 #######")
# print(i)

#예시 

for x in range(1,10):
    if x == 7:
        break #x값이 7가 되는 반복문 순간 종료 
    if x % 2 == 0: #원소가 짝수라면 
        continue #원소가 짝수면 넘어가기 
    print("출력되는 원소는 1,3,5중 하나여야 함")
    print(x) #홀수인 원소만 출력 단, 7일땐 종료라서 예상 출력은 1,3,5