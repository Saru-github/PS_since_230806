
def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0


my_string = "banana"
target = "ana"
print(solution(my_string, target))
