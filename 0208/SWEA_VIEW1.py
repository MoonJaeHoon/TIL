import sys
sys.stdin = open("input.txt")

## 1번 풀이 : 58,984 kb & 147 ms
T = 10
여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    top = list(map(int, input().split()))

    answer = 0
    for ind in range(2, N-2):
        highest=0
        for side in [-2,-1,1,2]:
            if top[ind+side]>highest:
                highest = top[ind+side]
        if highest < top[ind]:
            answer += top[ind]-highest
    print(f"#{test_case} {answer}")

## 2번 풀이 : 59,504 kb & 142 ms
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    top = [int(i) for i in input().split()]

    answer = 0
    for ind in range(2, N - 2):
        highest = 0
        for side in [-2, -1, 1, 2]:
            if top[ind + side] > highest:
                highest = top[ind + side]
        if highest < top[ind]:
            answer += top[ind] - highest
    print(f"#{test_case} {answer}")
