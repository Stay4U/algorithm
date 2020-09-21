'''
* 알고리즘
그리디(욕심쟁이 또는 탐욕 알고리즘)
현재 상황에서 지금 당장 좋은 것만 선택
* 문제
coins에 있는 수를 더하여 n을 만들 수 있는 최소 덧셈 횟수 구하기
* 예시
n = 1260
coins = [500, 100, 50, 10]
* 비고
아래의 알고리즘은 coins에 이웃하는 숫자가 배수관계여야 가능
배수관계가 아닌 경우 예시 : n = 800, coins=[500, 400, 100] > 최소 횟수 2회 (400*2), 알고리즘 4회(500*1, 100*3)
* 구현
'''
