# 12933
# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

def solution(n):
    nList = list(map(int, str(n)))
    newL = sorted(nList, reverse=True)
    strings = [str(i) for i in newL]
    a_string = "".join(strings)
    return int(a_string)


print(solution(118372))
