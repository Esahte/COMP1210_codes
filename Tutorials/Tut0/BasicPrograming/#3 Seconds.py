def seconds(initSecs):
    secs = initSecs
    timeRange = {'hour':0, 'minute':0, 'second':0}

    while secs != 0:
        while secs % 60 != 0:
            timeRange['second'] += 1
            secs -= 1
        secs = secs//60
        while secs%60 != 0:
            timeRange['minute'] += 1
            secs -= 1
        timeRange['hour'] += secs//60
        break

    # list to store keys in dictionary with values
    timeLst = []
    # iterates through dictionary to extract keys with values
    for (k, v) in timeRange.items():
        if v != 0:
            timeLst.append(k)

    # stores initial list size
    initialLen = False
    if len(timeLst) == 1: initialLen = True

    # creates statement to be returned
    statement = f'{initSecs} sec is '
    while len(timeLst)>1:
        if timeRange[timeLst[0]] > 1: statement += f'{timeRange[timeLst[0]]} {timeLst.pop(0)}s, '
        else: statement += f'{timeRange[timeLst[0]]} {timeLst.pop(0)}, '
    if timeRange[timeLst[0]] == 1 and initialLen: statement += f'{timeRange[timeLst[0]]} {timeLst.pop(0)}'
    elif timeRange[timeLst[0]] > 1 and initialLen: statement += f'{timeRange[timeLst[0]]} {timeLst.pop(0)}s'

    elif timeRange[timeLst[0]] > 1: statement += f'and {timeRange[timeLst[0]]} {timeLst.pop(0)}s'
    else: statement += f'and {timeRange[timeLst[0]]} {timeLst.pop(0)}'

    return statement


prompt = int(input('Enter a time range between 1 - 86,400 in secs: '))
print(seconds(prompt))