# 181928
# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    evenArr = []
    oddArr = []
    for x in num_list:
        if x % 2 == 0:
            evenArr.append(str(x))
        else :
            oddArr.append(str(x))

    return int("".join(evenArr)) + int("".join(oddArr))

        

num_list = [3, 4, 5, 2, 1]
print(solution(num_list))
