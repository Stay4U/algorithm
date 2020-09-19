'''
* 알고리즘
그리디(욕심쟁이 또는 탐욕 알고리즘)
현재 상황에서 지금 당장 좋은 것만 선택

* 문제
숫자를 원소로 하는 배열이 주어질 때, M번 더하여 가장 큰 수를 만들기.
특정 인덱스의 수가 연속해서 더해질 수 있는 횟수는 K.
인덱스가 다르다면 인덱스에 해당하는 수가 같아도 서로 다른 수로 인정.

R1. N : 배열의 크기( B BETWEEN 2 AND 1000)
R2. M : 숫자를 덧셈할 수 있는 횟수( M BETWEEN 1 AND 10000 )
R3. K : 연속해서 같은 수를 덧셈할 수 있는 횟수( K BETWEEN 1 AND 10000 )
R4. K <= M (K는 항상 M보다 작거나 같다)

* 예시
입력예시(공백으로 값 구분, 두 줄 입력) : 
5 8 3
2 4 5 4 6

출력예시 : 46

N : 5
M : 8
K : 3
6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 34

* 비고
한꺼번에 여러 데이터를 입력받는 소스
1) 공백으로 구분하여 입력받기 
m, n, k = map(int, input().split())

2) N개의 수를 공백으로 구분하여 입력받기
변수 = list(map(int, input().split()))

3) data.sort(reverse=True)

* 구현
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
total = 0

#1
'''
while True:
  for i in range(k):
    if m == 0: break
    total += first
    m -= 1
  
  if m == 0: break  
  total += second
  m -= 1

print(total)
'''  
#2
cnt =  (m // (k + 1)) * k
cnt += m % (k + 1)
print( (first * cnt) + (second * (m - cnt)) )

