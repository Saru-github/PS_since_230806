# 181920
# 정수 start와 end가 주어질 때, start부터 end까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.


def solution(start, end):
    return [i for i in range(start, end+1, 1)]


start = 3
end = 10
print(solution(start, end))
