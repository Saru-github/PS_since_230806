# 181849
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(num_str):
    return sum([int(x) for x in num_str])


num_str = "123456789"
print(solution(num_str))
