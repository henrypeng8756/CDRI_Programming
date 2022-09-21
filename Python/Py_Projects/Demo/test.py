dayList = []
for week in range(1, 5):
    print('Week %d:' % (week))
    for days in range(1, 4):
        i = float(input('Day %d:' % (days)))
        dayList.append(i)
print('Average:', '%.2f' %(sum(dayList)/12))
print('Highest:', max(dayList))
print('Lowest:', min(dayList))
