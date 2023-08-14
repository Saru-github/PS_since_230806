# 181887
# 정수 리스트 num_list가 주어집니다.
# 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요.
# 두 값이 같을 경우 그 값을 return합니다.


def solution(num_list):
    odd_num = 0
    even_num = 0

    for x in range(0, len(num_list), 2):
        even_num += num_list[x]
    for x in range(1, len(num_list), 2):
        odd_num += num_list[x]

    return max(even_num, odd_num)
#   return max(sum(num_list[::2]), sum(num_list[1::2]))


num_list = [4, 2, 6, 1, 7, 6]
print(solution(num_list))
