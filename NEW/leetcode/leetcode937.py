def reorderLogFiles(logs):
    digit_list = []
    str_list = []
    for log in logs:
        if log.split()[1].isdigit():
            digit_list.append(log)
        else:
            str_list.append(log)
    str_list.sort(key=lambda x: x.split()[1])
    return str_list + digit_list