'''
그리디(욕심쟁이 또는 탐욕 알고리즘)
현재 상황에서 직금 당장 좋은 것만 고르는 방법

* 문제
coins에 있는 수를 이용하여 n을 만들 수 있는 최소 갯수 구하기

* 비고
아래의 알고리즘은 coins에 이웃하는 숫자가 배수관계여야 가능

'''
n = 1260
nCopy = n
coins = [500, 100, 50, 10]

count = 0
for coin in coins:
  count += int(nCopy / coin)
  nCopy %= coin
  
print("%d를 만들수 있는 가장 작은 수는 %s입니다." %(n, count))
