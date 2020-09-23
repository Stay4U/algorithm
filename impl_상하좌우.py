'''
* 알고리즘
머릿속에 있는 알고리즘을 구현해내는 능력을 향상시키자

* 문제
N * N 행렬로 이루어진 공간에서 제시된 이동방향으로 이동한 뒤 마지막 좌표를 출력.

가장 왼쪽 위 좌표가 (1, 1)이고, 가장 오른쪽 아래 좌표가 (N, N)이다.
시작 좌표는 항상 (1, 1)이다.
이동방향은 상하좌우(UDLR)로 한 칸씩 이동한다.
N * N 행렬을 벗어나는 이동방향은 취소된다.(자리에서 이동하지 않는다.)


* 예시
입력예시 :
5
R R R U D D

출력예시 :
3 4

* 비고

* 구현
'''
n = int(input())
plans = input().split()

x, y = 1, 1 # start position

dx = [0, 0, -1, 1] # L R U D
dy = [-1, 1, 0, 0] # L R U D

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

      if nx > n or nx < 1 or ny > n or ny < 1 : 
        continue
      x, y = nx, ny

print(x, y)
