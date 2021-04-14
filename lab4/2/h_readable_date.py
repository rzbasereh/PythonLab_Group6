# 2-3

DAYS_OF_MONTH = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def get_datetime(timestamp):

    allDays = timestamp // (24 * 60 * 60)

    '''
    Notice: Every year that is exactly divisible by four is a leap year,
    except for years that are exactly divisible by 100,
    but these centurial years are leap years if they are exactly divisible by 400

    Notice: Each leap year has 366 days instead of 365,
     by extending February to 29 days rather than the common 28

    https://en.wikipedia.org/wiki/Leap_year
    '''

    year = 1970
    while allDays >= 365:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            allDays -= 366
        else:
            allDays -= 365
         
        year += 1

    leapYear = False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leapYear = True
    
    remainDays =  allDays + 1
    month = 0
    mIndex = 0
    while True:
        if mIndex == 1 and leapYear:
            monthDays = 29
        else:
            monthDays = DAYS_OF_MONTH[mIndex]

        if remainDays - monthDays < 0:
            break

        remainDays -= monthDays
        month += 1
        mIndex += 1

    if remainDays > 0:
        month += 1
        day = remainDays
    else:
        if month == 2 and leapYear:
            day = 29
        else:
            day = DAYS_OF_MONTH[month - 1]


    extraTime = timestamp % (24 * 60 * 60)

    hour = extraTime // 3600
    minute = (extraTime % 3600) // 60
    second = (extraTime % 3600) % 60
    
    return "Date & Time: {}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second)


timestamp = 1618343387
datetime = get_datetime(timestamp)
print(datetime)
