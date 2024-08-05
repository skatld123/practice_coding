from collections import defaultdict


def solution(record):
    answer = []
    msg_dict = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    user_dict = defaultdict(int)

    for action in record:
        list_act = action.split()
        if len(list_act) > 2:  # Enter, Change
            act, id, name = list_act
            user_dict[id] = name
            if act == "Change":
                continue
        else:  # Leave
            act, id = list_act
        answer.append(id + "/" + msg_dict[act])

    for i in range(len(answer)):
        id, msg = answer[i].split("/")
        answer[i] = user_dict[id] + msg
    return answer
