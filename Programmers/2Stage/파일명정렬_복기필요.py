def solution(files):
    answer = []
    split_list = []
    for i in range(len(files)):
        file = files[i]
        s, f = check_digit(file)
        if f == len(file):
            head = file[:s].lower()
            number = int(file[s:])
            tail = None
        else:
            number = int(file[s:f])
            head = file[:s].lower()
            tail = file[f + 1 :]
        split_list.append([i, head, number, tail])

    split_list.sort(key=lambda x: [x[1], x[2]])

    for spl in split_list:
        answer.append(files[spl[0]])

    return answer


def check_digit(name):
    start = 0
    finish = 0
    for i in range(len(name)):
        if start == 0 and name[i].isdigit():
            start = i
        elif start != 0 and not name[i].isdigit():
            finish = i
            break
    if start != 0 and finish == 0:
        finish = len(name)
    return (start, finish)
