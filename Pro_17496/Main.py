# N : 여름의 일 수
# T : 스타후르츠가 자라는데 걸리는 일 수
# C : 스타후르츠를 심을 수 있는 칸의 수
# P : 스타후르츠 개당 가격 정수

N, T, C, P = map(int, input().split())

print((N - 1) // T * C * P)