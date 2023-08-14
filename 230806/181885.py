# 181885
# 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
# todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.


def solution(todo_list, finished):
    answer = []
    index = 0
    for x in todo_list:
        if not finished[index]:
            answer.append(x)
        index += 1
    return answer


todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]
print(solution(todo_list, finished))
