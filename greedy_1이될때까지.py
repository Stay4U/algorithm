'''
* 알고리즘
그리디(욕심쟁이 또는 탐욕 알고리즘)
현재 상황에서 지금 당장 좋은 것만 선택

* 문제
어떤 수 N을 1로 만들어야 함
1) N - 1
2) N 이 K로 나누어 떨어지는 경우에만 N / K
N을 1로 만드는 최소 횟수를 구하자

* 예시
N : 25
K : 5
답 : 2 

* 비고

* 구현
'''
n, k = map(int, input().split())
count = 0
count += n - (int(n / k) * k)
count += int(n // k)

print(count)
