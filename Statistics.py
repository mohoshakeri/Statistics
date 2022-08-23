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