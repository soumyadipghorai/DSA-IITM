def minimum_platform(schedule):
    sch = schedule
    n = 0
    while sch != []:
        r = []
        d_time = sch[0][2]
        sch.pop(0)
        for k in sch:
            if (k[1] >= d_time):
                d_time = k[2]
                r.append(k)
        for i in r:
            sch.remove(i)
        n += 1
    return n

schedule = eval(input())           
print(minimum_platform(schedule))