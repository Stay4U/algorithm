'''
* 알고리즘
그리디(욕심쟁이 또는 탐욕 알고리즘)
현재 상황에서 지금 당장 좋은 것만 선택

* 문제
가장 높은 카드 선택

N * M 행렬에서 행 선택
선택한 행에서 가장 낮은 숫자 선택
선택한 숫자가 가장 큰 숫자이도록 선택하는 문제(가장 낮은 숫자를 선택하는게 룰)

1 <= N
M <= 100

* 예시
입력예시
3 3
3 1 2
4 1 4
2 2 2

출력예시
2

선택 행은 3행

* 비고


* 구현
'''
n, m = map(int, input().split()) # row, column

for i in range(n):
  result.append(min(list(map(int, input().split()))))
  
print(max(result))









