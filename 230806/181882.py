# 181882
# 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고,
# 50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    answer = []
    for x in arr:
        if x >= 50 and x % 2 == 0:
            answer.append(int(x / 2))
        elif x <= 50 and x % 2 == 1:
            answer.append(x * 2)
        else:
            answer.append(x)
    return answer

# return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]

arr = [1, 2, 3, 100, 99, 98]
print(solution(arr))
