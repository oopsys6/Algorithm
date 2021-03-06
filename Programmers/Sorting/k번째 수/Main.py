# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    sliceArray = []
    for i in range(len(commands)):
        sliceArray.append(array[commands[i][0] - 1 : commands[i][1]])
        resultArray = sorted(sliceArray[0])
        answer.append(resultArray[commands[i][2] - 1])
        sliceArray.pop(0)

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])