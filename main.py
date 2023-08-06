
def solution(num_list):
    for x in num_list:
        if x < 0:
            return num_list.index(x)
    return -1


num_list = [13, 22, 53, 24, 15, 6]
print(solution(num_list))
