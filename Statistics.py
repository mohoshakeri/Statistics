import statistics

def mean(data):
    if len(data) < 1:
        return 0
    return statistics.mean(data)

def variance(data):
    if len(data) < 2:
        return 0
    return statistics.variance(data)

def stdev(data):
    if len(data) < 2:
        return 0
    return statistics.stdev(data)

def total_growth(list):
    index = 0
    memory = []
    growth = []
    for item in list:
        if index == 0 :
            memory.append(item)
            index += 1
            continue
        memory.append(item)
        growth.append(memory[-1] - memory[-2])
        
    return sum(growth)

def partial_growth(list):
    try:
        if list[-1] != 0:
            result = (list[-1] / list[-2])*100
        else :
            result = (list[-2] * 100)
            return - result
    except ZeroDivisionError:
        if list[-1] != 0:
            result = (list[-1] *100)
            return result
        else:
            result = 100
    return int(result) - 100