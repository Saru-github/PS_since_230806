# 181831
# n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
# 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]


def solution(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][y] != arr[y][x]:
                return 0
    return 1


arr = [[5, 192, 33], [192, 72, 95], [33, 95, 999]]
print(solution(arr))
