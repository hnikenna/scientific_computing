def add_time(start, duration, date=''):
    time1 = start.split()[0]
    mValue = start.split()[1]
    dates = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
    ]
    new_day = 0

    time2 = duration
    time1_l = time1.split(':')
    time2_l = time2.split(':')
    new_hour = int(time1_l[0]) + int(time2_l[0])

    # MINUTE
    new_minute = int(time1_l[1]) + int(time2_l[1])

    while new_minute > 59:
        new_minute -= 60
        new_hour += 1

    if len(str(new_minute)) == 1:
        new_minute = '0' + str(new_minute)

    # HOUR
    while new_hour >= 12:
        if new_hour == 12:
            if mValue == 'AM':
                mValue = 'PM'
            elif mValue == 'PM':
                mValue = 'AM'
                new_day += 1
            break
        elif new_hour != 12:
            new_hour -= 12
            if mValue == 'AM':
                mValue = 'PM'
            elif mValue == 'PM':
                mValue = 'AM'
                new_day += 1
            if new_hour < 12:
                break
            elif new_hour == 12:
                continue


    if date:
        date_index = dates.index(date.title())
        for i in range(new_day):
            c = dates.pop(0)
            dates.append(c)
        date = dates[date_index]

    # NEW DAY COUNT
    if new_day == 1:
        new_day = '(next day)'
    elif new_day > 1:
        new_day = f'({new_day} days later)'

    # OUTPUT TIME
    new_time = str(new_hour) + ':' + str(new_minute) + ' ' + mValue
    if date:
        new_time += ', ' + str(date)

    if new_day != 0:
        new_time += ' ' + str(new_day)

    return new_time


print(add_time("11:43 PM", "24:20", "tueSday"))
