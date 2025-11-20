#2001 파리 퇴치 


T = int(input()) # test case

for tc in range(T):
N, M = map(int, input().split()) # N, M 입력 받기
arr = [list(map(int, input().split())) for _ in range(N)] # NxN 배열 입력받기

sum_value = 0
for i in range(N - M + 1): # 불필요한 연산을 줄이기 위해
for j in range(N - M + 1): # 0부터 N-M 크기 까지 순회

catch_fly = 0
for p in range(M):
for q in range(M):
catch_fly += arr[i + p][j + q] # 각 영역을 순회하여 파리 수 저장

if catch_fly > sum_value: # 현재 잡은 파리 수가 기존 보다 크다면 갱신
sum_value = catch_fly

print(f"#{tc + 1} {sum_value}")