# 181879
# 정수가 담긴 리스트 num_list가 주어질 때,
# 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    listLength = len(num_list)
    mul = 1
    if listLength > 11:
        return sum(num_list)
    else:
        for x in num_list:
            mul *= x
        return mul

        # return eval('*'.join(list(map(str, num_list))))


num_list = [2, 3, 4, 5]
print(solution(num_list))
