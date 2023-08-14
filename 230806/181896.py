# 181896
# 정수 리스트 num_list가 주어질 때,
# 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.


def solution(num_list):
    for x in num_list:
        if x < 0:
            return num_list.index(x)
    return -1


num_list = [13, 22, 53, 24, 15, 6]
print(solution(num_list))
